#! /usr/bin/env python

from glob import glob
import os.path as osp

import yaml
import jinja2


# function to extract name from file
basename = lambda f: osp.splitext(osp.basename(f))[0]


# load all paths keyed by their name
spec_files = {basename(f): f for f in glob('specs/*.yaml')}
jinja_templates = {basename(f): f for f in glob('specs/*.j2')}
py_files = {basename(f): f for f in glob('lang/python/airr/specs/*.yaml')}
doc_files = {basename(f): f for f in glob('docs/*.md')}


assert set(spec_files.keys()) == set(py_files.keys())
assert len(set(spec_files.keys()) - set(doc_files.keys())) == 0


for spec_name in spec_files:
    # check equality of specs
    with open(spec_files[spec_name], 'r') as ip:
        gold_spec = yaml.load(ip)
    with open(py_files[spec_name], 'r') as ip:
        py_spec = yaml.load(ip)

    assert gold_spec == py_spec

    # check that docs have been rendered
    with open(jinja_templates[spec_name], 'r') as ip:
        template = jinja2.Template(ip.read().strip())
    with open(doc_files[spec_name], 'r') as ip:
        doc_contents = ip.read().strip()

    assert template.render(gold_spec) == doc_contents
