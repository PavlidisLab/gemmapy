Code generation sources
=======================

**This are sources used to generate code in gemmapy/sdk:**

* openapi.yaml - Gemma RESTful API description, the recent description can be obtained by downloading
  https://dev.gemma.msl.ubc.ca/rest/v2/openapi.yaml
* templ/ - customized swagger templates used in code generation

**To produce the code in gemmapy/sdk/:**

(1) Get `Swagger Codegen 3.0 <https://github.com/swagger-api/swagger-codegen/tree/3.0.0>`_ jar, e.g: 
    
    .. code-block:: bash
    
       wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.31/swagger-codegen-cli-3.0.31.jar -O swagger-codegen-cli.jar
       
(2) Make a temporary directory, :code:`{temp_path}`. Copy openapi.yaml, templ/ and the swagger jar there.

(3) Generate the code
    
    .. code-block:: bash

       cd {temp_path}
       java -jar swagger-codegen-cli.jar generate -i openapi.yaml -l python -DpackageName=sdk -t templ --template-engine=handlebars -o ./sdk

(4) Copy generated code to proper location
    
    :code:`cp -a sdk/sdk {package_path}/gemmapy/sdk`

The current gemmapy/sdk was generated with swagger Codegen 3.0.31 and openapi.yaml (of 2022-06-23), templ/ 
presented in here. 
