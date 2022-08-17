write_tabular
-------------

**Write an AIRR tabular data**

Description
~~~~~~~~~~~

``write_tabular`` writes a TSV containing AIRR tabular records.

Usage
~~~~~

::

   write_tabular(data, file, schema, base = c("1", "0"), ...)

::

   write_rearrangement(data, file, base = c("1", "0"), ...)

::

   write_alignment(data, file, base = c("1", "0"), ...)

Arguments
~~~~~~~~~

data
   ``data.frame`` of Rearrangement data.
file
   output file name.
schema
   ``Schema`` object defining the output format.
base
   starting index for positional fields in the output file. Fields in
   the input ``data`` are assumed to be 1-based closed-intervals (R
   style). If ``"1"``, then these fields will not be modified. If
   ``"0"``, then fields ending in ``_start`` and ``_end`` will be
   converted to 0-based half-open intervals (python style) in the output
   file.
…
   additional arguments to pass to
   `write_delim <http://www.rdocumentation.org/packages/readr/topics/write_delim>`__.

Details
~~~~~~~

``write_rearrangement`` writes a ``data.frame`` containing AIRR
Rearrangement data to TSV.

``write_alignment`` writes a ``data.frame`` containing AIRR Alignment
data to TSV.

Examples
~~~~~~~~

.. code:: r

   # Get path to the rearrangement-example file
   file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")

   # Load data file
   df <- read_rearrangement(file)

::

   [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m1.31PB/s[0m                                                                                                                                                                                          [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m672.49TB/s[0m                                                                                                                                                                                          

.. code:: r


   # Write a Rearrangement data file
   outfile <- file.path(tempdir(), "output.tsv")
   write_tabular(df, outfile, schema=RearrangementSchema)

::

   [1mwrote[0m [32m11.45kB[0m in [36m 0s[0m, [32m1.02GB/s[0m[1mwrote[0m [32m1.00TB[0m in [36m 0s[0m, [32m471.43TB/s[0m                                                                                                                                                                                          

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema object definition.
See `read_tabular <read_tabular.html>`__ for reading to AIRR files.
