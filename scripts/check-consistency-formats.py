#! /usr/bin/env python3

import sys
from glob import glob
import os.path as osp

import yaml
import jinja2
import jsondiff
import difflib

# function to extract name from file
basename = lambda f: osp.splitext(osp.basename(f))[0]


# load all paths keyed by their name
spec_files = {basename(f): f for f in glob('specs/*.yaml')}
jinja_templates = {basename(f): f for f in glob('specs/*.j2')}
py_files = {basename(f): f for f in glob('lang/python/airr/specs/*.yaml')}
doc_files = {basename(f): f for f in glob('docs/*.md')}


if set(spec_files.keys()) != set(py_files.keys()):
    for spec in set(spec_files.keys()) - set(py_files.keys()):
        print('{} missing from python package'.format(spec), file=sys.stderr)
    for spec in set(py_files.keys()) - set(spec_files.keys()):
        print('{} found in python package but missing from specs/'.format(spec), file=sys.stderr)
    sys.exit(1)


if len(set(spec_files.keys()) - set(doc_files.keys())) > 0:
    for spec in set(spec_files.keys()) - set(doc_files.keys()):
        print('{} missing from rendered doc files'.format(spec), file=sys.stderr)
    sys.exit(1)


for spec_name in spec_files:
    # check equality of specs
    with open(spec_files[spec_name], 'r') as ip:
        gold_spec = yaml.load(ip)
    with open(py_files[spec_name], 'r') as ip:
        py_spec = yaml.load(ip)

    if jsondiff.diff(gold_spec, py_spec) != {}:
        print('{} spec is different from python version'.format(spec_name), file=sys.stderr)
        print(jsondiff.diff(gold_spec, py_spec), file=sys.stderr)
        sys.exit(1)

    # check that docs have been rendered
    with open(jinja_templates[spec_name], 'r') as ip:
        template = jinja2.Template(ip.read().strip())
    with open(doc_files[spec_name], 'r') as ip:
        doc_contents = ip.read().strip()

    if template.render(gold_spec) != doc_contents:
        doc_lines = doc_contents.splitlines()
        gold_lines = template.render(gold_spec).splitlines()
        diff = difflib.unified_diff(doc_lines, gold_lines)
        print('rendered doc for {} does not correspond to spec'.format(spec_name))
        print('\n'.join(diff))
        sys.exit(1)
