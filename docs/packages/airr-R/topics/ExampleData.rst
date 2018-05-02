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
