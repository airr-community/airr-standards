ExampleData
-----------

**Example AIRR data**

Description
~~~~~~~~~~~

Example data files compliant with the the AIRR Data Representation
standards.

Format
~~~~~~

``extdata/rearrangement-example.tsv.gz``: Rearrangement TSV file.

Examples
~~~~~~~~

.. code:: r

   # Get path to the rearrangement-example file
   file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")

   # Load data file
   df <- read_rearrangement(file)

::

   [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m1.49PB/s[0m                                                                                                                                                                                          [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m103.95TB/s[0m                                                                                                                                                                                          
