Code generation sources
=======================

**This are sources used to generate code in gemmapy/sdk:**

* openapi.yaml - Gemma RESTful API description, the recent description can be
  obtained by downloading https://gemma.msl.ubc.ca/rest/v2/openapi.yaml
* templ/ - customized Swagger templates used in code generation which contains
  a few fixes, the original Swagger templates for Python are available at
  https://github.com/swagger-api/swagger-codegen-generators/tree/master/src/main/resources/handlebars/python

**To produce the code in gemmapy/sdk/:**

Run the generate-sdk.sh script which will create a temporary directory and synchronize the newly generated code with the
content of `../gemmapy/sdk`.

.. code-block:: bash

   ./generate-sdk.sh
