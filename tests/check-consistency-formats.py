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
spec_files = {basename(f): f for f in glob('specs/airr-schema.yaml')}
v3spec_files = {basename(f): f for f in glob('specs/airr-schema-openapi3.yaml')}
py_files = {basename(f): f for f in glob('lang/python/airr/specs/airr-schema.yaml')}
py_v3_files = {basename(f): f for f in glob('lang/python/airr/specs/airr-schema-openapi3.yaml')}
r_files = {basename(f): f for f in glob('lang/R/inst/extdata/airr-schema.yaml')}
r_v3_files = {basename(f): f for f in glob('lang/R/inst/extdata/airr-schema-openapi3.yaml')}

# Check python package specs
if set(spec_files.keys()) != set(py_files.keys()):
    for spec in set(spec_files.keys()) - set(py_files.keys()):
        print('{} missing from python package'.format(spec), file=sys.stderr)
    for spec in set(py_files.keys()) - set(spec_files.keys()):
        print('{} found in python package but missing from specs/'.format(spec), file=sys.stderr)
    sys.exit(1)
if set(v3spec_files.keys()) != set(py_v3_files.keys()):
    for spec in set(v3spec_files.keys()) - set(py_v3_files.keys()):
        print('{} missing from python package'.format(spec), file=sys.stderr)
    for spec in set(py_v3_files.keys()) - set(v3spec_files.keys()):
        print('{} found in python package but missing from specs/'.format(spec), file=sys.stderr)
    sys.exit(1)

# Check R package specs
if set(spec_files.keys()) != set(r_files.keys()):
    for spec in set(spec_files.keys()) - set(r_files.keys()):
        print('{} missing from R package'.format(spec), file=sys.stderr)
    for spec in set(r_files.keys()) - set(spec_files.keys()):
        print('{} found in R package but missing from specs/'.format(spec), file=sys.stderr)
    sys.exit(1)
if set(v3spec_files.keys()) != set(r_v3_files.keys()):
    for spec in set(v3spec_files.keys()) - set(r_v3_files.keys()):
        print('{} missing from R package'.format(spec), file=sys.stderr)
    for spec in set(r_v3_files.keys()) - set(v3spec_files.keys()):
        print('{} found in R package but missing from specs/'.format(spec), file=sys.stderr)
    sys.exit(1)

# V3 spec against lang
for spec_name in v3spec_files:
    # check equality of specs
    with open(v3spec_files[spec_name], 'r') as ip:
        gold_spec = yaml.safe_load(ip)
    with open(py_v3_files[spec_name], 'r') as ip:
        py_spec = yaml.safe_load(ip)
    with open(r_v3_files[spec_name], 'r') as ip:
        r_spec = yaml.safe_load(ip)

    # Check python package
    if jsondiff.diff(gold_spec, py_spec) != {}:
        print('{} openapi v3 spec is different from python version'.format(spec_name), file=sys.stderr)
        print(jsondiff.diff(gold_spec, py_spec, syntax='explicit'), file=sys.stderr)
        sys.exit(1)

    # Check R package
    if jsondiff.diff(gold_spec, r_spec) != {}:
        print('{} openapi v3 spec is different from R version'.format(spec_name), file=sys.stderr)
        print(jsondiff.diff(gold_spec, r_spec), file=sys.stderr)
        sys.exit(1)

# V2 spec against lang
for spec_name in spec_files:
    # check equality of specs
    with open(spec_files[spec_name], 'r') as ip:
        gold_spec = yaml.safe_load(ip)
    with open(py_files[spec_name], 'r') as ip:
        py_spec = yaml.safe_load(ip)
    with open(r_files[spec_name], 'r') as ip:
        r_spec = yaml.safe_load(ip)

    # Check python package
    if jsondiff.diff(gold_spec, py_spec) != {}:
        print('{} openapi v2 spec is different from python version'.format(spec_name), file=sys.stderr)
        print(jsondiff.diff(gold_spec, py_spec, syntax='explicit'), file=sys.stderr)
        sys.exit(1)

    # Check R package
    if jsondiff.diff(gold_spec, r_spec) != {}:
        print('{} openapi v2 spec is different from R version'.format(spec_name), file=sys.stderr)
        print(jsondiff.diff(gold_spec, r_spec), file=sys.stderr)
        sys.exit(1)

# Check OpenAPI3 spec vs OpenAPI2
for spec_name in spec_files:
    with open(spec_files[spec_name], 'r') as ip:
        v2_spec = yaml.safe_load(ip)

for spec_name in v3spec_files:
    with open(v3spec_files[spec_name], 'r') as ip:
        v3_spec = yaml.safe_load(ip)

def translate_nullable(obj):
    for prop in obj['properties']:
        p = obj['properties'][prop]
        if p.get('x-airr') is not None:
            if p['x-airr'].get('nullable') is not None:
                p['nullable'] = p['x-airr']['nullable']
                del p['x-airr']['nullable']
            if p['x-airr'] == {}:
                del p['x-airr']
        if p.get('nullable') is None:
            p['nullable'] = True

def check_miairr_essential(obj, is_v3):
    for prop in obj['properties']:
        p = obj['properties'][prop]
        if p.get('x-airr') is not None:
            if p['x-airr'].get('miairr') == 'essential':
                if is_v3:
                    # for V3, default is nullable: false
                    if p.get('nullable'):
                        print(prop, ' in {} object in V3 spec is inconsistent with miairr:essential and nullable:true'.format(obj), file=sys.stderr)
                        return True
                else:
                    # for V2, default is nullable: true
                    if p['x-airr'].get('nullable') or p['x-airr'].get('nullable', 'missing') == 'missing':
                        print(prop, 'in {} object in V2 spec is inconsistent with miairr:essential and nullable:true'.format(obj), file=sys.stderr)
                        return True
    return False

found_miairr_inconsistency = False

# Make V2 look like V3 then compare
for obj in v2_spec:
    # print(obj)
    # print(v2_spec[obj])
    # print(v3_spec[obj])

    # singleton object, not a schema
    if obj == 'CURIEMap':
        if jsondiff.diff(v2_spec[obj], v3_spec[obj]) != {}:
            print('{} object in V2 spec is different from V3 spec'.format(obj), file=sys.stderr)
            print(jsondiff.diff(v2_spec[obj], v3_spec[obj]), file=sys.stderr)
            sys.exit(1)
        continue

    # singleton object, not a schema
    if obj == 'InformationProvider':
        if jsondiff.diff(v2_spec[obj], v3_spec[obj]) != {}:
            print('{} object in V2 spec is different from V3 spec'.format(obj), file=sys.stderr)
            print(jsondiff.diff(v2_spec[obj], v3_spec[obj]), file=sys.stderr)
            sys.exit(1)
        continue

    # AIRR attributes are different between versions
    if obj == 'Attributes':
        continue

    # discriminator is an object vs string
    if v2_spec[obj].get('discriminator') is not None:
        v2_spec[obj]['discriminator'] = { "propertyName": v2_spec[obj]['discriminator'] }

    # nullable and miairr flags
    if v2_spec[obj].get('properties') is not None:
        if check_miairr_essential(v2_spec[obj], False):
            found_miairr_inconsistency = True
        translate_nullable(v2_spec[obj])
        # look for sub-object
        for prop in v2_spec[obj]['properties']:
            if v2_spec[obj]['properties'][prop].get('properties') is not None:
                if check_miairr_essential(v2_spec[obj]['properties'][prop], False):
                    found_miairr_inconsistency = True
                translate_nullable(v2_spec[obj]['properties'][prop])
            # look for array of objects
            if v2_spec[obj]['properties'][prop].get('items') is not None:
                if v2_spec[obj]['properties'][prop]['items'].get('properties') is not None:
                    if check_miairr_essential(v2_spec[obj]['properties'][prop]['items'], False):
                        found_miairr_inconsistency = True
                    translate_nullable(v2_spec[obj]['properties'][prop]['items'])
    elif 'allOf' in v2_spec[obj]:
        if check_miairr_essential(v2_spec[obj]['allOf'][0], False):
            found_miairr_inconsistency = True
        translate_nullable(v2_spec[obj]['allOf'][0])

    # print(v2_spec[obj])
    # print(v3_spec[obj])
    if jsondiff.diff(v2_spec[obj], v3_spec[obj]) != {}:
        print('{} object is different between V2 and V3 spec'.format(obj), file=sys.stderr)
        print(jsondiff.diff(v2_spec[obj], v3_spec[obj]), file=sys.stderr)
        sys.exit(1)

# Make V3 look like V2 then compare
for obj in v3_spec:
    # nullable and miairr flags
    if v3_spec[obj].get('properties') is not None:
        #translate_nullable(v3_spec[obj])
        if check_miairr_essential(v3_spec[obj], True):
            found_miairr_inconsistency = True
        # look for sub-object
        for prop in v3_spec[obj]['properties']:
            if v3_spec[obj]['properties'][prop].get('properties') is not None:
                #translate_nullable(v3_spec[obj]['properties'][prop])
                if check_miairr_essential(v3_spec[obj]['properties'][prop], True):
                    found_miairr_inconsistency = True
            # look for array of objects
            if v3_spec[obj]['properties'][prop].get('items') is not None:
                if v3_spec[obj]['properties'][prop]['items'].get('properties') is not None:
                    #translate_nullable(v3_spec[obj]['properties'][prop]['items'])
                    if check_miairr_essential(v3_spec[obj]['properties'][prop]['items'], True):
                        found_miairr_inconsistency = True
    elif 'allOf' in v3_spec[obj]:
        #translate_nullable(v3_spec[obj]['allOf'][0])
        if check_miairr_essential(v3_spec[obj]['allOf'][0], True):
            found_miairr_inconsistency = True

if found_miairr_inconsistency:
    sys.exit(1)

