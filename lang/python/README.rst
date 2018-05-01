AIRR Python Reference Library
===============================================================================

**Installation**

Install in the usual manner from PyPI::

    > pip3 install airr --user

Or from the `downloaded <https://github.com/airr-community/airr-standards>`__
source code directory::

    > python3 setup.py install --user

**Reading AIRR formatted files**

The ``airr`` package contains functions to read and write AIRR data files
as either iterables or pandas data frames. The usage is straightforward,
as the file format is a typical tab delimited file, but the package
performs some additional validation and type conversion beyond using a
standard CSV reader.

.. code-block:: python

    import airr

    # Create an iteratable that returns a dictionary for each row
    reader = airr.read_rearrangement(open('input.tsv', 'r'))

    # Load the entire file into a pandas data frame
    df = airr.load_rearrangement(open('input.tsv', 'r'))

**Writing AIRR formatted files**

Similar to the read operations, write functions are provided for either creating
a writer class to perform row-wise output or writing the entire contents of
a pandas data frame to a file. Again, usage is straightforward with the `airr`
output functions simply performing some type conversion and field ordering
operations.

.. code-block:: python

    import airr

    # Create a writer class for iterative row output
    writer = airr.create_rearrangement(open('output.tsv', 'w'))
    for row in reader:  writer.write(row)

    # Write an entire pandas data frame to a file
    airr.dump_rearrangement(df, open('file.tsv', 'w'))