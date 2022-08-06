read_tabular
------------

**Read AIRR tabular data**

Description
~~~~~~~~~~~

``read_tabular`` reads a tab-delimited (TSV) file containing tabular
AIRR records.

Usage
~~~~~

::

   read_tabular(file, schema, base = c("1", "0"), aux_types = NULL, ...)

::

   read_rearrangement(file, base = c("1", "0"), ...)

::

   read_alignment(file, base = c("1", "0"), ...)

Arguments
~~~~~~~~~

file
   input file path.
schema
   ``Schema`` object defining the output format.
base
   starting index for positional fields in the input file. If ``"1"``,
   then these fields will not be modified. If ``"0"``, then fields
   ending in ``"_start"`` and ``"_end"`` are 0-based half-open intervals
   (python style) in the input file and will be converted to 1-based
   closed-intervals (R style).
aux_types
   named vector or list giving the type for fields that are not defined
   in ``schema``. The field name is the name, the value the type,
   denoted by one of ``"c"`` (character), ``"l"`` (logical), ``"i"``
   (integer), ``"d"`` (double), or ``"n"`` (numeric).
…
   additional arguments to pass to
   `read_delim <http://www.rdocumentation.org/packages/readr/topics/read_delim>`__.

Value
~~~~~

A ``data.frame`` of the TSV file with appropriate type and position
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

::

   [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m1.47PB/s[0m                                                                                                                                                                                          [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m877.10TB/s[0m                                                                                                                                                                                          

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema object definition.
See `write_tabular <write_tabular.html>`__ for writing AIRR data.
