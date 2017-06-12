#! /usr/bin/env bash

# get dir of this script: http://stackoverflow.com/questions/59895
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cp $DIR/../../../specs/*.yaml $DIR/../airr/specs
