Code generation sources
=======================

**This are sources used to generate code in gemmapy/sdk:**

* openapi.yaml - Gemma RESTful API description, the recent description can be
  obtained by downloading https://gemma.msl.ubc.ca/rest/v2/openapi.yaml
* patch-openapi.py - pre-processes openapi.yaml before code generation. It drops
  every non-GET operation, since gemmapy only reads from Gemma and generating the
  admin, ticket and workflow write endpoints costs hundreds of request-body models
  for a surface the wrapper never calls, then prunes the schemas left unreachable.
  It also collapses the response-level ``oneOf`` the spec uses to describe
  cursor pagination, which swagger-codegen v3 cannot express in Python: it emits
  an empty ``InlineResponseNNN`` model, the raw SDK then returns a plain dict and
  every ``process_*(response.data)`` call in the wrapper fails. Each ``oneOf`` is
  reduced to its legacy offset/limit variant; the script exits with an error if
  that variant has an untyped ``data`` payload. It writes a patched copy to a temporary file;
  openapi.yaml is never modified.
* openapi-patches.md - generated manifest listing every change patch-openapi.py
  made, with the sha256 and version of the spec it was applied to. Regenerated on
  every run; commit it alongside the SDK.
* templ/ - customized Swagger templates used in code generation which contains
  a few fixes, the original Swagger templates for Python are available at
  https://github.com/swagger-api/swagger-codegen-generators/tree/master/src/main/resources/handlebars/python

**To produce the code in gemmapy/sdk/:**

Run the generate-sdk.sh script which will create a temporary directory and synchronize the newly generated code with the
content of `../gemmapy/sdk`.

.. code-block:: bash

   ./generate-sdk.sh
