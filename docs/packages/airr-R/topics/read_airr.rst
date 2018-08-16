read_airr
---------

**Read an AIRR TSV**

Description
~~~~~~~~~~~

``read_airr`` reads a TSV containing AIRR records.

Usage
~~~~~

::

    read_airr(file, base = c("1", "0"), schema = RearrangementSchema, ...)

::

    read_rearrangement(file, base = c("1", "0"), ...)

::

    read_alignment(file, base = c("1", "0"), ...)

Arguments
~~~~~~~~~

file
    input file path.
base
    starting index for positional fields in the input file. If ``"1"``,
    then these fields will not be modified. If ``"0"``, then fields
    ending in ``"_start"`` and ``"_end"`` are 0-based half-open
    intervals (python style) in the input file and will be converted to
    1-based closed-intervals (R style).
schema
    ``Schema`` object defining the output format.
…
    additional arguments to pass to
    `read_delim <http://www.rdocumentation.org/packages/readr/topics/read_delim>`__.

Value
~~~~~

A data.frame of the TSV file with appropriate type and position
conversion for fields defined in the specification.

Details
~~~~~~~

``read_rearrangement`` reads an AIRR TSV containing Rearrangement data.

``read_alignment`` reads an AIRR TSV containing Alignment data.

Examples
~~~~~~~~

.. code:: r

    # Get path to the rearrangement-example file
    file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")

    # Load data file
    df <- read_rearrangement(file)

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema object definition.
See `write_airr <write_airr.html>`__ for writing AIRR data.
