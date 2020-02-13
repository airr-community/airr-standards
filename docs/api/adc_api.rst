.. _DataCommons:

AIRR Data Commons API V1
=============================

The use of high-throughput sequencing for profiling B-cell and T-cell
receptors has resulted in a rapid increase in data generation. It is
timely, therefore, for the Adaptive Immune Receptor Repertoire (AIRR)
community to establish a clear set of community-accepted data and
metadata standards; analytical tools; and policies and practices for
infrastructure to support data deposit, curation, storage, and
use. Such actions are in accordance with international funder and
journal policies that promote data deposition and data sharing – at a
minimum, data on which scientific publications are based should be
made available immediately on publication. Data deposit in publicly
accessible databases ensures that published results may be
validated. Such deposition also facilitates reuse of data for the
generation of new hypotheses and new knowledge.

The AIRR Common Repository Working Group (CRWG) developed a set of
recommendations__ (v0.6.0) that promote the deposit, sharing, and use
of AIRR sequence data. These recommendations were refined following
community discussions at the AIRR 2016 and 2017 Community Meetings and
were approved through a vote by the AIRR Community at the AIRR
Community Meeting in December 2017.

.. __: https://github.com/airr-community/common-repo-wg/blob/v0.6.0/recommendations.md

Overview
--------

The AIRR Data Commons (ADC) API provides programmatic access to
query and download AIRR-seq data. The ADC API uses JSON as its
communication format, and standard HTTP methods like ``GET`` and
``POST``. The ADC API is read-only and the mechanism of inclusion of
AIRR-seq studies into a data repository is left up to the repository.

This documentation explains how to construct and execute API requests
and interpret API responses.

**API Endpoints**

The ADC API is versioned with the version number (``v1``) as part of the
base path for all endpoints. Each ADC API endpoint represents
specific functionality as summarized in the following table:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Endpoint
      - Type
      - HTTP
      - Description
    * - ``/v1``
      - Service status
      - ``GET``
      - Returns success if API service is running.
    * - ``/v1/info``
      - Service information
      - ``GET``
      - Upon success, returns service information such as name, version, etc.
    * - ``/v1/swagger``
      - Swagger specification for API
      - ``GET``
      - Upon success, returns the OpenAPI specification for the ADC API implemented by this service. Useful for loading the API into tools like Swagger Editor__.
    * - ``/v1/repertoire/{repertoire_id}``
      - Retrieve a repertoire given its ``repertoire_id``
      - ``GET``
      - Upon success, returns the ``Repertoire`` information in JSON according to the :ref:`Repertoire schema <RepertoireSchema>`.
    * - ``/v1/repertoire``
      - Query repertoires
      - ``POST``
      - Upon success, returns a list of ``Repertoires`` in JSON according to the :ref:`Repertoire schema <RepertoireSchema>`.
    * - ``/v1/rearrangement/{rearrangement_id}``
      - Retrieve a rearrangement given its ``rearrangement_id``
      - ``GET``
      - Upon success, returns the ``Rearrangement`` information in JSON or TSV format according to the :ref:`Rearrangement schema <RearrangementSchema>`.
    * - ``/v1/rearrangement``
      - Query rearrangements
      - ``POST``
      - Upon success, returns a list of ``Rearrangements`` in JSON or TSV format according to the :ref:`Rearrangement schema <RearrangementSchema>`.

.. __: https://swagger.io/tools/swagger-editor/

**Authentication**

The ADC API currently does not define an authentication
method. Future versions of the API will provide an authentication
method so data repositories can support query and download of
controlled-access data.

Search and Retrieval
--------------------

The AIRR Data Commons REST API specifies endpoints for searching and
retrieving AIRR-seq data sets stored in an AIRR-compliant Data
Repository according to the AIRR Data Model. This documentation
describes Version 1 of the API. The general format of requests
and associated parameters are described below.

The design of the AIRR Data Commons REST API was greatly inspired by
National Cancer Institute's Genomic Data Commons (GDC) API__.

.. __: https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/

Components of a Request
~~~~~~~~~~~~~~~~~~~~~~~

The ADC API has two classes of endpoints. The endpoints that respond
to ``GET`` requests are simple services that require few or no
parameters. While, the endpoints that response to ``POST`` requests
are the main query services and provide many parameters for specifying
the query as well as the data in the API response.

A typical ``POST`` query request specifies the following parameters:

+ The ``filters`` parameter specifies the query.

+ The ``fields`` parameter specifies which data elements to be returned in the response.

+ The ``from`` and ``size`` parameters specify the number of results to skip and the maximum number of results to be returned in the response.

**Service Status Example**

The following is an example ``GET`` request to check that the service
API is available for VDJServer's data repository.

.. code-block:: bash

  curl https://vdjserver.org/airr/v1

The response should indicate success.

.. code-block:: json

  {"result":"success"}

**Service Info Example**

The following is an example ``GET`` request to get information about the service.

.. code-block:: bash

  curl https://vdjserver.org/airr/v1

The response provides various information.

.. code-block:: json

  {
    "name": "adc-api-js-mongodb",
    "description": "AIRR Data Commons API reference implementation",
    "version": "1.0.0",
    "airr_schema_version": 1.3,
    "max_size": 1000,
    "max_query_size": 2097152,
    "contact": {
      "name": "AIRR Community",
      "url": "https://github.com/airr-community"
    }
  }

**Query Repertoire Example**

The following is an example ``POST`` request to the ``repertoire``
endpoint of the ADC API. It queries for repertoires of human TCR beta
receptors (``filters``), skips the first 10 results (``from``),
requests 5 results (``size``), and requests only the ``repertoire_id``
field (``fields``).

.. code-block:: bash

  curl --data @query1-2_repertoire.json https://vdjserver.org/airr/v1/repertoire

The content of the :download:`JSON payload <../examples/queries/query1-2_repertoire.json>`.

.. literalinclude:: ../examples/queries/query1-2_repertoire.json
  :language: JSON

The response contains two JSON objects, an Info object that provides information about the API response and a Repertoire object that contains the list of Repertoires that met the query search criteria. In this case, the query returns a list of five repertoire identifiers. Note the Info object is based on the info block as specified in the OpenAPI v2.0 specification.

.. code-block:: json

  {
    "Info":
    {
        "title": "AIRR Data Commons API reference implementation",
        "description": "API response for repertoire query",
        "version": 1.3,
        "contact":
        {
            "name": "AIRR Community",
            "url": "https://github.com/airr-community"
        }
    },
    "Repertoire":
    [
        {"repertoire_id": "4357957907784536551-242ac11c-0001-012"},
        {"repertoire_id": "4476756703191896551-242ac11c-0001-012"},
        {"repertoire_id": "6205695788196696551-242ac11c-0001-012"},
        {"repertoire_id": "6393557657723736551-242ac11c-0001-012"},
        {"repertoire_id": "7158276584776536551-242ac11c-0001-012"}
    ]
  }

Endpoints
~~~~~~~~~

The ADC API V1 provides two primary endpoints for querying and
retrieving AIRR-seq data. The ``repertoire`` endpoint allows querying
upon any field in the :ref:`Repertoire schema
<RepertoireSchema>` including study, subject, sample, cell
processing, nucleic acid processing, sequencing run, raw sequencing
files, and data processing information. Queries on the content of raw
sequencing files is not support but is supported on file attributes
such as name, type and read information. Queries on ``Rearrangements``
is provided by the ``rearrangement`` endpoint.

The standard workflow to retrieve all of the data for an AIRR-seq
study involves performing a query on the ``repertoire`` endpoint to
retrieve the repertoires in the study, and one or more queries on the
``rearrangement`` endpoint to download the rearrangement data for each
repertoire. The endpoints are designed so the API
response can be saved directly into a file and be used by AIRR
analysis tools, including the AIRR python and R reference libraries,
without requiring modifications or transformation of the data.

**Repertoire Endpoint**

The ``repertoire`` endpoint provides access to all fields in
the :ref:`Repertoire schema <RepertoireSchema>`. There are two
type of endpoints; one for retrieving a single repertoire given its
identifier, and another for performing a query across all repertoires
in the data repository.

It is expected that the number of repertoires in a data repository
will never become so large such that queries become computationally
expensive. A data repository might have thousands of repertoires
across hundreds of studies, yet such numbers are easily handled by
modern databases. Based upon this, the ADC API does not place limits
on the ``repertoire`` endpoint for the fields that can be queried, the
operators that can be used, or the number of results that can be
returned.

*Retrieve a Single Repertoire*

Given a ``repertoire_id``, a single ``Repertoire`` object will be
returned.

.. code-block:: bash

  curl https://vdjserver.org/airr/v1/repertoire/4357957907784536551-242ac11c-0001-012

The response will provide the ``Repertoire`` data in JSON format.

.. code-block:: json

  {
    "Info":
    {
        "title": "AIRR Data Commons API reference implementation",
        "description": "API response for repertoire query",
        "version": 1.3,
        "contact":
        {
            "name": "AIRR Community",
            "url": "https://github.com/airr-community"
        }
    },
    "Repertoire":
    [
      {
        "repertoire_id":"4357957907784536551-242ac11c-0001-012",
        "study":{
           "study_id":"PRJNA300878",
           "submitted_by":"Florian Rubelt",
           "pub_ids":"PMID:27005435",
           "lab_name":"Mark M. Davis",
           "lab_address":"Stanford University",
           "study_title":"Homo sapiens B and T cell repertoire - MZ twins"
        },
        "subject":{
           "subject_id":"TW02A",
           "synthetic":false,
           "linked_subjects":"TW02B",
           "organism":{"id":"9606","value":"Homo sapiens"},
           "age":"25yr",
           "link_type":"twin",
           "sex":"F"
        },
        "sample":[
          {"sample_id":"TW02A_T_memory_CD4",
           "pcr_target":[{"pcr_target_locus":"TRB"}],
           "cell_isolation":"FACS",
           "read_length":"300",
           "cell_phenotype":"expression of CD45RO and CCR7",
           "cell_subset":"Memory CD4+ T cell",
           "filename":"SRR2905669_R1.fastq.gz",
           "single_cell":false,
           "file_type":"fastq",
           "tissue":"PBMC",
           "template_class":"RNA",
           "paired_filename":"SRR2905669_R2.fastq.gz",
           "paired_read_direction":"reverse",
           "read_direction":"forward",
           "sequencing_platform":"Illumina MiSeq"}
        ],
        "data_processing":[
          {"data_processing_id":"4976322832749171176-242ac11c-0001-012",
           "analysis_provenance_id":"651223970338378216-242ac11b-0001-007"}
        ]
      }
    ]
  }

*Query against all Repertoires*

A query in JSON format is passed in a ``POST`` request. This example queries for
repertoires of human IG heavy chain receptors for all studies in the data repository.

.. code-block:: bash

  curl --data @query2_repertoire.json https://vdjserver.org/airr/v1/repertoire

The content of the :download:`JSON payload <../examples/queries/query2_repertoire.json>`.

.. literalinclude:: ../examples/queries/query2_repertoire.json
  :language: JSON

The response will provide a list of ``Repertoires`` in JSON
format. The example output is not provided here due to its size.

**Rearrangement Endpoint**

The ``rearrangement`` endpoint provides access to all fields in
the :ref:`Rearrangement schema <RearrangementSchema>`. There are two
type of endpoints; one for retrieving a single rearrangement given its
identifier, and another for performing a query across all
rearrangements in the data repository.

Unlike repertoire data, data repositories are expected to store
millions or billions of rearrangement records, where performing
"simple" queries can quickly become computationally expensive. Data
repositories will need to optimize their databases for
performance. Therefore, the ADC API does not require that all fields
be queryable and only a limited set of query capabilities must be
supported. The queryable fields are described in the Fields section
below.

*Retrieve a Single Rearrangement*

Given a ``rearrangement_id``, a single ``Rearrangement`` object will
be returned.

.. code-block:: bash

  curl https://vdjserver.org/airr/v1/rearrangement/5d6fba725dca5569326aa104

The response will provide the ``Rearrangement`` data in JSON format.

.. code-block:: json

  {
    "Info":
    {
        "title": "AIRR Data Commons API reference implementation",
        "description": "API response for rearrangement query",
        "version": 1.3,
        "contact":
        {
            "name": "AIRR Community",
            "url": "https://github.com/airr-community"
        }
    },
    "Rearrangement":
    [
      {
        "rearrangement_id":"5d6fba725dca5569326aa104",
        "repertoire_id":"1841923116114776551-242ac11c-0001-012",

        "... remaining fields":"snipped for space"
      }
    ]
  }

*Query against all Rearrangements*

Supplying a ``repertoire_id``, when it is known, should greatly speed
up the query as it can significantly reduce the amount of data to be
searched, though it isn't necessary.

This example queries for rearrangements with a specific junction amino
acid sequence among a set of repertoires. A limited set of fields is
requested to be returned. The resultant data can be
requested in JSON or :ref:`AIRR TSV <FormatSpecification>` format.

.. code-block:: bash

  curl --data @query1_rearrangement.json https://vdjserver.org/airr/v1/rearrangement

The content of the :download:`JSON payload <../examples/queries/query1_rearrangement.json>`.

.. literalinclude:: ../examples/queries/query1_rearrangement.json
  :language: JSON

Here is the response in AIRR TSV format.

.. code-block:: text

  productive	v_call	rearrangement_id	repertoire_id
  true	IGHV1-69*04	5d6fba725dca5569326aa106	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*04	5d6fba725dca5569326aa11b	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*10	5d6fba725dca5569326aa149	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*04	5d6fba735dca5569326aa245	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*04	5d6fba735dca5569326aa274	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*04	5d6fba735dca5569326aa27b	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*04	5d6fba735dca5569326aa27c	1841923116114776551-242ac11c-0001-012
  true	IGHV1-24*01	5d6fba735dca5569326aa2a0	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*04	5d6fba745dca5569326aa359	1841923116114776551-242ac11c-0001-012
  true	IGHV1-69*04	5d6fba745dca5569326aa408	1841923116114776551-242ac11c-0001-012

Request Parameters
~~~~~~~~~~~~~~~~~~

The ADC API supports the follow query parameters. These are only
applicable to the ``repertoire`` and ``rearrangement`` query
endpoints, i.e. the HTTP ``POST`` endpoints.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Parameter
      - Default
      - Description
    * - ``filters``
      - null
      - Specifies logical expression for query critieria
    * - ``format``
      - JSON
      - Specifies the API response format: JSON, AIRR TSV
    * - ``fields``
      - null
      - Specifies which fields to include in the response
    * - ``from``
      - 0
      - Specifies the first record to return from a set of search results
    * - ``size``
      - repository dependent
      - Specifies the number of results to return
    * - ``facets``
      - null
      - Provide aggregate count information for the specified fields

**Filters Query Parameter**

The ``filters`` parameter enables passing complex query criteria to
the ADC API. The parameter represents the query in a JSON object.

A ``filters`` query consists of an operator (or a nested set of
operators) with a set of ``field`` and ``value`` operands. The query
criteria as represented in a JSON object can be considered an
expression tree data structure where internal nodes are operators and
child nodes are operands. The expression tree can be of any depth, and
recursive algorithms are typically used for tree traversal.

The following operators are support by the ADC API.

.. |br| raw:: html

    <br>

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Operator
      - Operands
      - Value Data Types
      - Description
      - Example
    * - =
      - field and value
      - string, number, integer, or boolean
      - equals
      - {"op":"=","content":{"field":"junction_aa","value":"CASSYIKLN"}}
    * - !=
      - field and value
      - string, number, integer, or boolean
      - does not equal
      - {"op":"!=","content":{"field":"subject.organism.id","value":"9606"}}
    * - <
      - field and value
      - number, integer
      - less than
      - {"op":"<","content":{"field":"sample.cell_number","value":1000}}
    * - <=
      - field and value
      - number, integer
      - less than or equal
      - {"op":"<=","content":{"field":"sample.cell_number","value":1000}}
    * - >
      - field and value
      - number, integer
      - greater than
      - {"op":">","content":{"field":"sample.cells_per_reaction","value":10000}}
    * - >=
      - field and value
      - number, integer
      - greater than or equal
      - {"op":">=","content":{"field":"sample.cells_per_reaction","value":10000}}
    * - is missing
      - field
      - n/a
      - field is missing or is null
      - {"op":"is missing","content":{"field":"sample.tissue"}}
    * - is
      - field
      - n/a
      - identical to "is missing" operator, provided for GDC compatibility
      - {"op":"is","content":{"field":"sample.tissue"}}
    * - is not missing
      - field
      - n/a
      - field is not missing and is not null
      - {"op":"is not missing","content":{"field":"sample.tissue"}}
    * - not
      - field
      - n/a
      - identical to "is not missing" operator, provided for GDC compatibility
      - {"op":"not","content":{"field":"sample.tissue"}}
    * - in
      - field, multiple values in a list
      - string, number, or integer
      - matches a string or number in a list
      - {"op":"in","content":{"field":"subject.strain_name","value":["C57BL/6","BALB/c","NOD"]}}
    * - exclude
      - field, multiple values in a list
      - string, number, or integer
      - does not match any string or number in a list
      - {"op":"exclude","content":{"field":"subject.strain_name","value":["SCID","NOD"]}}
    * - contains
      - field, value
      - string
      - contains the substring
      - {"op":"contains","content":{"field":"study.study_title","value":"cancer"}}
    * - and
      - multiple operators
      - n/a
      - logical AND
      - {"op":"and","content":[ |br| {"op":"!=","content":{"field":"subject.organism.id","value":"9606"}}, |br| {"op":">=","content":{"field":"sample.cells_per_reaction","value":10000}}, |br| {"op":"exclude","content":{"field":"subject.strain_name","value":["SCID","NOD"]}} |br| ]}
    * - or
      - multiple operators
      - n/a
      - logical OR
      - {"op":"and","content":[ |br| {"op":"<","content":{"field":"sample.cell_number","value":1000}}, |br| {"op":"is missing","content":{"field":"sample.tissue"}}, |br| {"op":"exclude","content":{"field":"subject.organism.id","value":["9606","10090"]}} |br| ]}

Note that the ``not`` operator is different from a logical NOT
operator, and the logical NOT is not needed as the other operators
provide negation.

The ``field`` operand specifies a complete property name in the AIRR
Data Model. The Fields section below describes the available queryable
fields.

The ``value`` operand specifies one or more values when evaluating the
operator for the ``field`` operand.

A simple query with a single operator looks like this:

.. code-block:: json

  {
    "filters": {
      "op":"=",
      "content": {
        "field":"junction_aa",
        "value":"CASSYIKLN"
      }
    }
  }

A more complex query with multiple operators looks like this:

.. code-block:: json

  {
    "filters": {
      "op":"and",
      "content": [
        {
          "op":"!=",
          "content": {
            "field":"subject.organism.id",
            "value":"9606"
          }
        },
        {
          "op":">=",
          "content": {
            "field":"sample.cells_per_reaction",
            "value":"10000"
          }
        },
        {
          "op":"exclude",
          "content": {
            "field":"subject.organism.id",
            "value": ["9606", "10090"]
          }
        }
      ]
    }
  }

**Format Query Parameter**

Specifies the format of the API response. JSON is the default format
and the only format available for all endpoints except for the
``rearrangement`` endpoint that accepts AIRR for the :ref:`AIRR TSV
<FormatSpecification>` format.

**Fields Query Parameter**

The ``fields`` parameter specifies which fields are to be included in
the API response. By default all fields with non-null values are
returned in the API response.

**Size and From Query Parameters**

The ADC API provides a pagination feature that limits the number of results returned by the API.

The ``from`` query parameter specifies which record to start from when
returning results. This allows records to be skipped. The default
value is ``0`` indicating that the first record in the set of results
will be returned.

The ``size`` query parameters specifies the maximum number of results
to return. The default value is specific to the data repository, and a
maximum value may be imposed by the data repository. This is to
prevent queries from "accidently" returning millions of records. The
``info`` endpoint provides the data repository default and maximum
values for the ``repertoire`` and ``rearrangement`` endpoints, which
may have different values. A value of ``0`` indicates there is no
limit on the number of results to return, but if the data repository
does not support this then the default value will be used.

The combination of ``from`` and ``size`` can be used to implement
pagination in a graphical user interface, or to split a very large
download into smaller batches. For example, if an interface displays
10 records as a time, the request would assign ``size=10`` and
``from=0`` to get the ten results to display on the first page. When
the user traverses to the "next page", the request would assign
``from=10`` to skip the first ten results and return the next ten
results, and ``from=20`` for the next page after that, and so on.

**Facets Query Parameter**

The ``facets`` parameter aggregate count information for the specified
field. Only a single field can be specified. It provides all values
that exist for the field, and the number of records (repertoires or
rearrangement) that have this value. The typical use of this parameter
is for displaying aggregate information in a graphical user
interface. The ``facets`` parameter can be used in conjunction with
the ``filters`` parameter to get aggregate information for a set of
search results.

Here is a simple query with only the ``facets`` parameter to return
the set of values for ``sample.pcr_target.pcr_target_locus`` and the
count of repertoires repertoires that have each value. The content of
the :download:`JSON payload <../examples/queries/facets1_repertoire.json>`.

.. literalinclude:: ../examples/queries/facets1_repertoire.json
  :language: JSON

Sending this query in an API request.

.. code-block:: bash

  curl --data @facets1_repertoire.json https://vdjserver.org/airr/v1/repertoire

The output from the request is similar to normal queries except the data is
provided with the `Facet` key.

.. code-block:: json

  {
    "Info": {
      "title": "AIRR Data Commons API reference implementation",
      "description": "API response for repertoire query",
      "version": 1.3,
      "contact": {
        "name": "AIRR Community",
        "url": "https://github.com/airr-community"
      }
    },
    "Facet": [
      {"sample.pcr_target.pcr_target_locus":[["TRB"]],"count":40},
      {"sample.pcr_target.pcr_target_locus":[["IGH"]],"count":20}
    ]
  }

Here is a query with both ``filters`` and ``facets`` parameters, which restricts
the data records used for the facets count. The content of
the :download:`JSON payload <../examples/queries/facets2_repertoire.json>`.

.. literalinclude:: ../examples/queries/facets2_repertoire.json
  :language: JSON

Sending this query in an API request.

.. code-block:: bash

  curl --data @facets2_repertoire.json https://vdjserver.org/airr/v1/repertoire

Example output from the request. This result indicates there are ten
subjects each with two IGH repertoires.

.. code-block:: json

  {
    "Info": {
      "title": "AIRR Data Commons API reference implementation",
      "description": "API response for repertoire query",
      "version": 1.3,
      "contact": {
        "name": "AIRR Community",
        "url": "https://github.com/airr-community"
      }
    },
    "Facet": [
      {"subject.subject_id":"TW05B","count":2},
      {"subject.subject_id":"TW05A","count":2},
      {"subject.subject_id":"TW03A","count":2},
      {"subject.subject_id":"TW04A","count":2},
      {"subject.subject_id":"TW01A","count":2},
      {"subject.subject_id":"TW04B","count":2},
      {"subject.subject_id":"TW02A","count":2},
      {"subject.subject_id":"TW03B","count":2},
      {"subject.subject_id":"TW01B","count":2},
      {"subject.subject_id":"TW02B","count":2}
    ]
  }

ADC API Limits and Thresholds
-----------------------------

**Repertoire endpoint query fields**

It is expected that the number of repertoires in a data repository will never become so
large such that queries become computationally expensive. A data repository might have
thousands of repertoires across hundreds of studies, yet such numbers are easily handled
by databases. Based upon this, the ADC API does not place limits on the repertoire endpoint
for the fields that can be queried or the operators that can be used.

**Rearrangement endpoint query fields**

Unlike repertoire data, data repositories are expected to store billions of
rearrangement records, where performing “simple” queries can quickly become computationally
expensive. Data repositories are encouraged to optimize their databases for performance.
Therefore, based upon a set of query use cases provided by immunology experts, a minimal
set of required fields was defined that can be queried. These required fields are described
in the following Table. The fields also have the AIRR extension property ``adc-api-optional: false``
in the AIRR Schema.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - rearrangement_id, repertoire_id, sample_processing_id, data_processing_id, clone_id, cell_id, pair_id
      - Identifiers; rearrangement_id allows for query of that specific rearrangement object in the repository, while repertoire_id, sample_processing_id, and data_processing_id are links to the repertoire metadata for the rearrangement. The clone_id, cell_id, and pair_id are all identifiers that group rearrangements based on clone definition, single cell assignment, and paired chain linking.
    * - locus, v_call, d_call, j_call, c_call, productive, junction_aa, junction_aa_length
      - Commonly used rearrangement annotations.

**Repertoire/rearrangement object size**

Any single repertoire or rearrangement object has a maximum that is typically dependent
upon the back-end database which stores the data. For MongoDB-based data repositories, the
largest object size is 16 megabytes.

**Repertoire/rearrangement query size**

For MongoDB-based data repositories, a query is a document thus the query size is limited
to the maximum document size of 16 megabytes.

**Data repository specific limits**

A data repository may provide additional limits. These can be retrieved from the ``info``
endpoint. If the data repository does not provide a limit, then the ADC API default limit or
no limit is assumed.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field
      - Description
    * - ``max_size``
      - The maximum value for the ``size`` query parameter. Attempting to retrieve beyond this maximum may trigger an error or may only return ``max_size`` records based upon the data repository behavior.
    * - ``max_query_size``
      - The maximum size of the JSON query object.


Reference Implementation
--------------------------------

The AIRR Community provides a reference implementation for an ADC API
service with more information found :ref:`here <ADCAPIReference>`.
