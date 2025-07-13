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
*  For those fields that contain Amino Acid or Nucleotide strings, the case for the
   characters (upper or lower case) is not stated in the specification. Repository
   implementations should expect upper or lower case queries for these fields. Repositories
   may want to enforce internal characteristics for these fields (e.g. AA are always upper case,
   nt are always lower case) to facilitate efficient storage and searching. Because case is not
   stated, repositories can return amino acid and nucleotide sequences using the case utilized
   internally.
*  Relevant HTTP error codes should be returned on error conditions. HTTP 408
   (timeout) should be used if the API does not complete an operation because of an
   internal time limit, and HTTP 413 (Content too large) should be returned when either
   max_size or max_query_size are exceeded.
*  Extensions beyond the standard API, e.g., support for the Async API, should be specified
   with the `extensions` property in the `/info` endpoint.

Repository operation principles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Research groups that are running repositories as part of the AIRR Data Commons should,
to the best of their ability, ensure that their repository uptime is maintained and that
repository queries on fields that have the adc_query_support attribute set are completed in a timely manner.

In order to maximize scientific reproducibility and data provenance, it is recommended that 
data stewards/data curators avoid releasing partially loaded data into the AIRR Data Commons. 
When loading a study it is recommended that all data from a specific AIRR Schema object
(e.g. Rearrangement, Clone, Cell) be loaded and then made accessible
in the ADC as a single package, rather than having the repository accessible in the ADC
while the data is being loaded.
Piecemeal data loading of data for a specific schema object (e.g. Rearrangement) for a
study in a production repository will result in queries returning different results as
searches are made over time. This can lead to consumers of the data receiving confusing results,
makes for complicated data provenance, and hampers scientific reproducibility. 

Authentication
~~~~~~~~~~~~~~

The ADC API currently does not define an authentication method. Future
versions of the API may provide an authentication method so data
repositories can support query and download of controlled-access data.

Extensions
~~~~~~~~~~~~~~

Implementation of the ADC API is sufficient for most repositories. However, repositories
may also implement extension APIs that provide additional capability and functionality.

*  Asynchronous API.
*  Statistics API (for future consideration).

Table of Content
----------------

.. toctree::
   :maxdepth: 1

   adc_api_endpoints
   adc_api_requests
   adc_api_limits
   adc_api_reference
   adc_api_async


.. == External links ==

.. _`Genomic Data Commons (GDC) API`: https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/
