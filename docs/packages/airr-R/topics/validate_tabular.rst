validate_tabular
----------------

**Validate tabular AIRR data**

Description
~~~~~~~~~~~

``validate_tabular`` validates compliance of the contents of a
``data.frame`` to the AIRR standards.

Usage
~~~~~

::

   validate_tabular(data, schema)

::

   validate_rearrangement(data)

Arguments
~~~~~~~~~

data
   ``data.frame`` of tabular data to validate.
schema
   ``Schema`` object defining the data standard of the table.

Value
~~~~~

Returns ``TRUE`` if the input ``data`` is compliant and ``FALSE`` if
not.

Details
~~~~~~~

``validate_rearrangement`` validates the standards compliance of AIRR
Rearrangement data stored in a ``data.frame``

Examples
~~~~~~~~

.. code:: r

   # Get path to the rearrangement-example file
   file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")

   # Load data file
   df <- read_rearrangement(file)

::

   [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m1.49PB/s[0m                                                                                                                                                                                          [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m1.12PB/s[0m                                                                                                                                                                                          

.. code:: r


   # Validate a data.frame against the Rearrangement schema
   validate_rearrangement(df)

::

   [1] TRUE
