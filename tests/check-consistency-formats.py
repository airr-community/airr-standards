#!/usr/bin/env python3

# Imports
import filecmp
import os
import sys
import yaml
from glob import glob

# function to extract name from file
basename = lambda f: os.path.splitext(os.path.basename(f))[0]

# load all paths keyed by their name
test_files = {**{"python": {basename(f): f for f in glob('lang/python/tests/data/*')}},
              **{"R": {basename(f): f for f in glob('lang/R/tests/data-tests/*')}}}
spec_files = {**{"spec": {basename(f): f for f in glob('specs/airr-schema.yaml')}},
              **{"python": {basename(f): f for f in glob('lang/python/airr/specs/airr-schema.yaml')}},
              **{"R": {basename(f): f for f in glob('lang/R/inst/extdata/airr-schema.yaml')}}
              }


def check_file_sync(dic_files: dict, files_key_a: str, files_key_b: str):
    # Check python package specs
    if set(dic_files[files_key_a].keys()) != set(dic_files[files_key_b].keys()):
        for spec in set(dic_files[files_key_a].keys()) - set(dic_files[files_key_b].keys()):
            print('{} missing from {} package'.format(spec, files_key_b, file=sys.stderr))
        for spec in set(dic_files[files_key_b].keys()) - set(dic_files[files_key_a].keys()):
            print('{} found in {} package but missing from {}/'.format(spec, files_key_b, files_key_a), file=sys.stderr)
        sys.exit(1)


# Check python package specs
check_file_sync(spec_files, "spec", "python")
# Check R package specs
check_file_sync(spec_files, "spec", "R")
# Check R vs python package test files
check_file_sync(test_files, "R", "python")

# check equality of specs
for spec_name in spec_files["spec"]:

    if not filecmp.cmp(spec_files["spec"][spec_name], spec_files["python"][spec_name]):
        print('{} spec is different from python version'.format(spec_name), file=sys.stderr)
        sys.exit(1)
    if not filecmp.cmp(spec_files["spec"][spec_name], spec_files["R"][spec_name]):
        print('{} spec is different from R version'.format(spec_name), file=sys.stderr)
        sys.exit(1)

# check equality of test files
for file_name in test_files["R"]:

    if not filecmp.cmp(test_files["R"][file_name], test_files["python"][file_name]):
        print('R {} test file is different from python version'.format(file_name), file=sys.stderr)
        sys.exit(1)

