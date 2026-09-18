#!/usr/bin/env python
"""Pre-process the Gemma openapi spec so swagger-codegen v3 can generate a usable
Python SDK.

Why this exists
---------------
The gemma2 spec introduced cursor pagination as an *alternative* 200 response,
expressed as a response-level ``oneOf``::

    "200":
      content:
        application/json:
          schema:
            oneOf:
            - $ref: ".../ResponseDataObjectListBioAssayValueObject"   # legacy offset/limit
            - $ref: ".../CursorPaginatedResponseDataObjectBioAssayValueObject"

swagger-codegen v3's Python generator cannot express ``oneOf`` polymorphism. It
emits an empty ``InlineResponseNNN`` model (no ``swagger_types``, no fields), so
``api_client`` hands back a bare dict and every ``ps.process_*(response.data)``
call in the wrapper dies with ``'dict' object has no attribute 'data'``.

Separately, several endpoints that used to reference a *parameterized* container
(``PaginatedResponseDataObjectGeneValueObject``, whose ``data`` is an array of
``GeneValueObject``) now reference an unparameterized generic
(``PaginatedResponseDataObject``, whose ``data`` is an array of bare ``object``).
Those generate a model whose ``data`` is a list of raw JSON dicts. That is worse
than a crash: ``sub.access_field_dict`` looks up snake_case names against
camelCase JSON keys, so every column silently comes back NaN.

What this does
--------------
1. Drops every non-GET operation. gemmapy only reads from Gemma; generating the
   admin, ticket and workflow write endpoints costs hundreds of request-body
   models for a surface the wrapper never calls.
2. Collapses each response-level ``oneOf`` to its single legacy (non-cursor)
   variant, dropping the ``Cursor*`` alternatives.
3. Where that variant is an unparameterized generic, re-points it at a typed
   container (synthesizing the container schema when the spec no longer defines
   it), restoring the payload item type the wrapper's processors need.

Both steps are recorded in a manifest file so the diff against upstream is
auditable. The downloaded ``openapi.yaml`` itself is never modified: the patched
copy is a build artifact consumed only by swagger-codegen.

Usage:
    python patch-openapi.py <in.yaml> <out.yaml> <manifest.md>
"""
import collections
import datetime
import hashlib
import os
import sys

import yaml

# Endpoints whose surviving (non-cursor) variant is an unparameterized generic,
# mapped to the payload item type its wrapper processor expects. The container
# name is taken from the spec; only the item type is supplied here.
#
# The first block reproduces exactly what the production spec
# (gemma.msl.ubc.ca) generated before gemma2 dropped the parameterized
# containers -- see the prod-vs-gemma2 comparison in the commit that added this
# file. The second block covers endpoints that only exist on gemma2; gemmapy has
# no wrapper for them today, but typing them costs nothing and keeps the
# generated SDK uniform.
ITEM_TYPES = {
    # present in the production spec, verified against its generated SDK
    "getResultSets": "DifferentialExpressionAnalysisResultSetValueObject",
    "getGeneProbes": "CompositeSequenceValueObject",
    "getGenes": "GeneValueObject",
    "getPlatformDatasets": "ExpressionExperimentValueObject",
    "getPlatformElement": "CompositeSequenceValueObject",
    "getPlatformElementGenes": "GeneValueObject",
    "getPlatformElements": "CompositeSequenceValueObject",
    "getPlatforms": "ArrayDesignValueObject",
    "getPlatformsByIds": "ArrayDesignValueObject",
    "getTaxonDatasets": "ExpressionExperimentValueObject",
    "getTaxonGeneProbes": "CompositeSequenceValueObject",
    "getTaxonGenes": "GeneValueObject",
    # gemma2-only endpoints, no gemmapy wrapper yet
    "getTickets": "TicketValueObject",
    "getPlatformTickets": "TicketValueObject",
    "getTicketEvents": "TicketEventValueObject",
}


#: Keys under a path item that are not operations, so they survive the GET-only
#: filter even though they are not verbs.
NON_OPERATION_KEYS = frozenset(
    {"summary", "description", "servers", "parameters", "$ref"})


def drop_non_get(spec):
    """Remove every non-GET operation from the spec, in place.

    gemmapy only ever reads from Gemma, but the spec also describes the admin,
    ticket and workflow endpoints that write. Generating those produces several
    hundred request-body models for an API surface the wrapper never calls, and
    leaves a generated client capable of mutating curation state. gemma.R does
    the same filtering in inst/script/registry.R.

    Returns the list of (path, verb, operationId) removed.
    """
    removed = []
    for path, item in list(spec.get("paths", {}).items()):
        if not isinstance(item, dict):
            continue
        for verb in list(item):
            if verb in NON_OPERATION_KEYS or verb.lower() == "get":
                continue
            op = item[verb]
            oid = op.get("operationId", "?") if isinstance(op, dict) else "?"
            removed.append((path, verb.upper(), oid))
            del item[verb]
        # a path whose only operations were writes carries nothing we can call
        if not any(v.lower() == "get" for v in item):
            del spec["paths"][path]
    return removed


def refs_in(node):
    """Every schema name referenced anywhere under `node`."""
    found = set()
    stack = [node]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            ref = cur.get("$ref")
            if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
                found.add(ref.rsplit("/", 1)[1])
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)
    return found


def prune_unreachable_schemas(spec):
    """Drop schemas no remaining operation can reach, in place.

    swagger-codegen emits a model class for every entry in
    ``components.schemas``, not just the ones the paths use, so dropping the
    write operations orphans their request bodies rather than removing them.
    This walks ``$ref`` from the surviving paths and deletes whatever is left
    unreachable.

    Returns the sorted list of schema names removed.
    """
    schemas = spec.get("components", {}).get("schemas", {})
    reachable = refs_in(spec.get("paths", {}))
    frontier = list(reachable)
    while frontier:
        name = frontier.pop()
        for nested in refs_in(schemas.get(name, {})):
            if nested not in reachable:
                reachable.add(nested)
                frontier.append(nested)

    removed = sorted(set(schemas) - reachable)
    for name in removed:
        del schemas[name]
    return removed


def is_untyped(schema, schemas):
    """True if the container's `data` payload has lost its item type."""
    props = (schema or {}).get("properties", {})
    data = props.get("data")
    if data is None:
        return False
    if data.get("type") == "array":
        return "$ref" not in (data.get("items") or {})
    return data.get("type") == "object" and "$ref" not in data


def typed_container_name(generic, item):
    return generic + item


def synthesize(schemas, generic, item, log):
    """Return the name of a typed container for `generic` carrying `item`,
    creating the schema if the spec no longer defines it."""
    name = typed_container_name(generic, item)
    if name in schemas:
        return name, False
    base = schemas[generic]
    typed = yaml.safe_load(yaml.safe_dump(base))  # deep copy
    data = typed["properties"]["data"]
    ref = {"$ref": "#/components/schemas/" + item}
    if data.get("type") == "array":
        data["items"] = ref
    else:
        typed["properties"]["data"] = ref
    schemas[name] = typed
    return name, True


def main():
    src, dst, manifest_path = sys.argv[1], sys.argv[2], sys.argv[3]

    raw = open(src, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    spec = yaml.safe_load(raw.decode("utf-8"))
    schemas = spec["components"]["schemas"]

    collapsed, retyped, synthesized, skipped = [], [], [], []

    dropped = drop_non_get(spec)

    for path, item in spec.get("paths", {}).items():
        for verb, op in item.items():
            if not isinstance(op, dict) or "responses" not in op:
                continue
            oid = op.get("operationId", "?")
            for code, resp in op["responses"].items():
                for ctype, media in (resp.get("content") or {}).items():
                    schema = media.get("schema") or {}
                    if "oneOf" not in schema:
                        continue
                    refs = [s.get("$ref", "").split("/")[-1] for s in schema["oneOf"]]
                    keep = [r for r in refs if "Cursor" not in r]
                    if not keep:
                        skipped.append((oid, path, code, refs, "no non-cursor variant"))
                        continue
                    chosen = keep[0]
                    media["schema"] = {"$ref": "#/components/schemas/" + chosen}
                    collapsed.append((oid, path, code, ctype, refs, chosen))

                    if is_untyped(schemas.get(chosen), schemas):
                        item_type = ITEM_TYPES.get(oid)
                        if item_type is None:
                            skipped.append((oid, path, code, refs,
                                            "untyped payload, no item type mapped"))
                            continue
                        if item_type not in schemas:
                            skipped.append((oid, path, code, refs,
                                            "item type %s absent from spec" % item_type))
                            continue
                        new_name, made = synthesize(schemas, chosen, item_type, retyped)
                        media["schema"] = {"$ref": "#/components/schemas/" + new_name}
                        retyped.append((oid, path, code, chosen, new_name, item_type))
                        if made:
                            synthesized.append(new_name)

    # after the collapse, so the synthesized containers count as reachable
    orphaned = prune_unreachable_schemas(spec)

    with open(dst, "w", encoding="utf-8") as fh:
        yaml.safe_dump(spec, fh, sort_keys=False, allow_unicode=True, width=1000)

    write_manifest(manifest_path, spec, src, digest,
                   collapsed, retyped, synthesized, skipped, dropped, orphaned)

    print("patch-openapi: dropped %d non-GET operations and %d now-unreachable "
          "schemas, collapsed %d oneOf responses, retyped %d, synthesized %d "
          "schemas, skipped %d"
          % (len(dropped), len(orphaned), len(collapsed), len(retyped),
             len(synthesized), len(skipped)))
    if skipped:
        for oid, path, code, refs, why in skipped:
            print("  skipped %s (%s): %s" % (oid, path, why))


def write_manifest(out, spec, src, digest, collapsed, retyped, synthesized,
                   skipped, dropped, orphaned):
    info = spec.get("info", {})
    servers = spec.get("servers", [{}])
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

    lines = []
    w = lines.append
    w("# openapi.yaml patches applied before code generation")
    w("")
    w("Generated by `sdk-gen/patch-openapi.py`. Do not edit by hand.")
    w("")
    w("| | |")
    w("|---|---|")
    w("| source | `%s` |" % os.path.basename(src))
    w("| server | %s |" % servers[0].get("url", "?"))
    w("| spec version | %s |" % info.get("version", "?"))
    w("| sha256 (unpatched) | `%s` |" % digest)
    w("| patched at | %s |" % now)
    w("")
    w("The downloaded `openapi.yaml` is left untouched; these changes are applied")
    w("to a temporary copy that is fed to swagger-codegen.")
    w("")
    w("## Why")
    w("")
    w("swagger-codegen v3's Python generator cannot express a response-level")
    w("`oneOf`. It emits an empty `InlineResponseNNN` model, which makes the raw")
    w("SDK return a plain dict and breaks every `ps.process_*(response.data)` call")
    w("in the wrapper. Endpoints that also lost their parameterized response")
    w("container are re-typed, because an untyped `data` payload deserializes to")
    w("raw camelCase dicts that the snake_case processors silently read as NaN.")
    w("")

    w("## 1. Dropped non-GET operations (%d)" % len(dropped))
    w("")
    w("gemmapy only reads from Gemma. Generating the write endpoints produces")
    w("hundreds of request-body models the wrapper never calls, and yields a")
    w("client able to mutate curation state. gemma.R filters the same way in")
    w("`inst/script/registry.R`.")
    w("")
    if dropped:
        by_verb = collections.Counter(verb for _, verb, _ in dropped)
        w("| verb | operations removed |")
        w("|---|---|")
        for verb, n in sorted(by_verb.items()):
            w("| %s | %d |" % (verb, n))
        w("")
        w("<details><summary>full list</summary>")
        w("")
        for path, verb, oid in sorted(dropped, key=lambda r: (r[0], r[1])):
            w("- `%s %s` — `%s`" % (verb, path, oid))
        w("")
        w("</details>")
    else:
        w("_None._")
    w("")

    w("## 2. Schemas pruned as unreachable (%d)" % len(orphaned))
    w("")
    w("swagger-codegen emits a model for every entry in `components.schemas`,")
    w("so removing the write operations orphans their request bodies rather")
    w("than deleting them. These are the schemas no surviving operation can")
    w("reach through `$ref`.")
    w("")
    if orphaned:
        w("<details><summary>full list</summary>")
        w("")
        for name in orphaned:
            w("- `%s`" % name)
        w("")
        w("</details>")
    else:
        w("_None._")
    w("")

    w("## 3. Collapsed `oneOf` responses (%d)" % len(collapsed))
    w("")
    w("The cursor-pagination alternatives are dropped and the legacy")
    w("offset/limit variant is kept, matching how the gemmapy wrapper paginates.")
    w("")
    w("| operationId | path | code | variants in spec | kept |")
    w("|---|---|---|---|---|")
    for oid, path, code, ctype, refs, chosen in collapsed:
        dropped = ", ".join("~~%s~~" % r if r not in (chosen,) else r for r in refs)
        w("| `%s` | `%s` | %s | %s | `%s` |" % (oid, path, code, dropped, chosen))
    w("")

    w("## 4. Re-typed response payloads (%d)" % len(retyped))
    w("")
    w("These endpoints now reference an unparameterized generic whose `data` is an")
    w("array of bare `object`. Each is re-pointed at a typed container so the")
    w("generated models carry the payload type the processors expect.")
    w("")
    if retyped:
        w("| operationId | generic in spec | replaced with | payload item |")
        w("|---|---|---|---|")
        for oid, path, code, chosen, new_name, item_type in retyped:
            w("| `%s` | `%s` | `%s` | `%s` |" % (oid, chosen, new_name, item_type))
    else:
        w("_None._")
    w("")

    w("## 5. Schemas synthesized (%d)" % len(synthesized))
    w("")
    w("Typed containers the spec no longer defines, rebuilt from the generic")
    w("container plus the payload item type.")
    w("")
    if synthesized:
        for name in sorted(set(synthesized)):
            w("- `%s`" % name)
    else:
        w("_None._")
    w("")

    w("## 6. Left alone (%d)" % len(skipped))
    w("")
    if skipped:
        w("| operationId | path | reason |")
        w("|---|---|---|")
        for oid, path, code, refs, why in skipped:
            w("| `%s` | `%s` | %s |" % (oid, path, why))
    else:
        w("_None._")
    w("")

    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
