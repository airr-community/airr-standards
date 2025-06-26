.. _DataCommonsAsyncAPI:

Asynchronous API
================

The ADC API is a synchronous API, which means that a query is executed
immediately and all data satisfying the query is returned in the
response, regardless of the length of time to execute the query and the
amount of data returned in the response. The network connection between
the client and server is maintained until the request is complete.

Repositories may wish to have better control over queries that either
take a long time to run or which return large amounts of data. Partial
control is provided by utilizing the `max_size` limit, which restricts
the amount of data returned; however, there is nothing to restrict the
number of concurrent queries nor how long an individual query can run.
For network services with time restrictions, this can cause timeouts as
the client/server connection is cut if queries take too long.

The ADC Asynchronous API is an extension that repositories may implement
which provides control over query execution. Queries are performed
asynchronously, which means that incoming query requests return
immediately with a status record, queries are executed in the future by
the repository, and the status record is updated when the query is
complete and the data is ready.

Currently only the ``rearrangement`` endpoint is required, but other
endpoints may be added in future versions. The Async API mirrors the ADC
API with the query parameters that are accepted with the exception of
``facets`` (this may be added in future versions).

Repositories should assign a unique ``query_id`` for every incoming
query request, which will allow the status of the query to be tracked.
Requests may specify a URL for notifications as the query status
changes; however, notifications do not have guaranteed delivery so
client programs should utilize polling as a backup. Repositories should
update the query status and send out notifications, as the query goes
through various processing stages. The current statuses that repositories
must support are listed below.

*  PENDING: A query which has been received but not yet completely accepted for submission.
   The repository may perform additional error checks before accepting the query.
*  SUBMITTED: A query that has passed any initial error checks and is submitted to be executed.
*  PROCESSING: A query that is currently being processed.
*  FINISHED: A query that has finished and data is available.
*  ERROR: A query where an error occurred that prevents completion.
*  EXPIRED: A query that has finished but has expired and the data is no longer available.

When a query is FINISHED, the data should be made available with a download URL. The
download does not have to be through the same API service, which allows repositories to
utilize services that are more efficient at downloading large data files.

Async API Endpoints
-------------------

The ADC Async API is versioned with the major version number (``v1``) as
part of the base path (``/airr/async/v1``) for all endpoints. Each endpoint provides specific
functionality as summarized in the following table:

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
    * - ``/v1/rearrangement``
      - Query rearrangements asynchronously
      - ``POST``
      - Upon success, returns a query status object with a unique ``query_id``.
    * - ``/v1/status/{query_id}``
      - Retrieve query status given its ``query_id``
      - ``GET``
      - Upon success, returns the query status information.

Request Asynchronous Query on Rearrangements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``rearrangement`` endpoint provides access to all fields in
the :ref:`Rearrangement schema <RearrangementSchema>`. Unlike
the ADC API which limits the set of queryable fields, any field
can be included in an asynchronous query.

This example queries for rearrangements with a specific junction amino
acid sequence among a set of repertoires. This is the exact same query
that can be sent to the synchronous ADC API.

.. code-block:: bash

  curl --data @query1_rearrangement.json -H 'content-type: application/json' https://vdjserver.org/airr/async/v1/rearrangement

The content of the :download:`JSON payload <../examples/queries/query1_rearrangement.json>`.

.. literalinclude:: ../examples/queries/query1_rearrangement.json
  :language: JSON

Here is an example response with the unique ``query_id``.

.. code-block:: json

    {
      "message":"rearrangement lrq submitted.",
      "query_id":"1978706891589873170-242ac118-0001-012"
    }

Retrieve Status of an Asynchronous Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The status of an asynchronous query can be retrieved at any time by
sending a request with the ``query_id``. Here is an example using the
``query_id`` from the above request.

.. code-block:: bash

  curl https://vdjserver.org/airr/async/v1/status/1978706891589873170-242ac118-0001-012

Here is an example response:

.. code-block:: json

    {
      "query_id":"1978706891589873170-242ac118-0001-012",
      "endpoint":"rearrangement",
      "status":"FINISHED",
      "message":null,
      "created":"2024-02-25T16:19:07.801-06:00",
      "estimated_count":10,
      "final_file":"1978706891589873170-242ac118-0001-012.airr.tsv",
      "download_url":"https://vdj-agave-api.tacc.utexas.edu/postits/v2/f8d52cdb-9234-41e3-a908-95c9034a3360-010"
    }

Retrieve Data for an Asynchronous Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a query is FINISHED, the ``download_url`` field will provide the
URL for retrieving the data. The ``final_file`` field is a repository
assigned file name, usually made unique in some way by using the
``query_id``, that is provided for convenience, but clients are allowed
to use whatever filename they wish. Here is an example to download the
data for above query.

.. code-block:: bash

  curl -o 1978706891589873170-242ac118-0001-012.airr.tsv https://vdj-agave-api.tacc.utexas.edu/postits/v2/f8d52cdb-9234-41e3-a908-95c9034a3360-010

Request Notifications for Query Status Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The client can request that a URL be called by the repository whenever
the status of a query changes. This can only be done with the initial
query request. A notification object is provided with the initial query
request that specifies the URL to be called, whether the GET or POST
method is used, and what status changes to receive. This object is
provided with the ``notification`` parameter. Here is the above example
query request where a notification URL has been added.

.. code-block:: json

    {
        "filters":{
            "op":"and",
            "content": [
                {
                    "op":"in",
                    "content": {
                        "field":"repertoire_id",
                        "value":[
                            "2603354229190496746-242ac113-0001-012",
                            "2618085967015776746-242ac113-0001-012",
                            "2633633748627296746-242ac113-0001-012",
                            "2564613624180576746-242ac113-0001-012"
                        ]
                    }
                },
                {
                    "op":"=",
                    "content": {
                        "field":"junction_aa",
                        "value":"CARDPRSYHAFDIW"
                    }
                }
            ]
        },
        "fields":["repertoire_id","sequence_id","v_call","productive"],
        "format":"tsv",
        "notification":{
            "url"": "https://notify.example.com",
            "method": "POST"
        }
    }

When sending a notification, the repository will call the URL using requested method and
provide data with information about the query status change. This data is exactly the
same as what is returned by the ``status`` endpoint.

