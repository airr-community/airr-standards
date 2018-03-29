import airr

# read a rearrangments file
print('*****')
print('*****')
print('Read a rearrangements file.')
print('*****')
print('*****')
data = airr.read(open('toy_data.tsv', 'r'))
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
data = airr.read(open('toy_data.tsv', 'r'))
newd = airr.create(open('my_data.tsv', 'w'), fields=data.fields)
print(newd.fields)
print(newd.external_fields)
for r in data:  newd.write(r)
newd.close()

data = airr.read(open('my_data.tsv', 'r'))
print(data.fields)
print(data.external_fields)
for r in data:  print(r)

# create a derived rearrangements file with additional annotation
print('*****')
print('*****')
print('Derive rearrangements file from another.')
print('*****')
print('*****')
mored = airr.derive(open('more_data.tsv', 'w'), open('my_data.tsv', 'r'),
                    fields=['new_field', 'more_annotation'])
print(mored.fields)
print(mored.external_fields)
for r in airr.read(open('my_data.tsv', 'r')):
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
valid = airr.validate(['more_data.tsv'])
if valid:
    print('more_data.tsv passes validation.')
else:
    print('ERROR: more_data.tsv does not pass validation.')
