.. _DataCommonsAPI:

AIRR Data Commons API V1
========================

Note: This section is about the API, if you are looking for information
on the AIRR Data Commons, please see :ref:`here<DataCommons>`.


Overview
--------

The AIRR Data Commons (ADC) API provides programmatic access to
query and download AIRR-seq data. The ADC API uses JSON as its
communication format, and standard HTTP methods like ``GET`` and
``POST``. The ADC API is read-only and the mechanism of inclusion of
AIRR-seq studies into a data repository is left up to the repository.

This documentation explains how to construct and execute API requests
and interpret API responses.


Search and Retrieval
--------------------

The AIRR Data Commons API specifies endpoints for searching and
retrieving AIRR-seq data sets stored in an AIRR-compliant Data
Repository according to the AIRR Data Model. This documentation
describes Version 1 of the API. The general format of requests
and associated parameters are described below.

The design of the AIRR Data Commons API was greatly inspired by
National Cancer Institute's `Genomic Data Commons (GDC) API`_.



Repository implementation principles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementers of the ADC API should follow the following high level
principles. Users of the ADC API can expect the following principles
to be followed.

*  All API endpoints should return JSON encodings as an API response.
*  For some API endpoints it is possible to request TSV files, and
   those endpoints that support TSV files are documented in the
   :ref:`<DataCommonsAPIEndpoints>` section.
*  Endpoints that are not documented as supporting TSV can reject TSV
   requests.
*  If an API endpoint returns a field, then the content of that field
   in the JSON and TSV response must be equivalent.
*  Relevant HTTP error codes should be returned on error conditions. HTTP 408
   (timeout) should be used if the API does not complete an operation because of an
   internal time limit, and HTTP 413 (Content too large) should be returned when either
   max_size or max_query_size are exceeded.

Repository operation principles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Research groups that are running repositories as part of the AIRR Data Commons should,
to the best of their ability, ensure that their repository uptime is maintained and that
repository queries on fields that have the adc_query_support attribute set are completed in a timely manner.

In order to maximize scientific reproducibility and data provenance, it is recommended that 
data stewards/data curators avoid releasing partially loaded data into the AIRR Data Commons. 
When loading a study it is recommended that the entire study be loaded and then made accessible
in the ADC, rather than having the repository accessible in the ADC while the data is being loaded.
Data loading over time can lead to confusion to consumers of the data in the ADC, as queries will 
return different results as data is loaded.

Authentication
~~~~~~~~~~~~~~

The ADC API currently does not define an authentication method. Future
versions of the API may provide an authentication method so data
repositories can support query and download of controlled-access data.


Table of Content
----------------

.. toctree::
   :maxdepth: 1

   adc_api_endpoints
   adc_api_requests
   adc_api_limits
   adc_api_reference


.. == External links ==

.. _`Genomic Data Commons (GDC) API`: https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/
