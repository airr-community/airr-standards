validate_airr
-------------

**Validate AIRR data**

Description
~~~~~~~~~~~

``validate_airr`` validates compliance of the contents of a data.frame
to the AIRR data standards.

Usage
~~~~~

::

    validate_airr(data, schema = RearrangementSchema)

Arguments
~~~~~~~~~

data
    data.frame to validate.
schema
    ``Schema`` object defining the data standard.

Value
~~~~~

Returns ``TRUE`` if the input ``data`` is compliant and ``FALSE`` if
not.

Examples
~~~~~~~~

.. code:: r

    # Get path to the rearrangement-example file
    file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")

    # Load data file
    df <- read_rearrangement(file)

    # Validate a data.frame against the Rearrangement schema
    validate_airr(data, schema=RearrangementSchema)

*Warning*:Warning: File is missing AIRR mandatory field(s): sequence_id,
sequence, rev_comp, productive, v_call, d_call, j_call,
sequence_alignment, germline_alignment, junction, junction_aa, v_cigar,
d_cigar, j_cigar

::

    [1] FALSE

