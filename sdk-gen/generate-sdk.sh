#!/bin/bash
set -e
swagger_version=3.0.73
temp_sdk_dir=$(mktemp -d)
script_dir=$(dirname "${BASH_SOURCE[0]}")
gemmapy_version=$(grep 'version' "$script_dir/../pyproject.toml" | sed 's/version = //')
echo "Updating openapi.yaml..."
curl https://gemma.msl.ubc.ca/rest/v2/openapi.yaml -o "$script_dir/openapi.yaml" --compressed
# swagger-codegen v3 cannot generate usable Python for the response-level oneOf
# schemas the spec uses for cursor pagination, so codegen runs against a patched
# copy. openapi.yaml itself stays as downloaded; changes are listed in
# openapi-patches.md.
echo "Patching openapi.yaml for code generation..."
python "$script_dir/patch-openapi.py" "$script_dir/openapi.yaml" "$temp_sdk_dir/openapi.patched.yaml" "$script_dir/openapi-patches.md"

echo "Downloading swagger-codegen-cli.jar..."
curl "https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/$swagger_version/swagger-codegen-cli-$swagger_version.jar" -o "$temp_sdk_dir/swagger-codegen-cli.jar"

echo "SDK will be generated in $temp_sdk_dir..."
java -jar "$temp_sdk_dir/swagger-codegen-cli.jar" generate -i "$temp_sdk_dir/openapi.patched.yaml" -l python -t "$script_dir/templ" -DpackageName=gemmapy.sdk -o "$temp_sdk_dir" --http-user-agent "gemmapy/$gemmapy_version"
rsync -av --delete "$temp_sdk_dir/gemmapy/sdk/" "$script_dir/../gemmapy/sdk/"
rm -rf "$temp_sdk_dir"
