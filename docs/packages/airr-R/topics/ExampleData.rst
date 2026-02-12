ExampleData
-----------

**Example AIRR data**

Description
~~~~~~~~~~~

Example data files compliant with the the AIRR Data Representation
standards.

Format
~~~~~~

- ``extdata/rearrangement-example.tsv.gz``: Rearrangement TSV file.
- ``extdata/repertoire-example.yaml``: Repertoire YAML file.
- ``extdata/germline-example.json``: GermlineSet and GenotypeSet JSON
  file.

Examples
~~~~~~~~

.. code:: r

   # Load Rearrangement example
   file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
   rearrangement <- read_rearrangement(file)

::

   indexed 0B in  0s, 0B/sindexed 1.00TB in  0s, 2.67PB/s                                                                                                                                                                                                             indexed 0B in  0s, 0B/sindexed 1.00TB in  0s, 2.43PB/s                                                                                                                                                                                                             

.. code:: r


   # Load Repertoire example
   file <- system.file("extdata", "repertoire-example.yaml", package="airr")
   repertoire <- read_airr(file)

   # Load GermlineSet and GenotypeSet examples
   file <- system.file("extdata", "germline-example.json", package="airr")
   germline <- read_airr(file)
