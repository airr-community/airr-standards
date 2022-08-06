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

   validate_airr(data, each = FALSE)

Arguments
~~~~~~~~~

data
   ``list`` containing records of an AIRR Data Model objected imported
   from a YAML or JSON representation.
each
   if ``TRUE`` return a logical vector with results for each object in
   ``data`` instead of a single ``TRUE`` or ``FALSE`` value.

Value
~~~~~

Returns ``TRUE`` if the input ``data`` is compliant with AIRR standards
and ``FALSE`` if not. If ``each=TRUE`` is set, then a vector with
results for each each object in ``data`` is returned instead.

Examples
~~~~~~~~

.. code:: r

   # Get path to the rearrangement-example file
   f1 <- system.file("extdata", "repertoire-example.yaml", package="airr")
   f2 <- system.file("extdata", "germline-example.json", package="airr")

   # Load data file
   repertoire <- read_airr(f1)
   germline <- read_airr(f2)

   # Validate a single record
   validate_airr(repertoire)

::

   [1] TRUE

.. code:: r


   # Return validation for individual objects
   validate_airr(germline, each=TRUE)

::

   GenotypeSet GermlineSet 
          TRUE        TRUE 

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema definitions. See
`read_airr <read_airr.html>`__ for loading AIRR Data Models from a file.
See `write_airr <write_airr.html>`__ for writing AIRR Data Models to a
file.
