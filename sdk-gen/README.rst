Code generation sources
=======================

**This are sources used to generate code in gemmapy/sdk:**

* openapi.yaml - Gemma RESTful API description, the recent description can be
  obtained by downloading https://gemma.msl.ubc.ca/rest/v2/openapi.yaml
* templ/ - customized Swagger templates used in code generation which contains
  a few fixes, the original Swagger templates for Python are available at
  https://github.com/swagger-api/swagger-codegen-generators/tree/master/src/main/resources/handlebars/python

**To produce the code in gemmapy/sdk/:**

(1) Get `Swagger Codegen 3.0.35 <https://github.com/swagger-api/swagger-codegen/tree/3.0.35>`_ jar, e.g:

    .. code-block:: bash

       wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.35/swagger-codegen-cli-3.0.35.jar -O swagger-codegen-cli.jar

(2) Run the generate-sdk.sh script which will create a temporary directory and
    synchronize the newly generated code with the content of `../gemmapy/sdk`.

    .. code-block:: bash

       ./generate-sdk.sh

The current `gemmapy/sdk` was generated with Swagger Codegen 3.0.35 and
openapi.yaml (of 2022-10-14, REST API v.2.5.1), templ/ presented in here.
