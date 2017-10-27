#! /usr/bin/env python

import sys
from collections import Counter

import yaml
import csv
from deepdiff import DeepDiff

object_map = { '1 / study': 'MiAIRR_Study',
               '1 / subject': 'MiAIRR_Subject',
               '1 / diag. & intervent.': 'MiAIRR_Diagnosis',
               '2 / sample': 'MiAIRR_Sample',
               '3 / process (cell)': 'MiAIRR_CellProcessing',
               '3 / process (nucl. acid)': 'MiAIRR_NucleicAcidProcessing',
               '5 / process (comput.)': 'MiAIRR_SoftwareProcessing',
               '6 / data (proc. seq.)': 'MiAIRR_Rearrangement' }

with open('AIRR_Minimal_Standard_Data_Elements.tsv', 'r') as ip:
    dictReader = csv.DictReader(ip, dialect='excel-tab')
    miairr_elements = [line for line in dictReader]

with open('AIRR_Minimal_Standard_Data_Elements.tsv', 'r') as ip:
    # header line present
    assert next(ip).split()[0] == 'MiAIRR'

    table = [line.split('\t')[6].strip() for line in ip]
    # handle the exceptional 4 / data line
    assert table.count('') == 1
    _ = table.pop(table.index(''))

with open('specs/definitions.yaml', 'r') as ip:
    definitions = yaml.load(ip)
    properties = [property
                  for obj in definitions.values()
                  for property in obj['properties']
                  if obj.get('discriminator') == 'MiAIRR']

failed = False

# check for uniqueness of fields in AIRR_Minimal_Standard_Data_Elements.tsv
if len(table) != len(set(table)):
    for k, v in Counter(table).items():
        if v > 1:
            print(f'{k:30} found {v} times in tsv when it should be unique\n', file=sys.stderr)
    failed = True

# check for differences in fields between specs/definitions.yaml and
# AIRR_Minimal_Standard_Data_Elements.tsv
for key in object_map.keys():
    elements = [element['AIRR Formats WG field name'] for element in miairr_elements
                if element['MiAIRR data set / subset'] == key]
    definition = definitions.get(object_map[key])
    if not definition:
        print(f'{object_map[key]} not found in definitions.yaml.\n', file=sys.stderr)
        failed = True
        continue

    properties = [property for property in definition['properties']]
    if set(elements) != set(properties):
        for field in set(properties) - set(elements):
            print(f'{field:30} is found in yaml but not tsv for {object_map[key]}', file=sys.stderr)
        for field in set(elements) - set(properties):
            print(f'{field:30} is found in tsv but not yaml for {object_map[key]}', file=sys.stderr)
        failed = True

# check that MiAIRR object definitions contained
# within AIRR definition
for definition in definitions.keys():
    if definitions[definition].get('discriminator') == 'MiAIRR':
        name = definition.split('_')[1]
        if not definitions.get(name):
            print(f'{name} corresponding to {definition} not found in definitions.yaml', file=sys.stderr)
            failed = True
            continue

        for prop in definitions[definition]['properties']:
            if not definitions[name]['properties'].get(prop):
                print(f'{prop} in {definition} object is not in {name} object.', file=sys.stderr)
                failed = True
                continue
            ddiff = DeepDiff(definitions[definition]['properties'][prop], definitions[name]['properties'][prop], ignore_order=True)
            if ddiff:
                print(f'{prop} in {definition} object is not the same object in {name}.', file=sys.stderr)
                print(ddiff, file=sys.stderr)
                failed = True

# check consistency with NCBI XML definitions, per @BusseChristian's pseudocode
# in https://github.com/airr-community/airr-standards/issues/20
import pandas as pd

miairr_table = pd.read_csv('AIRR_Minimal_Standard_Data_Elements.tsv', sep='\t', header=0, index_col=None)
miairr_biosample_rows = miairr_table.iloc[:, 0].isin(["1 / subject", "1 / diag. & intervent.", "2 / sample", "3 / process (cell)"])
miairr_identifiers = set(miairr_table[miairr_biosample_rows].iloc[:, 6])

ncbi_biosample = pd.read_excel('NCBI_implementation/templates_XLS/AIRR_BioSample_v1.0.xls', skiprows=13)
ncbi_identifiers = set([x.lstrip('*') for x in ncbi_biosample.columns])

if miairr_identifiers != ncbi_identifiers:
    for field in set(miairr_identifiers) - set(ncbi_identifiers):
        print(f'{field:30} is found in MiAIRR table tsv but not in NCBI Biosample template xls', file=sys.stderr)
    for field in set(ncbi_identifiers) - set(miairr_identifiers):
        print(f'{field:30} is found in NCBI Biosample template xls but not in MiAIRR table tsv', file=sys.stderr)
    failed = True

if failed: sys.exit(1)
