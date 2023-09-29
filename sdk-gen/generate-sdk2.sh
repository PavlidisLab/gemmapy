#!/bin/sh
# temp_sdk_dir=$(mktemp -d)
curl https://gemma.msl.ubc.ca/rest/v2/openapi.yaml -o openapi.yaml --compressed

curl https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh -o openapi-generator-cli.sh

chmod u+x openapi-generator-cli.sh


# echo "SDK will be generated in $temp_sdk_dir..."



./openapi-generator-cli.sh generate -i openapi.yaml  -g python -o tmp --additional-properties=packageVersion=0.99.0,packageName=gemmapy.sdk2 --skip-validate-spec

rsync -av --delete "tmp/gemmapy/sdk2/" ../gemmapy/sdk2/
