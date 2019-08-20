#!/usr/bin/env python3

import csv
import pandas as pd
import sys
import yaml
from collections import Counter
#from deepdiff import DeepDiff

miairr_dataset_to_api_object = {
    '1 / study': 'Study',
    '1 / subject': 'Subject',
    '1 / diag. & intervent.': 'Diagnosis',
    '2 / sample': 'Sample',
    '3 / process (cell)': 'CellProcessing',
    '3 / process (nucl. acid)': 'NucleicAcidProcessing',
    '3 / process (nucl. acid [pcr])': 'PCRTarget',
    '3 / process (sequencing)': 'SequencingRun',
    '5 / process (comput.)': 'SoftwareProcessing',
    '6 / data (proc. seq.)': 'Rearrangement'}

#
# The MiAIRR TSV is going to be generated directly from the schema, making
# most of these checks invalid. This script should be deprecated or reworked
# with other checks.
#

print('Skipping MiAIRR consistency checks')
sys.exit(0)

with open('AIRR_Minimal_Standard_Data_Elements.tsv', 'r') as ip:
    tsv_data = list(csv.DictReader(ip, dialect='excel-tab'))


with open('specs/airr-schema.yaml', 'r') as ip:
    yaml_data = yaml.load(ip)


failed = False


# check for uniqueness of fields in AIRR_Minimal_Standard_Data_Elements.tsv
fields = [e['AIRR Formats WG field name'] for e in tsv_data]
if len(fields) != len(set(fields)):
    print('Duplicate entries found in AIRR_Minimal_Standard_Data_Elements.tsv', file=sys.stderr)
    for k, v in Counter(fields).items():
        if v > 1:
            print(f'{k:30} found {v} times in tsv when it should be unique\n', file=sys.stderr)
    failed = True


# check for differences in fields between specs/airr-schema.yaml and
# AIRR_Minimal_Standard_Data_Elements.tsv
for dataset in miairr_dataset_to_api_object.keys():
    api_object = miairr_dataset_to_api_object[dataset]
    tsv_fields = [row['AIRR Formats WG field name']
                  for row in tsv_data
                  if row['MiAIRR data set / subset'] == dataset]
    yaml_object = yaml_data.get(api_object, None)
    if not yaml_object:
        print(f'{api_object} not found in airr-schema.yaml.\n', file=sys.stderr)
        failed = True
        continue
    yaml_fields = [property for property in yaml_object['properties'] if yaml_object['properties'][property].get('x-miairr')]
    if set(tsv_fields) != set(yaml_fields):
        print(f'yaml {api_object} does not match tsv {dataset}', file=sys.stderr)
        for field in set(yaml_fields) - set(tsv_fields):
            print(f'{field:30} is found in yaml {api_object} but not tsv {dataset}', file=sys.stderr)
        for field in set(tsv_fields) - set(yaml_fields):
            print(f'{field:30} is found in tsv {dataset} but not yaml {api_object}', file=sys.stderr)
        failed = True


# check that MiAIRR object definitions contained
# within AIRR definition
#for miairr_api_object in yaml_data.keys():
#    if yaml_data[miairr_api_object]['discriminator'] == 'MiAIRR':
#        airr_api_object = miairr_api_object.split('_')[1]
#        if airr_api_object not in yaml_data:
#            print(f'{airr_api_object} corresponding to {miairr_api_object} not found in airr-schema.yaml', file=sys.stderr)
#            failed = True
#            continue

#        for miairr_field in yaml_data[miairr_api_object]['properties']:
#            if miairr_field not in yaml_data[airr_api_object]['properties']:
#                print(f'{miairr_field} in {miairr_api_object} object is not in {airr_api_object} object.', file=sys.stderr)
#                failed = True
#                continue
#            ddiff = DeepDiff(yaml_data[miairr_api_object]['properties'][miairr_field], yaml_data[airr_api_object]['properties'][miairr_field], ignore_order=True)
#            if ddiff:
#                print(f'{miairr_field} in {miairr_api_object} object is not the same object in {airr_api_object}.', file=sys.stderr)
#                print(ddiff, file=sys.stderr)
#                failed = True


# check consistency with NCBI XML definitions, per @BusseChristian's pseudocode
# in https://github.com/airr-community/airr-standards/issues/20
with open('NCBI_implementation/mapping_MiAIRR_BioSample.tsv', 'r') as ip:
    miairr_to_ncbi = {r['AIRR Formats WG field name']: r['NCBI BioSample attribute']
                      for r in csv.DictReader(ip, dialect='excel-tab')}
miairr_biosample_identifiers = [r['AIRR Formats WG field name']
                                for r in tsv_data
                                if r['MiAIRR data set / subset'] in ["1 / subject", "1 / diag. & intervent.", "2 / sample", "3 / process (cell)"]]
miairr_biosample_identifiers.append('study_id') # manually add
mapped_identifiers = {miairr_to_ncbi.get(name, name)
                      for name in miairr_biosample_identifiers}
ncbi_biosample_template = pd.read_excel('NCBI_implementation/templates_XLS/AIRR_BioSample_v1.0.xls', skiprows=13)
ncbi_identifiers = set([x.lstrip('*') for x in ncbi_biosample_template.columns])
if mapped_identifiers != ncbi_identifiers:
    print('AIRR_Minimal_Standard_Data_Elements.tsv does not match AIRR_BioSample_v1.0.xls', file=sys.stderr)
    for field in set(mapped_identifiers) - set(ncbi_identifiers):
        print(f'{field:30} is found in MiAIRR table tsv but not in NCBI Biosample template xls', file=sys.stderr)
    for field in set(ncbi_identifiers) - set(mapped_identifiers):
        print(f'{field:30} is found in NCBI Biosample template xls but not in MiAIRR table tsv', file=sys.stderr)
    failed = True


if failed:
    print('consistency checks failed', file=sys.stderr)
    sys.exit(1)
