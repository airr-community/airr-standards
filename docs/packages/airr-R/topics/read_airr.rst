read_airr
---------

**Read an AIRR Data Model file in YAML or JSON format**

Description
~~~~~~~~~~~

``read_airr`` loads a YAML or JSON file containing AIRR Data Model
records.

Usage
~~~~~

::

   read_airr(
   file,
   format = c("auto", "yaml", "json"),
   validate = TRUE,
   adf = TRUE
   )

Arguments
~~~~~~~~~

file
   path to the input file.
format
   format of the input file. Must be one of ``"auto"``, ``"yaml"``, or
   ``"json"``. If ``"auto"`` (default), the format will be detected from
   the ``file`` extension.
validate
   run schema validation if ``TRUE``.
adf
   if ``TRUE`` validate only AIRR DataFile defined objects. If ``FALSE``
   attempt validation of all objects in ``data``. Ignored if
   ``validate=FALSE``

Value
~~~~~

A named nested ``list`` contained in the AIRR Data Model with the
top-level names reflecting the individual AIRR objects.

Examples
~~~~~~~~

.. code:: r

   # Get path to the Reportoire and GermlineSet example files
   f1 <- system.file("extdata", "repertoire-example.yaml", package="airr")
   f2 <- system.file("extdata", "germline-example.json", package="airr")

   # Load data files
   repertoire <- read_airr(f1)
   germline <- read_airr(f2)

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema definition objects.
See `write_airr <write_airr.html>`__ for writing AIRR Data Model records
in YAML or JSON format.
