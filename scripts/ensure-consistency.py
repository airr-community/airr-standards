#! /usr/bin/env python

import sys
from collections import Counter

import yaml


with open('AIRR_Minimal_Standard_Data_Elements.tsv', 'r') as ip:
    # header line present
    assert next(ip).split()[0] == 'Collection'

    table = [line.split('\t')[5].strip() for line in ip]
    # handle the exceptional 4 / data line
    assert table.count('') == 1
    _ = table.pop(table.index(''))


with open('specs/definitions.yaml', 'r') as ip:
    definitions = yaml.load(ip)
    properties = [property
                  for obj in definitions.values()
                  for property in obj['properties']]


# check for uniqueness of fields in AIRR_Minimal_Standard_Data_Elements.tsv
if len(table) != len(set(table)):
    for k, v in Counter(table).items():
        if v > 1:
            print(f'{k:30} found {v} times in tsv when it should be unique\n', file=sys.stderr)
    sys.exit(1)


# check for differences in fields between specs/definitions.yaml and
# AIRR_Minimal_Standard_Data_Elements.tsv
if set(properties) != set(table):
    for field in set(properties) - set(table):
        print(f'{field:30} is found in yaml but not tsv\n', file=sys.stderr)
    for field in set(table) - set(properties):
        print(f'{field:30} is found in tsv but not yaml\n', file=sys.stderr)
    sys.exit(1)
