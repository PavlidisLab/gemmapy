#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guard the response types that sdk-gen/patch-openapi.py asserts on the spec's behalf.

The Gemma spec declares the payload of several endpoints as an untyped
``data: array of object``, even though the endpoint really returns a specific
value object. patch-openapi.py re-points those responses at a typed container so
the generated models carry the payload type the processors need.

That is an assumption made on the server's behalf, and it fails quietly: if an
endpoint starts returning something else, the generated model simply ignores the
unknown keys and ``sub.access_field`` yields NaN for every column rather than
raising. These tests fetch one page of raw JSON per re-typed endpoint and assert
the keys still fit the type we asserted, so upstream drift shows up here instead
of in somebody's analysis.
"""
import ast
import json
import os
import pathlib
import time

import pytest

import gemmapy
from gemmapy import sdk
from gemmapy.sdk.rest import ApiException

api = gemmapy.GemmaPy()

PATCHER = pathlib.Path(__file__).resolve().parent.parent / "sdk-gen" / "patch-openapi.py"


def _item_types():
    """Read ITEM_TYPES out of patch-openapi.py without importing it (it needs PyYAML,
    which is a code-generation dependency rather than a test one)."""
    tree = ast.parse(PATCHER.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "ITEM_TYPES" for t in node.targets
        ):
            return ast.literal_eval(node.value)
    raise AssertionError("ITEM_TYPES not found in %s" % PATCHER)


ITEM_TYPES = _item_types()

# operationId -> (raw SDK method, kwargs) for one small page of live data.
CALLS = {
    "getGenes": ("get_genes", {"limit": 3}),
    "getGeneProbes": ("get_gene_probes", {"gene": "ENSG00000157540", "limit": 3}),
    "getPlatforms": ("get_platforms", {"limit": 3}),
    "getPlatformsByIds": ("get_platforms_by_ids", {"platform": ["GPL1355"]}),
    "getPlatformDatasets": ("get_platform_datasets", {"platform": "GPL1355", "limit": 3}),
    "getPlatformElements": ("get_platform_elements", {"platform": "GPL1355", "limit": 3}),
    "getPlatformElement": ("get_platform_element",
                           {"platform": "GPL1355", "probes": ["1367452_at"]}),
    "getPlatformElementGenes": ("get_platform_element_genes",
                                {"platform": "GPL1355", "probe": "1367452_at"}),
    "getResultSets": ("get_result_sets", {"limit": 3}),
    "getTaxonDatasets": ("get_taxon_datasets", {"taxon": "human", "limit": 3}),
    "getTaxonGenes": ("get_taxon_genes", {"taxon": "human", "limit": 3}),
    "getTaxonGeneProbes": ("get_taxon_gene_probes",
                           {"taxon": "human", "gene": "DYRK1A", "limit": 3}),
}

# Re-typed endpoints deliberately left uncovered, with the reason.
UNCOVERED = {
    "getTickets": "curation tickets, requires authentication",
    "getPlatformTickets": "curation tickets, requires authentication",
    "getTicketEvents": "curation tickets, requires authentication and a ticket id",
}


@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)


def test_every_retyped_endpoint_is_accounted_for():
    """Adding an entry to ITEM_TYPES without covering it here (or explaining why
    not) would leave an asserted type unguarded."""
    assert set(ITEM_TYPES) == set(CALLS) | set(UNCOVERED)


def _first_item(raw_body):
    body = json.loads(raw_body)
    data = body.get("data")
    if isinstance(data, list):
        return data[0] if data else None
    return data if isinstance(data, dict) else None


@pytest.mark.parametrize("operation_id", sorted(CALLS))
def test_retyped_payload_matches_asserted_type(operation_id):
    method_name, kwargs = CALLS[operation_id]
    item_type = ITEM_TYPES[operation_id]

    model = getattr(sdk.models, item_type)
    known_keys = set(model.attribute_map.values())

    try:
        # _preload_content=False keeps the raw body, so we see the keys the
        # generated model would otherwise silently drop.
        response = getattr(api.raw, method_name)(_preload_content=False, **kwargs)
    except ApiException as e:
        if e.status in (401, 403):
            pytest.skip("%s needs authentication" % operation_id)
        raise

    item = _first_item(response.data)
    if item is None:
        pytest.skip("%s returned no rows to inspect" % operation_id)

    unknown = set(item) - known_keys
    assert not unknown, (
        "%s returned keys that %s does not declare: %s. The spec types this "
        "payload as a bare object and sdk-gen/patch-openapi.py asserts %s on its "
        "behalf; if the endpoint genuinely changed, update ITEM_TYPES there."
        % (operation_id, item_type, sorted(unknown), item_type)
    )
