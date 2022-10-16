#!/bin/sh
temp_sdk_dir=$(mktemp -d)
echo "SDK will be generated in $temp_sdk_dir..."
java -jar swagger-codegen-cli.jar generate -i openapi.yaml -l python -t templ -DpackageName=gemmapy.sdk -o "$temp_sdk_dir"
rsync -av --delete "$temp_sdk_dir/gemmapy/sdk/" ../gemmapy/sdk/
