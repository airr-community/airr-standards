Installation
------------------------------------------------------------------------------

Install in the usual manner from PyPI::

    > pip3 install airr --user

Or from the `downloaded <https://github.com/airr-community/airr-standards>`__
source code directory::

    > python3 setup.py install --user


Quick Start
------------------------------------------------------------------------------

Reading AIRR Repertoire metadata files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr`` package contains functions to read and write AIRR repertoire metadata
files. The file format is either YAML or JSON, and the package provides a
light wrapper over the standard parsers. The file needs a ``json``, ``yaml``, or ``yml``
file extension so that the proper parser is utilized. All of the repertoires are loaded
into memory at once and no streaming interface is provided::

    import airr

    # Load the repertoires
    data = airr.load_repertoire('input.airr.json')
    for rep in data['Repertoire']:
        print(rep)

Why are the repertoires in a list versus in a dictionary keyed by the ``repertoire_id``?
There are two primary reasons for this. First, the ``repertoire_id`` might not have been
assigned yet. Some systems might allow MiAIRR metadata to be entered but the
``repertoire_id`` is assigned to that data later by another process. Without the
``repertoire_id``, the data could not be stored in a dictionary. Secondly, the list allows
the repertoire data to have a default ordering. If you know that the repertoires all have
a unique ``repertoire_id`` then you can quickly create a dictionary object using a
comprehension::

    rep_dict = { obj['repertoire_id'] : obj for obj in data['Repertoire'] }

Writing AIRR Repertoire metadata files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writing AIRR repertoire metadata is also a light wrapper over standard YAML or JSON
parsers. The ``airr`` library provides a function to create a blank repertoire object
in the appropriate format with all of the required fields. As with the load function,
the complete list of repertoires are written at once, there is no streaming interface::

    import airr

    # Create some blank repertoire objects in a list
    reps = []
    for i in range(5):
        reps.append(airr.repertoire_template())

    # Write the repertoires
    airr.write_repertoire('output.airr.json', reps)

Reading AIRR Rearrangement TSV files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr`` package contains functions to read and write AIRR rearrangement files
as either iterables or pandas data frames. The usage is straightforward,
as the file format is a typical tab delimited file, but the package
performs some additional validation and type conversion beyond using a
standard CSV reader::

    import airr

    # Create an iteratable that returns a dictionary for each row
    reader = airr.read_rearrangement('input.tsv')
    for row in reader: print(row)

    # Load the entire file into a pandas data frame
    df = airr.load_rearrangement('input.tsv')

Writing AIRR formatted files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to the read operations, write functions are provided for either creating
a writer class to perform row-wise output or writing the entire contents of
a pandas data frame to a file. Again, usage is straightforward with the ``airr``
output functions simply performing some type conversion and field ordering
operations::

    import airr

    # Create a writer class for iterative row output
    writer = airr.create_rearrangement('output.tsv')
    for row in reader:  writer.write(row)

    # Write an entire pandas data frame to a file
    airr.dump_rearrangement(df, 'file.tsv')

By default, ``create_rearrangement`` will only write the ``required`` fields
in the output file. Additional fields can be included in the output file by
providing the ``fields`` parameter with an array of additional field names::

    # Specify additional fields in the output
    fields = ['new_calc', 'another_field']
    writer = airr.create_rearrangement('output.tsv', fields=fields)

A common operation is to read an AIRR rearrangement file, and then
write an AIRR rearrangement file with additional fields in it while
keeping all of the existing fields from the original file. The
``derive_rearrangement`` function provides this capability::

    import airr

    # Read rearrangement data and write new file with additional fields
    reader = airr.read_rearrangement('input.tsv')
    fields = ['new_calc']
    writer = airr.derive_rearrangement('output.tsv', 'input.tsv', fields=fields)
    for row in reader:
        row['new_calc'] = 'a value'
        writer.write(row)


Validating AIRR data files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr`` package can validate repertoire, rearrangement, germline set
and genotype data files
to ensure that they contain all required fields and that the fields types
match the AIRR Schema. This can be done using the ``airr-tools`` command
line program or the validate functions in the library can be called::

    # Validate a rearrangement file
    airr-tools validate rearrangement -a input.tsv

    # Validate a repertoire metadata file
    airr-tools validate repertoire -a input.airr.json

    # Validate a germline set file
    airr-tools validate germline_set -a germline_set.json

    # Validate a genotype set file
    airr-tools validate genotype_set -a genotype_set.json

Combining Repertoire metadata and Rearrangement files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr`` package does not keep track of which repertoire metadata files
are associated with rearrangement files, so users will need to handle those
associations themselves. However, in the data, the ``repertoire_id`` field forms
the link. The typical usage is that a program is going to perform some
computation on the rearrangements, and it needs access to the repertoire metadata
as part of the computation logic. This example code shows the basic framework
for doing that, in this case doing gender specific computation::

    import airr

    # Load the repertoires
    data = airr.load_repertoire('input.airr.json')

    # Put repertoires in dictionary keyed by repertoire_id
    rep_dict = { obj['repertoire_id'] : obj for obj in data['Repertoire'] }

    # Create an iteratable for rearrangement data
    reader = airr.read_rearrangement('input.tsv')
    for row in reader:
        # get repertoire metadata with this rearrangement
        rep = rep_dict[row['repertoire_id']]
        
        # check the gender
        if rep['subject']['sex'] == 'male':
            # do male specific computation
        elif rep['subject']['sex'] == 'female':
            # do female specific computation
        else:
            # do other specific computation

Reading AIRR Germline Sets and Genotype Sets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As for repertoires, The ``airr`` package contains functions to read and write AIRR
germline and genotype sets.
files. The file format is either YAML or JSON, and the package provides a
light wrapper over the standard parsers. The file needs a ``json``, ``yaml``, or ``yml``
file extension so that the proper parser is utilized::

    import airr

    data = airr.load_germline_set('data/good_germline_set.json')
    germline_set = data['GermlineSet']

    for allele_description in germline_set['allele_descriptions']:
        print(allele_description['label'])

    data = airr.load_genotype_set('data/good_genotype_set.json')
    genotype_set = data['GenotypeSet']

    for genotype_class in genotype_set['genotype_class_list']:
        print(genotype_class['locus'])

Validating AIRR Genotypes and Germline Sets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can validate germline set and genotype sets as they are loaded using the validate flag::

    import airr

    try:
        data = airr.load_germline_set('data/bad_germline_set.json', validate=True)
    except airr.ValidationError:
        print('The format of the germline set is invalid')

    try:
        data = airr.load_genotype_set('data/bad_genotype_set.json', validate=True)
    except airr.ValidationError:
        print('The format of the genotype set is invalid')


You can validate germline sets and genotype sets in-memory (for example sets that
you have created or manipulated) using validate_germline_set and validate_genotype_set::

    import airr

    try:
        data = airr.load_germline_set('data/bad_germline_set.json')
        airr.validate_germline_set(data)
    except airr.ValidationError:
        print('The format of the germline set is invalid')

    try:
        data = airr.load_genotype_set('data/bad_genotype_set.json')
        airr.validate_genotype_set(data)
    except airr.ValidationError:
        print('The format of the genotype set is invalid')



