#!/bin/sh
temp_sdk_dir=$(mktemp -d)
script_dir=$(dirname "${BASH_SOURCE[0]}")
curl https://gemma.msl.ubc.ca/rest/v2/openapi.yaml -o openapi.yaml --compressed
curl https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.35/swagger-codegen-cli-3.0.35.jar -o swagger-codegen-cli.jar

echo "SDK will be generated in $temp_sdk_dir..."
java -jar swagger-codegen-cli.jar generate -i "$script_dir/openapi.yaml" -l python -t "$script_dir/templ" -DpackageName=gemmapy.sdk -o "$temp_sdk_dir" --http-user-agent gemmapy/0.0.2
rsync -av --delete "$temp_sdk_dir/gemmapy/sdk/" "$script_dir/../gemmapy/sdk/"
