import airr

# read a rearrangments file
print('*****')
print('*****')
print('Read a rearrangements file.')
print('*****')
print('*****')
data = airr.read(open('toy_data.tsv', 'r'))
#print (data.additionalFieldNames)
for r in data:
    print(r)
data.close()

# Create a new rearrangements file with an intermediate parser
# Technically, the parser tool should be reading the VDJ rearrangements
# output file, parsing it, then writing the row data.
print('*****')
print('*****')
print('Create new rearrangements file.')
print('*****')
print('*****')
newd = airr.create(open('my_data.tsv', 'w'))
newd.addRearrangementActivityWithParser('seq.fasta', 'VDJServer GLDB 10_05_2016', 'my_data.tsv', 'IgBlast', 'alignment', 'changeo', 'seq.igblast.out', 'MakeDb')
data = airr.read(open('toy_data.tsv', 'r'))
#print(data.additionalFieldNames)
newd.addFields('my_parser', data.additionalFieldNames)
#print(newd.additionalFieldNames)
for r in data:
    #print(r)
    newd.write(r)
newd.close()

data = airr.read(open('my_data.tsv', 'r'))
#print (data.additionalFieldNames)
#print (data._inputFieldNames)
for r in data:
    print(r)
data.close()

# create a derived rearrangements file with additional annotation
print('*****')
print('*****')
print('Derive rearrangements file from another.')
print('*****')
print('*****')
mored = airr.createDerivation(open('my_data.tsv', 'r'), open('more_data.tsv', 'w'), 'myTool', 'my special analysis', 'mytool', 'http://mytool.org')
mored[1].addFields('mytool', ['new_field', 'more_annotation'])
#print(mored[1].additionalFieldNames)
#print(mored[0]._inputFieldNames)
for r in mored[0]:
    #print(r)
    r['new_field'] = 'A'
    r['more_annotation'] = 'B'
    #print(r)
    mored[1].write(r)
mored[0].close()
mored[1].close()
