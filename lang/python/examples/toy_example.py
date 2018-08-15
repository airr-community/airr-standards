#!/usr/bin/env python3

# imports
import airr

# read a rearrangments file
print('*****')
print('*****')
print('Read a rearrangements file.')
print('*****')
print('*****')
data = airr.read_rearrangement('toy_data.tsv')
print(data.fields)
print(data.external_fields)
for r in data:  print(r)

# Create a new rearrangements file with an intermediate parser
# Technically, the parser tool should be reading the VDJ rearrangements
# output file, parsing it, then writing the row data.
print('*****')
print('*****')
print('Create new rearrangements file.')
print('*****')
print('*****')
data = airr.read_rearrangement('toy_data.tsv')
newd = airr.create_rearrangement('my_data.tsv', fields=data.fields)
print(newd.fields)
print(newd.external_fields)
for r in data:  newd.write(r)
newd.close()

data = airr.read_rearrangement('my_data.tsv')
print(data.fields)
print(data.external_fields)
for r in data:  print(r)

# create a derived rearrangements file with additional annotation
print('*****')
print('*****')
print('Derive rearrangements file from another.')
print('*****')
print('*****')
mored = airr.derive_rearrangement('more_data.tsv', 'my_data.tsv',
                    fields=['new_field', 'more_annotation'])
print(mored.fields)
print(mored.external_fields)
for r in airr.read_rearrangement('my_data.tsv'):
    r['new_field'] = 'A'
    r['more_annotation'] = 'B'
    print(r)
    mored.write(r)
mored.close()

# validate rearrangements file
print('*****')
print('*****')
print('Validate rearrangements file.')
print('*****')
print('*****')
print('Validating more_data.tsv')
valid = airr.validate_rearrangement('more_data.tsv')
if valid:
    print('PASS: more_data.tsv passes validation.')
else:
    print('FAIL: more_data.tsv does not pass validation.')

# should fail validation due to missing required field
print('Validating bad_data.tsv')
valid = airr.validate_rearrangement('bad_data.tsv')
if not valid:
    print('PASS: bad_data.tsv fails validation.')
else:
    print('FAIL: bad_data.tsv passed validation.')

# merge rearrangements file
print('*****')
print('*****')
print('Merge rearrangements files.')
print('*****')
print('*****')
valid = airr.merge_rearrangement('merged.tsv', ['toy_data.tsv', 'toy_data.tsv'])
if valid:
    print('PASS: files were merged.')
else:
    print('FAIL: files were not merged.')

# passes validation even though duplicate sequence_ids
valid = airr.validate_rearrangement('merged.tsv')
if not valid:
    print('FAIL: merged.tsv fails validation.')
else:
    print('PASS: merged.tsv passed validation.')
