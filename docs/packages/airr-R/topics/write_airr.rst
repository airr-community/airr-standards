write_airr
----------

**Write AIRR Data Model records to YAML or JSON files**

Description
~~~~~~~~~~~

``write_airr`` writes a YAML or JSON file containing AIRR Data Model
records.

Usage
~~~~~

::

   write_airr(
   data,
   file,
   format = c("auto", "yaml", "json"),
   validate = TRUE,
   adf = TRUE
   )

Arguments
~~~~~~~~~

data
   ``list`` containing AIRR Model Records.
file
   output file name.
format
   format of the output file. Must be one of ``"auto"``, ``"yaml"``, or
   ``"json"``. If ``"auto"`` (default), the format will be detected from
   the ``file`` extension.
validate
   run schema validation prior to write if ``TRUE``.
adf
   if ``TRUE`` validate and write only AIRR DataFile defined objects. If
   ``FALSE`` attempt validation and write of all objects in ``data``.

Examples
~~~~~~~~

.. code:: r

   # Get path to the repertoire-example file
   file <- system.file("extdata", "repertoire-example.yaml", package="airr")

   # Load data file
   repertoire <- read_airr(file)

   # Write a Rearrangement data file
   outfile <- file.path(tempdir(), "output.yaml")
   write_airr(repertoire, outfile)

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema definition objects.
See `read_airr <read_airr.html>`__ for reading to AIRR Data Model files.
