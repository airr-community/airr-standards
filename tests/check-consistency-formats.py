#!/usr/bin/env python3

# Imports
import jsondiff
import os
import sys
import yaml
from glob import glob

# function to extract name from file
basename = lambda f: os.path.splitext(os.path.basename(f))[0]

# load all paths keyed by their name
#spec_files = {basename(f): f for f in glob('specs/*.yaml')}
#py_files = {basename(f): f for f in glob('lang/python/airr/specs/*.yaml')}
#r_files = {basename(f): f for f in glob('lang/R/inst/extdata/*.yaml')}
spec_files = {basename(f): f for f in glob('specs/definitions.yaml')}
py_files = {basename(f): f for f in glob('lang/python/airr/specs/definitions.yaml')}
r_files = {basename(f): f for f in glob('lang/R/inst/extdata/definitions.yaml')}

# Check python package specs
if set(spec_files.keys()) != set(py_files.keys()):
    for spec in set(spec_files.keys()) - set(py_files.keys()):
        print('{} missing from python package'.format(spec), file=sys.stderr)
    for spec in set(py_files.keys()) - set(spec_files.keys()):
        print('{} found in python package but missing from specs/'.format(spec), file=sys.stderr)
    sys.exit(1)

# Check R package specs
if set(spec_files.keys()) != set(r_files.keys()):
    for spec in set(spec_files.keys()) - set(r_files.keys()):
        print('{} missing from R package'.format(spec), file=sys.stderr)
    for spec in set(r_files.keys()) - set(spec_files.keys()):
        print('{} found in R package but missing from specs/'.format(spec), file=sys.stderr)
    sys.exit(1)

for spec_name in spec_files:
    # check equality of specs
    with open(spec_files[spec_name], 'r') as ip:
        gold_spec = yaml.load(ip)
    with open(py_files[spec_name], 'r') as ip:
        py_spec = yaml.load(ip)
    with open(r_files[spec_name], 'r') as ip:
        r_spec = yaml.load(ip)

    # Check python package
    if jsondiff.diff(gold_spec, py_spec) != {}:
        print('{} spec is different from python version'.format(spec_name), file=sys.stderr)
        print(jsondiff.diff(gold_spec, py_spec), file=sys.stderr)
        sys.exit(1)

    # Check R package
    if jsondiff.diff(gold_spec, r_spec) != {}:
        print('{} spec is different from R version'.format(spec_name), file=sys.stderr)
        print(jsondiff.diff(gold_spec, r_spec), file=sys.stderr)
        sys.exit(1)

