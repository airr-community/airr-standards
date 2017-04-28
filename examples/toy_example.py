import airr

# read a rearrangments file
data = airr.read('toy_data.tsv')
print (data.fieldNames)
for r in data:
    print(r)
data.close()

# Create a new rearrangements file with an intermediate parser
# Technically, the parser tool should be reading the VDJ rearrangements
# output file, parsing it, then writing the row data.
newd = airr.create('my_data.tsv')
newd.addRearrangementActivityWithParser('seq.fasta', 'VDJServer GLDB 10_05_2016', 'my_data.tsv', 'IgBlast', 'alignment', 'changeo', 'seq.igblast.out', 'MakeDb')
data = airr.read('toy_data.tsv')
for r in data:
    newd.write(r)
newd.close()

# create a derived rearrangements file with additional annotation
mored = airr.createDerivation('my_data.tsv', 'more_data.tsv', 'myTool', 'my special analysis', 'mytool', 'http://mytool.org')
mored[1].addFields('mytool', ['new_field', 'more_anotation'])
for r in mored[0]:
    print(r)
    r['new_field'] = 'A'
    r['more_annotation'] = 'B'
    mored[1].write(r)
mored[0].close()
mored[1].close()
