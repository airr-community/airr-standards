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
        print(f'{field:30} is found in yaml but not tsv', file=sys.stderr)
    for field in set(table) - set(properties):
        print(f'{field:30} is found in tsv but not yaml', file=sys.stderr)
    sys.exit(1)


# check consistency with NCBI XML definitions, per @BusseChristian's pseudocode
# in https://github.com/airr-community/airr-standards/issues/20
import pandas as pd

miairr_table = pd.read_csv('AIRR_Minimal_Standard_Data_Elements.tsv', sep='\t', header=0, index_col=None)
miairr_biosample_rows = miairr_table.iloc[:, 0].isin(["1 / subject", "1 / diag. & intervent.", "2 / sample", "3 / process (cell)"])
miairr_identifiers = set(miairr_table[miairr_biosample_rows].iloc[:, 5])

ncbi_biosample = pd.read_excel('NCBI_implementation/templates_XLS/AIRR_BioSample_v1.0.xls', skiprows=13)
ncbi_identifiers = set([x.lstrip('*') for x in ncbi_biosample.columns])

if miairr_identifiers != ncbi_identifiers:
    for field in set(miairr_identifiers) - set(ncbi_identifiers):
        print(f'{field:30} is found in MiAIRR table tsv but not in NCBI Biosample template xls', file=sys.stderr)
    for field in set(ncbi_identifiers) - set(miairr_identifiers):
        print(f'{field:30} is found in NCBI Biosample template xls but not in MiAIRR table tsv', file=sys.stderr)
    sys.exit(1)
