ExampleData
-----------

**Example AIRR data**

Description
~~~~~~~~~~~

Example data files compliant with the the AIRR Data Representation
standards.

Format
~~~~~~

-  ``extdata/rearrangement-example.tsv.gz``: Rearrangement TSV file.
-  ``extdata/repertoire-example.yaml``: Repertoire YAML file.
-  ``extdata/germline-example.json``: GermlineSet and GenotypeSet JSON
   file.

Examples
~~~~~~~~

.. code:: r

   # Load Rearrangement example
   file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
   rearrangement <- read_rearrangement(file)

::

   [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m1.24PB/s[0m                                                                                                                                                                                          [1mindexed[0m [32m0B[0m in [36m 0s[0m, [32m0B/s[0m[1mindexed[0m [32m1.00TB[0m in [36m 0s[0m, [32m845.97TB/s[0m                                                                                                                                                                                          

.. code:: r


   # Load Repertoire example
   file <- system.file("extdata", "repertoire-example.yaml", package="airr")
   repertoire <- read_airr(file)

   # Load GermlineSet and GenotypeSet examples
   file <- system.file("extdata", "germline-example.json", package="airr")
   germline <- read_airr(file)
