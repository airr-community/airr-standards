.. _DataCommonsAPIRequests:

Components of a Request
~~~~~~~~~~~~~~~~~~~~~~~

The ADC API has two classes of endpoints. The endpoints that respond
to ``GET`` requests are simple services that require few or no
parameters. While, the endpoints that response to ``POST`` requests
are the main query services and provide many parameters for specifying
the query as well as the data in the API response.

A typical ``POST`` query request specifies the following parameters:

+ The ``filters`` parameter specifies the query.

+ The ``from`` and ``size`` parameters specify the number of results to skip and the maximum number of results to be returned in the response.

+ The ``fields`` parameter specifies which data elements to be
  returned in the response. By default all fields (AIRR and non-AIRR)
  stored in the data repository are returned. This can vary between
  data repositories based upon how the repository decides to store
  blank or null fields, so the ``fields`` and/or ``include_fields``
  parameter should be used to guarantee the existence of data elements
  in the response.

+ The ``include_fields`` parameter specifies the set of AIRR fields to
  be included in the response. This parameter can be used in
  conjunction with the ``fields`` parameter, in which case the list of
  fields is merged. This is a mechanism to ensure that specific,
  well-defined sets of AIRR data elements are returned without
  requiring all of those fields to be individually provided in the
  ``fields`` parameter.

The sets that can be requested are summarized in the table below.

.. csv-table::
   :header: "include_fields", "MiAIRR", "AIRR required", "AIRR identifiers", "other AIRR/ADC fields"

   "miairr",      "Y","some","N","N"
   "airr-core",   "Y","Y","Y","N"
   "airr-schema", "Y","Y","Y","Y"

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

  curl https://vdjserver.org/airr/v1/info

The response provides various information about the repository itself, the API that is implemented by the repository,
the schema version of the data that is returned from repository queries, as well as repository specific details such
as the maximum number of records that are allowed to be requested in a single query as well as the maximum size (in bytes)
of the queries sent to the repository.

.. code-block:: json

    {
      "title": "api-js-tapis",
      "description": "AIRR Data Commons API for VDJServer Community Data Portal",
      "version": "2.0.0",
      "contact": {
        "name": "VDJServer",
        "url": "http://vdjserver.org/",
        "email": "vdjserver@utsouthwestern.edu"
      },
      "license": {
        "name": "GNU AGPL V3"
      },
      "api": {
        "title": "AIRR Data Commons API",
        "version": "1.0.0",
        "contact": {
          "name": "AIRR Community",
          "url": "http://www.airr-community.org/",
          "email": "join@airr-community.org"
        },
        "description": "Major Version 1 of the Adaptive Immune Receptor Repertoire (AIRR) data repository web service application programming interface (API).\n",
        "license": {
          "name": "Creative Commons Attribution 4.0 International",
          "url": "https://creativecommons.org/licenses/by/4.0/"
        }
      },
      "schema": {
        "title": "AIRR Schema",
        "description": "Schema definitions for AIRR standards objects",
        "version": "1.3",
        "contact": {
          "name": "AIRR Community",
          "url": "https://github.com/airr-community"
        },
        "license": {
          "name": "Creative Commons Attribution 4.0 International",
          "url": "https://creativecommons.org/licenses/by/4.0/"
        }
      },
      "max_size": 1000,
      "max_query_size": 2097152
    }

**Query Repertoire Example**

The following is an example ``POST`` request to the ``repertoire``
endpoint of the ADC API. It queries for repertoires of human TCR beta
receptors (``filters``), skips the first 10 results (``from``),
requests 5 results (``size``), and requests only the ``repertoire_id``
field (``fields``).

.. code-block:: bash

  curl --data @query1-2_repertoire.json -H 'content-type: application/json' https://vdjserver.org/airr/v1/repertoire

The content of the :download:`JSON payload <../examples/queries/query1-2_repertoire.json>`.

.. literalinclude:: ../examples/queries/query1-2_repertoire.json
  :language: JSON

The response contains two JSON objects, an Info object that provides information about the API response and a
Repertoire object that contains the list of Repertoires that met the query search criteria. In this case, the query
returns a list of five repertoire identifiers. Note the Info object is based on the info block as specified in
the OpenAPI v2.0 specification.

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
        {"repertoire_id": "5993695857891348971-242ac118-0001-012"},
        {"repertoire_id": "5981154557681996267-242ac118-0001-012"},
        {"repertoire_id": "6018649617881108971-242ac118-0001-012"},
        {"repertoire_id": "5959121371158548971-242ac118-0001-012"},
        {"repertoire_id": "5939278622251028971-242ac118-0001-012"}
    ]
  }


Request Parameters
~~~~~~~~~~~~~~~~~~

The ADC API supports the follow query parameters. These are only
applicable to the query endpoints, i.e. the HTTP ``POST`` endpoints.

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
    * - ``include_fields``
      - null
      - Specifies the set of AIRR fields to be included in the response
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
      - array of string, number, or integer
      - matches a string or number in a list
      - {"op":"in","content":{"field":"subject.strain_name","value":["C57BL/6","BALB/c","NOD"]}}
    * - exclude
      - field, multiple values in a list
      - array of string, number, or integer
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
      - {"op":"or","content":[ |br| {"op":"<","content":{"field":"sample.cell_number","value":1000}}, |br| {"op":"is missing","content":{"field":"sample.tissue"}}, |br| {"op":"exclude","content":{"field":"subject.organism.id","value":["9606","10090"]}} |br| ]}

Note that the ``not`` operator is different from a logical NOT
operator, and the logical NOT is not needed as the other operators
provide negation.

The ``field`` operand specifies a fully qualified property name in the AIRR
Data Model. Fully qualified AIRR properties are either a JSON/YAML base type (``string``, ``number``,
``integer``, or ``boolean``) or an array of one of these base types (some AIRR fields are arrays
e.g. ``study.keywords_study``).
The Fields section below describes the available queryable fields.

The ``value`` operand specifies one or more values when evaluating the
operator for the ``field`` operand.

*Queries Against Arrays*

A number of fields in the AIRR Data Model are arrays, such as
``study.keywords_study`` which is an array of strings or
``subject.diagnosis`` which is an array of ``Diagnosis`` objects. A
query operator on an array field will apply that operator to each
entry in the array to decide if the query filter is satisfied. The
behavior is different for various operators. For operators such as
``=`` and ``in``, the filter behaves like the Boolean ``OR`` over the
array entries, that is if **any** array entry evaluates to true then
the query filter is satisfied. For operators such as ``!=`` and
``exclude``, the filter behaves like the Boolean ``AND`` over the
array entries, that is **all** array entries must evaluate to true for
the query filter to be satisfied.

For complex queries over arrays, it is necessary to compose complex queries into
more than one query. For example consider the following subject:

.. code-block:: bash

  * Subject
    * diagnosis
      (Diagnosis record 1)
        * disease_diagnosis: "rheumatoid arthritis"
        * disease_length: "20 years"
      (Diagnosis record 2)
        * disease_diagnosis: "pancreatic ductal adenocarcinoma"
        * disease_length: "6 months"


If the end result that is required it to find all disease diagnoses of "pancreatic ductal adenocarcinoma"
that have a disease length of over 10 years, searching for ``disease_diagnosis = pancreatic ductal adenocarcinom`` and ``disease_length > 10``
will result in the above Subject being returned, even though the subject has not had pancreatic ductal adenocarcinom for more than 10 years.
This is because there is a diagnosis of pancreatic ductal adenocarcinom and a disease length
of more than 10 years but from a different diagnoses. This is a correct response to the query, but does not return the desired outcome.

In order to achieve the desired outcome, it is necessary to search for one of the conditions (e.g. ``disease_diagnosis = pancreatic ductal adenocarcinom``),
compile a list of ``repertoire_ids`` that meet that condition, and then search for the second condition (e.g. ``disease_length > 10``)
across those ``repertoire_ids``.

*Examples*

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

Specifies the format of the API response. ``json`` is the default
format and is available for all endpoints. The ``rearrangement``
``POST`` endpoint also accepts ``tsv`` which will provide the data in
the :ref:`AIRR TSV <TSVSpecification>` format. A specific ordering of
fields in the TSV format should not be assumed from one API request to
another. Take care to properly merge AIRR TSV data from multiple API
requests, e.g. such as with the ``airr-tools merge`` program.

**Fields Query Parameter**

The ``fields`` parameter specifies which fields are to be included in
the API response. By default all fields (AIRR and non-AIRR) stored in
the data repository are returned. However, this can vary between data
repositories based upon how the repository decides to store blank or
null fields, so the ``fields`` and/or ``include_fields`` parameter
should be used to guarantee the existence of data elements in the
response.

**Include Fields Query Parameter**

The ``include_fields`` parameter specifies that the API response
should include a well-defined set of AIRR Standard fields. These sets
include:

+ ``miairr``, for only the MiAIRR fields.

+ ``airr-core``, for the AIRR required and identifier fields. This is
  expected to be the most common option as it provides all MiAIRR
  fields, additional required fields useful for analysis, and all
  identifier fields for linking objects in the AIRR Data Model.

+ ``airr-schema``, for all AIRR fields in the AIRR Schema.

The ``include_fields`` parameter is a mechanism to ensure that
specific AIRR data elements are returned without requiring those
fields to be individually provided with the ``fields`` parameter. Any
data elements that lack a value will be assigned ``null`` in the
response. Any empty array of objects, for example
``subject.diagnosis``, will be populated with a single object with all
of the object's properties given a null value. Any empty array of
primitive data types, like string or number, will be assigned
``null``. Note that if both the ``include_fields`` and the ``fields``
parameter are provided, the API response will include the set of AIRR
fields and in addition will include any additional fields that are
specified in the ``fields`` parameter.

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

The ``facets`` parameter provides aggregate count information for the
specified field. Only a single field can be specified. The ``facets``
parameter can be used in conjunction with the ``filters`` parameter to
get aggregate counts for a set of search results. It returns the set
of values for the field, and the number of records (repertoires or
rearrangement) that have this value. For field values that have no
counts, the API service can either return the field value with a 0
count or exclude the field value in the aggregation.  The typical use
of this parameter is for displaying aggregate information in a
graphical user interface.


Here is a simple query with only the ``facets`` parameter to return
the set of values for ``sample.pcr_target.pcr_target_locus`` and the
count of repertoires repertoires that have each value. The content of
the :download:`JSON payload <../examples/queries/facets1_repertoire.json>`.

.. literalinclude:: ../examples/queries/facets1_repertoire.json
  :language: JSON

Sending this query in an API request.

.. code-block:: bash

  curl --data @facets1_repertoire.json -H 'content-type: application/json' https://vdjserver.org/airr/v1/repertoire

The output from the request is similar to normal queries except the data is
provided with the `Facet` key.

.. code-block:: json

    {
      "Info": {
        "title": "AIRR Data Commons API for VDJServer Community Data Portal",
        "description": "VDJServer ADC API response for repertoire query",
        "version": "1.3",
        "contact": {
          "name": "VDJServer",
          "url": "http://vdjserver.org/",
          "email": "vdjserver@utsouthwestern.edu"
        }
      },
      "Facet": [
        {
          "sample.pcr_target.pcr_target_locus": "TRB",
          "count": 2786
        },
        {
          "sample.pcr_target.pcr_target_locus": "TRA",
          "count": 242
        },
        {
          "sample.pcr_target.pcr_target_locus": "IGK",
          "count": 122
        },
        {
          "sample.pcr_target.pcr_target_locus": "IGH",
          "count": 547
        },
        {
          "sample.pcr_target.pcr_target_locus": "IGL",
          "count": 121
        }
      ]
    }

Here is a query with both ``filters`` and ``facets`` parameters, which restricts
the data records used for the facets count. The content of
the :download:`JSON payload <../examples/queries/facets2_repertoire.json>`.

.. literalinclude:: ../examples/queries/facets2_repertoire.json
  :language: JSON

Sending this query in an API request.

.. code-block:: bash

  curl --data @facets2_repertoire.json -H 'content-type: application/json' https://vdjserver.org/airr/v1/repertoire

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

Note: ADC API facet requests differ from those in the GDC API on which the ADC API is based. In the ADC
API it is allowed to request a facet count on a field that is being filtered, whereas in the GDC API
filters on the facet'ed field are ignored (see `Genomic Data Commons (GDC) API Facets`_ restriction #2).

Queries on Nested Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As stated above, in general API response data will be have been
flattened by the query handler. However, there are several instances in
which properties within the top-level entities are arrays of objects,
which cannot be flattened because all the information will be expected
to present in the response. Therefore, in these cases, the data that is
queried and potentially returned will be nested. In addition, while the
array of object is obvious from the AIRR Schema, they array component
does **not** appear in the hierarchical property names used by the API.
Note that this does not create any collisions as the schema allows the
existence of multiple properties with the same designation.

However, it results in two possible ways how an ``AND`` operator can
behave when using such nested properties as input. These are defined as
follows:

Given that two or more instances of an object class exists within an
array that is a property of a higher-level entity, and given a query
that contains an AND operation that uses tests on two or more properties
of said object class as an input, the code handling the query will
exhibit

*  *local* behavior, if for the ``AND`` operation to evaluate to
   ``TRUE`` it requires that all tests must succeed within an instance
   of the object and within at least one object of the array, i.e., the
   code is aware of the nesting and is able to parse the hierarchy of
   properties from the provided string, or
*  *global* behavior, if for the ``AND`` operation to evaluate to
   ``TRUE`` it requires all tests to succeed, but independent of the
   instances in which the matching properties are located, i.e., the
   code is agnostic to the nesting and treats all properties within the
   array as a single set.

While both behaviors have their use cases, ADC API handlers are expected
to exhibit "local" behavior, as is easier to implement on the
client-side, where it would require joining the the result sets of the
queries for each of the properties individually.


.. _`Genomic Data Commons (GDC) API Facets`: https://docs.gdc.cancer.gov/API/Users_Guide/Search_and_Retrieval/#facets
