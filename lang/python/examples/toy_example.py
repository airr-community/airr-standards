import airr

# read a rearrangments file
print('*****')
print('*****')
print('Read a rearrangements file.')
print('*****')
print('*****')
data = airr.read_rearrangement(open('toy_data.tsv', 'r'))
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
data = airr.read_rearrangement(open('toy_data.tsv', 'r'))
newd = airr.create_rearrangement(open('my_data.tsv', 'w'), fields=data.fields)
print(newd.fields)
print(newd.external_fields)
for r in data:  newd.write(r)
newd.close()

data = airr.read_rearrangement(open('my_data.tsv', 'r'))
print(data.fields)
print(data.external_fields)
for r in data:  print(r)

# create a derived rearrangements file with additional annotation
print('*****')
print('*****')
print('Derive rearrangements file from another.')
print('*****')
print('*****')
mored = airr.derive_rearrangement(open('more_data.tsv', 'w'), open('my_data.tsv', 'r'),
                    fields=['new_field', 'more_annotation'])
print(mored.fields)
print(mored.external_fields)
for r in airr.read_rearrangement(open('my_data.tsv', 'r')):
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
valid = airr.validate_rearrangement([open('more_data.tsv', 'r')])
if valid:
    print('PASS: more_data.tsv passes validation.')
else:
    print('FAIL: more_data.tsv does not pass validation.')

# should fail validation due to missing required field
print('Validating bad_data.tsv')
valid = airr.validate_rearrangement([open('bad_data.tsv', 'r')])
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
valid = airr.merge_rearrangement(open('merged.tsv', 'w'), [open('toy_data.tsv', 'r'), open('toy_data.tsv', 'r')])
if valid:
    print('PASS: files were merged.')
else:
    print('FAIL: files were not merged.')

# should fail validation due to duplicate sequence_ids
valid = airr.validate_rearrangement([open('merged.tsv', 'r')])
if not valid:
    print('PASS: merged.tsv fails validation.')
else:
    print('FAIL: merged.tsv passed validation.')
