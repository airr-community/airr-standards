write_airr
----------

**Write an AIRR TSV**

Description
~~~~~~~~~~~

``write_airr`` writes an TSV containing AIRR formatted records.

Usage
~~~~~

::

    write_airr(data, file, base = c("0", "1"), schema = RearrangementSchema,
    ...)

::

    write_rearrangement(data, file, base = c("0", "1"), ...)

::

    write_alignment(data, file, base = c("0", "1"), ...)

Arguments
~~~~~~~~~

data
    data.frame of Rearrangement data.
file
    output file name.
base
    starting index for positional fields in the output file. If ``"0"``,
    then fields ending in ``_start`` and ``_end`` will be converted to
    0-based half-open intervals (python style) in the output file. If
    ``"1"``, then these fields will not be modified. Fields in the input
    ``data`` are assumed to be 1-based closed-intervals (R style).
schema
    ``Schema`` object defining the output format.
…
    additional arguments to pass to
    `write_tsv <http://www.rdocumentation.org/packages/readr/topics/write_delim>`__.

Details
~~~~~~~

``write_rearrangement`` writes a data.frame containing AIRR
Rearrangement data to TSV.

``write_alignment`` writes a data.frame containing AIRR Alignment data
to TSV.

Examples
~~~~~~~~

.. code:: r

    ### Not run:
    # Write Rearrangement data
    # write_rearrangement(data, "file.tsv")

See also
~~~~~~~~

See `Schema <Schema-class.md>`__ for the AIRR schema object definition.
See `read_airr <read_airr.md>`__ for reading to AIRR files.
