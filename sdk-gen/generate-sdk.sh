#!/bin/bash
set -e
swagger_version=3.0.55
temp_sdk_dir=$(mktemp -d)
script_dir=$(dirname "${BASH_SOURCE[0]}")
gemmapy_version=$(grep 'version' "$script_dir/../setup.cfg" | sed 's/version = //')
echo "Updating openapi.yaml..."
curl https://staging-gemma.msl.ubc.ca/rest/v2/openapi.yaml -o "$script_dir/openapi.yaml" --compressed
echo "Updating swagger-codegen-cli.jar..."
curl "https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/$swagger_version/swagger-codegen-cli-$swagger_version.jar" -o swagger-codegen-cli.jar

echo "SDK will be generated in $temp_sdk_dir..."
java -jar swagger-codegen-cli.jar generate -i "$script_dir/openapi.yaml" -l python -t "$script_dir/templ" -DpackageName=gemmapy.sdk -o "$temp_sdk_dir" --http-user-agent "gemmapy/$gemmapy_version"
rsync -av --delete "$temp_sdk_dir/gemmapy/sdk/" "$script_dir/../gemmapy/sdk/"

