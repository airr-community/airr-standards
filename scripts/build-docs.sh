#! /usr/bin/env bash

for YAML_FILE in specs/*.yaml; do
    NAME=$(basename $YAML_FILE .yaml)
    echo Rendering $NAME spec
    cat $YAML_FILE | jinja2 specs/$NAME.j2 > docs/$NAME.md
done
