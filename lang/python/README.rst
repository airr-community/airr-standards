Installation
------------------------------------------------------------------------------

Install in the usual manner from PyPI::

    > pip3 install airr --user

Or from the `downloaded <https://github.com/airr-community/airr-standards>`__
source code directory::

    > python3 setup.py install --user


Quick Start
------------------------------------------------------------------------------

Deprecation Notice
^^^^^^^^^^^^^^^^^^^^

The ``load_repertoire``, ``write_repertoire``, and ``validate_repertoire`` functions
have been deprecated for the new generic ``load_airr_data``, ``write_airr_data``, and
``validate_airr_data`` functions. These new functions are backwards compatible with
the Repertoire metadata format but also support the new AIRR objects such as GermlineSet,
RepertoireGroup, GenotypeSet, Cell and Clone. This new format is defined by the DataFile
Schema, which describes a standard set of objects included in a file containing
AIRR Data Model presentations. Currently, the AIRR DataFile does not completely support
Rearrangement, so users should continue using AIRR TSV files and its specific functions.
Also, the ``repertoire_template`` function has been deprecated for the ``Schema.template``
method, which can now be called on any AIRR Schema to create a blank object.

Reading AIRR Data Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr`` package contains functions to read and write AIRR Data
Model files. The file format is either YAML or JSON, and the package provides a
light wrapper over the standard parsers. The file needs a ``json``, ``yaml``, or ``yml``
file extension so that the proper parser is utilized. All of the AIRR objects
are loaded into memory at once and no streaming interface is provided::

    import airr

    # Load the AIRR data
    data = airr.read_airr('input.airr.json')
    # loop through the repertoires
    for rep in data['Repertoire']:
        print(rep)

Why are the AIRR objects, such as Repertoire, GermlineSet, and etc., in a list versus in a
dictionary keyed by their identifier (e.g., ``repertoire_id``)? There are two primary reasons for
this. First, the identifier might not have been assigned yet. Some systems might allow MiAIRR
metadata to be entered but the identifier is assigned to that data later by another process. Without
the identifier, the data could not be stored in a dictionary. Secondly, the list allows the data to
have a default ordering. If you know that the data has a unique identifier then you can quickly
create a dictionary object using a comprehension. For example, with repertoires::

    rep_dict = { obj['repertoire_id'] : obj for obj in data['Repertoire'] }

another example with germline sets::

    germline_dict = { obj['germline_set_id'] : obj for obj in data['GermlineSet'] }

Writing AIRR Data Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writing an AIRR Data File is also a light wrapper over standard YAML or JSON
parsers. Multiple AIRR objects, such as Repertoire, GermlineSet, and etc., can be
written together into the same file. In this example, we use the ``airr`` library ``template``
method to create some blank Repertoire objects, and write them to a file.
As with the read function, the complete list of repertoires are written at once,
there is no streaming interface::

    import airr

    # Create some blank repertoire objects in a list
    data = { 'Repertoire': [] }
    for i in range(5):
        data['Repertoire'].append(airr.schema.RepertoireSchema.template())

    # Write the AIRR Data
    airr.write_airr('output.airr.json', data)

Reading AIRR Rearrangement TSV files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr`` package contains functions to read and write AIRR Rearrangement
TSV files as either iterables or pandas data frames. The usage is straightforward,
as the file format is a typical tab delimited file, but the package
performs some additional validation and type conversion beyond using a
standard CSV reader::

    import airr

    # Create an iteratable that returns a dictionary for each row
    reader = airr.read_rearrangement('input.tsv')
    for row in reader: print(row)

    # Load the entire file into a pandas data frame
    df = airr.load_rearrangement('input.tsv')

Writing AIRR Rearrangement TSV files
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

The ``airr`` package can validate AIRR Data Model JSON/YAML files and Rearrangement
TSV files to ensure that they contain all required fields and that the fields types
match the AIRR Schema. This can be done using the ``airr-tools`` command
line program or the validate functions in the library can be called::

    # Validate a rearrangement TSV file
    airr-tools validate rearrangement -a input.tsv

    # Validate an AIRR DataFile
    airr-tools validate airr -a input.airr.json

Combining Repertoire metadata and Rearrangement files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr`` package does not currently keep track of which AIRR Data Model files
are associated with which Rearrangement TSV files, though there is ongoing work to define
a standardized manifest, so users will need to handle those
associations themselves. However, in the data, AIRR identifier fields, such as ``repertoire_id``,
form the link between objects in the AIRR Data Model.
The typical usage is that a program is going to perform some
computation on the Rearrangements, and it needs access to the Repertoire metadata
as part of the computation logic. This example code shows the basic framework
for doing that, in this case doing gender specific computation::

    import airr

    # Load AIRR data containing repertoires
    data = airr.read_airr('input.airr.json')

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

