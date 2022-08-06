validate_airr
-------------

**Validate an AIRR Data Model nested list representation**

Description
~~~~~~~~~~~

``validate_airr`` validates the fields in a named nested list
representation of the AIRR Data Model. Typically, generating by reading
of JSON or YAML formatted AIRR files.

Usage
~~~~~

::

   validate_airr(data)

Arguments
~~~~~~~~~

data
   ``list`` containing records of an AIRR Data Model objected imported
   from a YAML or JSON representation.

Value
~~~~~

Returns ``TRUE`` if the input ``data`` is compliant with AIRR standards
and ``FALSE`` if not.

Examples
~~~~~~~~

.. code:: r

   # Get path to the rearrangement-example file
   file <- system.file("extdata", "repertoire-example.yaml", package="airr")

   # Load data file
   repr <- read_airr(file)

   # Validate
   validate_airr(repr)

::

   [1] TRUE

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema definitions. See
`read_airr <read_airr.html>`__ for loading AIRR Data Models from a file.
See `write_airr <write_airr.html>`__ for writing AIRR Data Models to a
file.
