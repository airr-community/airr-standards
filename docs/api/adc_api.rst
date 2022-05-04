.. _DataCommonsAPI:

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
    * - ``/v1/repertoire/{repertoire_id}``
      - Retrieve a repertoire given its ``repertoire_id``
      - ``GET``
      - Upon success, returns the ``Repertoire`` information in JSON according to the :ref:`Repertoire schema <RepertoireSchema>`.
    * - ``/v1/repertoire``
      - Query repertoires
      - ``POST``
      - Upon success, returns a list of ``Repertoires`` in JSON according to the :ref:`Repertoire schema <RepertoireSchema>`.
    * - ``/v1/rearrangement/{sequence_id}``
      - Retrieve a rearrangement given its ``sequence_id``
      - ``GET``
      - Upon success, returns the ``Rearrangement`` information in JSON format according to the :ref:`Rearrangement schema <RearrangementSchema>`.
    * - ``/v1/rearrangement``
      - Query rearrangements
      - ``POST``
      - Upon success, returns a list of ``Rearrangements`` in JSON or AIRR TSV format according to the :ref:`Rearrangement schema <RearrangementSchema>`.
    * - ``/v1/clone/{clone_id}``
      - Retrieve a Clone given its ``clone_id``
      - ``GET``
      - Upon success, returns the ``Clone`` information in JSON format according to the :ref:`Clone schema <CloneSchema>`.
    * - ``/v1/clone``
      - Query clones
      - ``POST``
      - Upon success, returns a list of ``Clones`` in JSON format according to the :ref:`Clone schema <CloneSchema>`. 
    * - ``/v1/cell/{cell_id}``
      - Retrieve a Cell given its ``cell_id``
      - ``GET``
      - Upon success, returns the ``Cell`` information in JSON format according to the :ref:`Cell schema <CellSchema>`.
    * - ``/v1/cell``
      - Query cells
      - ``POST``
      - Upon success, returns a list of ``Cells`` in JSON format according to the :ref:`Cell schema <CellSchema>`. 
    * - ``/v1/expression/{expression_id}``
      - Retrieve a Expression Property given its ``expression_id``
      - ``GET``
      - Upon success, returns the ``Expression`` information in JSON format according to the :ref:`CellExpression schema <CellExpressionSchema>`.
    * - ``/v1/expression``
      - Query Cell Expression properties
      - ``POST``
      - Upon success, returns a list of ``Expression Properties`` in JSON format according to the :ref:`CellExperssion schema <CellExpressionSchema>`. 
    * - ``/v1/receptor/{receptor_id}``
      - Retrieve a Receptor given its ``receptor_id``
      - ``GET``
      - Upon success, returns the ``Receptor`` information in JSON format according to the :ref:`Receptor schema <ReceptorSchema>`.
    * - ``/v1/receptor``
      - Query Receptor properties
      - ``POST``
      - Upon success, returns a list of ``Receptors`` in JSON format according to the :ref:`Receptor schema <ReceptorSchema>`. 

**Authentication**

The ADC API currently does not define an authentication
method. Future versions of the API will provide an authentication
method so data repositories can support query and download of
controlled-access data.

Search and Retrieval
--------------------

The AIRR Data Commons API specifies endpoints for searching and
retrieving AIRR-seq data sets stored in an AIRR-compliant Data
Repository according to the AIRR Data Model. This documentation
describes Version 1 of the API. The general format of requests
and associated parameters are described below.

The design of the AIRR Data Commons API was greatly inspired by
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
   :header: "include_fields", "MiAIRR", "AIRR required", "AIRR identifiers", "other AIRR fields"

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

The response provides various information.

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

  curl https://vdjserver.org/airr/v1/repertoire/5993695857891348971-242ac118-0001-012

The response will provide the ``Repertoire`` data in JSON format.

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
      "Repertoire": [
        {
          "repertoire_id": "5993695857891348971-242ac118-0001-012",
          "repertoire_name": null,
          "repertoire_description": null,
          "study": {
            "study_id": "4995411523885404651-242ac118-0001-012",
            "study_title": "T cell Receptor Repertoires Acquired via Routine Pap Testing May Help Refine Cervical Cancer and Precancer Risk Estimates",
            "study_type": {
              "id": "NCIT:C16084",
              "label": "Observational Study"
            },
            "study_description": "Cervical cancer is the fourth most common cancer and fourth leading cause of cancer death among women worldwide. In low Human Development Index settings, it ranks second. Screening and surveillance involve the cytology-based Papanicolaou (Pap) test and testing for high-risk human papillomavirus (hrHPV). The Pap test has low sensitivity to detect precursor lesions, while a single hrHPV test cannot distinguish a persistent infection from one that the immune system will naturally clear. Furthermore, among women who are hrHPV-positive and progress to high-grade cervical lesions, testing cannot identify the ~20% who would progress to cancer if not treated. Thus, reliable detection and treatment of cancers and precancers requires routine screening followed by frequent surveillance among those with past abnormal or positive results. The consequence is overtreatment, with its associated risks and complications, in screened populations and an increased risk of cancer in under-screened populations. Methods to improve cervical cancer risk assessment, particularly assays to predict regression of precursor lesions or clearance of hrHPV infection, would benefit both populations. Here we show that women who have lower risk results on follow-up testing relative to index testing have evidence of enhanced T cell clonal expansion in the index cervical cytology sample compared to women who persist with higher risk results from index to follow-up. We further show that a machine learning classifier based on the index sample T cells predicts this transition to lower risk with 95% accuracy (19/20) by leave-one-out cross-validation. Using T cell receptor deep sequencing and machine learning, we identified a biophysicochemical motif in the complementarity-determining region 3 of T cell receptor β chains whose presence predicts this transition. While these results must still be tested on an independent cohort in a prospective study, they suggest that this approach could improve cervical cancer screening by helping distinguish women likely to spontaneously regress from those at elevated risk of progression to cancer. The advancement of such a strategy could reduce surveillance frequency and overtreatment in screened populations and improve the delivery of screening to under-screened populations.",
            "inclusion_exclusion_criteria": "We included samples from White Hispanic women age 18 years or older. We excluded women who were HIV+, pregnant, had an intrauterine device, or had a sexually transmitted disease at the time of sample collection. We obtained samples across all cytology result categories: Negative for Intraepithelial Lesion or Malignancy (NILM, Normal), Abnormal Squamous Cells of Undetermined Significance (ASCUS), Low-grade Squamous Intraepithelial Lesion (LSIL), and High-grade Squamous Intraepithelial Lesion (HSIL). At Parkland Health and Hospital System (PHHS), the primary screening strategy is cytology alone with a reflex hrHPV test for women with an ASCUS cytology result. The test assays for positivity across 14 HPV types, and the ASCUS result category is divided into ASCUS/HPV- (negative for all 14 types) and ASCUS/HPV+ (positive for at least one type). An additional exclusion criterion was applied to women with a result of Normal, ASCUS/HPV-, and ASCUS/HPV+, and that is they were excluded if they had previously had cervical cancer or previous treatment of cervical pre-cancerous lesions.\n\nWe applied these inclusion and exclusion criteria in a quota sampling scheme to ensure adequate representation of women across all five result categories. We targeted a minimum of 100 samples total with a minimum of 15 samples in each category, and then rescued all samples meeting our criteria each week until all minimums were reached.",
            "lab_name": "Lindsay G. Cowell",
            "lab_address": "UT Southwestern Medical Center",
            "submitted_by": "Scott Christley, scott.christley@utsouthwestern.edu, UT Southwestern Medical Center",
            "grants": "This research was supported by Simmons Comprehensive Cancer Center Development Funds and by a charitable donation from Young Texans Against Cancer, both to LC and JT.",
            "pub_ids": "PMID: 33868241",
            "keywords_study": [
              "contains_tcr"
            ],
            "adc_publish_date": "2021-08-05T03:50:02.295Z",
            "adc_update_date": "2021-08-05T05:43:14.260Z",
            "collected_by": null
          },
          "subject": {
            "subject_id": "5_20",
            "synthetic": false,
            "species": {
              "id": "NCBITAXON:9606",
              "label": "Homo sapiens"
            },
            "sex": "female",
            "age_min": 49.1,
            "age_max": 49.1,
            "age_unit": {
              "id": "UO:0000036",
              "label": "year"
            },
            "ethnicity": "Hispanic",
            "race": "White",
            "diagnosis": [
              {
                "disease_diagnosis": {
                  "id": null,
                  "label": null
                },
                "study_group_description": null,
                "disease_length": null,
                "disease_stage": null,
                "prior_therapies": null,
                "immunogen": null,
                "intervention": null,
                "medical_history": null
              }
            ],
            "age_event": null,
            "ancestry_population": null,
            "strain_name": null,
            "linked_subjects": null,
            "link_type": null
          },
          "sample": [
            {
              "sample_id": "5_20_DNA",
              "sample_type": "cytology",
              "tissue": {
                "id": "UBERON:0004801",
                "label": "cervix epithelium"
              },
              "anatomic_site": "cervix",
              "disease_state_sample": "hsil",
              "cell_species": {
                "id": null,
                "label": null
              },
              "single_cell": false,
              "cell_storage": false,
              "template_class": "DNA",
              "template_amount": "2ug",
              "library_generation_method": "PCR",
              "library_generation_protocol": "Adaptive Biotechnologies",
              "library_generation_kit_version": "v3",
              "pcr_target": [
                {
                  "pcr_target_locus": "TRB",
                  "forward_pcr_primer_target_location": null,
                  "reverse_pcr_primer_target_location": null
                }
              ],
              "complete_sequences": "partial",
              "physical_linkage": "none",
              "sequencing_run_id": "UTSW-Monson-P02-04",
              "sequencing_run_date": "11/16/17",
              "sequencing_files": {
                "file_type": "fasta",
                "filename": "5-20_DNA.fasta",
                "read_direction": "forward",
                "read_length": null,
                "paired_filename": null,
                "paired_read_direction": null,
                "paired_read_length": null
              },
              "sample_processing_id": null,
              "collection_time_point_relative": null,
              "collection_time_point_reference": null,
              "biomaterial_provider": null,
              "tissue_processing": null,
              "cell_subset": {
                "id": null,
                "label": null
              },
              "cell_phenotype": null,
              "cell_number": null,
              "cells_per_reaction": null,
              "cell_quality": null,
              "cell_isolation": null,
              "cell_processing_protocol": null,
              "template_quality": null,
              "total_reads_passing_qc_filter": null,
              "sequencing_platform": null,
              "sequencing_facility": null,
              "sequencing_kit": null
            }
          ],
          "data_processing": [
            {
              "data_processing_id": "bf0617e7-b4a4-480f-99e3-b53eef9ca6d4-007",
              "primary_annotation": true,
              "software_versions": "igblast-ls5-1.14u2",
              "data_processing_files": [
                "5-20_DNA.igblast.airr.tsv.gz"
              ],
              "germline_database": "VDJServer IMGT 2019.01.23",
              "paired_reads_assembly": null,
              "quality_thresholds": null,
              "primer_match_cutoffs": null,
              "collapsing_method": null,
              "data_processing_protocols": null,
              "analysis_provenance_id": null
            }
          ]
        }
      ]
    }


*Query against all Repertoires*

A query in JSON format is passed in a ``POST`` request. This example queries for
repertoires of human IG heavy chain receptors for all studies in the data repository.

.. code-block:: bash

  curl --data @query2_repertoire.json -H 'content-type: application/json' https://vdjserver.org/airr/v1/repertoire

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

Given a ``sequence_id``, a single ``Rearrangement`` object will
be returned.

.. code-block:: bash

  curl https://vdjserver.org/airr/v1/rearrangement/610b77f6d5812c007f79bba3

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
        "sequence_id":"610b77f6d5812c007f79bba3",
        "repertoire_id":"5993695857891348971-242ac118-0001-012",
        "data_processing_id": "bf0617e7-b4a4-480f-99e3-b53eef9ca6d4-007",

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
requested in JSON or :ref:`AIRR TSV <TSVSpecification>` format.

.. code-block:: bash

  curl --data @query1_rearrangement.json -H 'content-type: application/json' https://vdjserver.org/airr/v1/rearrangement

The content of the :download:`JSON payload <../examples/queries/query1_rearrangement.json>`.

.. literalinclude:: ../examples/queries/query1_rearrangement.json
  :language: JSON

Here is the response in AIRR TSV format.

.. code-block:: text

    sequence_id	productive	v_call	repertoire_id
    5f70b421e10383007e3038ad	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e3038c2	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e3038f0	true	IGHV1-69*10	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e3039ec	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e303a1b	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e303a22	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e303a23	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e303a47	true	IGHV1-24*01	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e303b00	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012
    5f70b421e10383007e303baf	true	IGHV1-69*04	2564613624180576746-242ac113-0001-012

**Clone Endpoint**

The ``clone`` endpoint provides access to all fields in
the :ref:`Clone schema <CloneSchema>`. There are two
type of endpoints; one for retrieving a single clone given its
identifier, and another for performing a query across all
clones in the data repository.

Unlike repertoire data, data repositories are expected to store
millions or billions of clone records, where performing
"simple" queries can quickly become computationally expensive. Data
repositories will need to optimize their databases for
performance. Therefore, the ADC API does not require that all fields
be queryable and only a limited set of query capabilities must be
supported. The queryable fields are described in the Fields section
below.

*Retrieve a Single Clone*

Given a ``clone_id``, a single ``Clone`` object will
be returned.

.. code-block:: bash

  curl https://covid19-1.ireceptor.org/airr/v1/clone/{clone_id}

Where clone_id is the ID of a clone object in the repository. The response will provide the ``Clone`` data in JSON format.

.. code-block:: json

    {
      "Info":
      {
        "title": "airr-api-ireceptor",
        "description": "AIRR Data Commons API for iReceptor",
        "version": "3.0",
        "last_update": null,
        "contact": {
            "name": "iReceptor",
            "url": "http://www.ireceptor.org",
            "email": "support@ireceptor.org"
        }
      }, 
      "Clone":
      [
        {
          "clone_id": "clonotype1",
          "repertoire_id": "PRJCA002413-Healthy_Control_1-IG",
          "data_processing_id": "PRJCA002413-Healthy_Control_1",
          "sequences": null,
          "v_call": "IGHV2-70",
          "d_call": "",
          "j_call": "IGHJ3",
          "junction": "TGCGCACGGGCTCATTGTTCGTGGGGCAGCAGCAGGTTCGGTGCTTTTGATATGTGG",
          "junction_aa": "CARAHCSWGSSRFGAFDMW",
          "junction_length": 57,
          "junction_aa_length": 19,
          "FIELDS REMOVED" : "FOR SPACE"
        }
      ]
    }

*Query against all Clones*

Supplying a ``repertoire_id``, when it is known, should greatly speed
up the query as it can significantly reduce the amount of data to be
searched, though it isn't necessary.

This example queries for clones with a specific junction amino
acid sequence among a set of repertoires. A limited set of fields is
requested to be returned. The resultant data is provided in JSON format.

.. code-block:: bash

  curl -d '{"filters":{"op":"=","content":{"field":"junction_aa","value":"CARAHCSWGSSRFGAFDMW"}},"size":1}' -H 'content-type: application/json' http://covid19-1.ireceptor.org/airr/v1/clone
  
This query searches the repository for clones that have a specific ``junction_aa`` field with a value of ``CARAHCSWGSSRFGAFDMW`` and requests only a
single object in the response (``"size":1``). The response would be similar to that provided by the single clone query given above.

**Cell Endpoint**

The ``cell`` endpoint provides access to all fields in
the :ref:`Cell schema <CellSchema>`. There are two
type of endpoints; one for retrieving a single cell given its
identifier, and another for performing a query across all
cells in the data repository.

Unlike repertoire data, data repositories are expected to store
millions of cell records, where performing
"simple" queries can quickly become computationally expensive. Data
repositories will need to optimize their databases for
performance. Therefore, the ADC API does not require that all fields
be queryable and only a limited set of query capabilities must be
supported. The queryable fields are described in the Fields section
below.

*Retrieve a Single Cell*

Given a ``cell_id``, a single ``Cell`` object will
be returned.

.. code-block:: bash

  curl https://covid19-1.ireceptor.org/airr/v1/cell/{cell_id}

Where cell_id is the ID of a cell object in the repository. The response will provide the ``Cell`` data in JSON format.

.. code-block:: json

 {"Info":{
    "title": "airr-api-ireceptor",
    "description": "AIRR Data Commons API for iReceptor",
    "version": "3.0",
    "last_update": null,
    "contact": {
        "name": "iReceptor",
        "url": "http://www.ireceptor.org",
        "email": "support@ireceptor.org"
    }
  }, "Cell":[
  {
    "cell_id": "AAACCTGCACCGATAT-1",
    "rearrangements": null,
    "receptors": null,
    "repertoire_id": "PRJCA002413-ERS1-CELL",
    "data_processing_id": "PRJCA002413-ERS1",
    "expression_study_method": "single-cell transcriptome",
    "expression_raw_doi": null,
    "expression_index": null,
    "virtual_pairing": false,
  }]}

*Query against all Cells*

Supplying a ``repertoire_id``, when it is known, should greatly speed
up the query as it can significantly reduce the amount of data to be
searched, though it isn't necessary.

This example queries for clones with a specific junction amino
acid sequence among a set of repertoires. A limited set of fields is
requested to be returned. The resultant data is provided in JSON format.

.. code-block:: bash

  curl -d '{"filters":{"op":"=","content":{"field":"repertoire_id","value":"PRJCA002413-ERS1-CELL"}},"size":1}' -H 'content-type: application/json' http://covid19-1.ireceptor.org/airr/v1/cell
  
This query searches the repository for cells that have a specific ``repertoire_id`` field with a value of ``PRJCA002413-ERS1-CELL`` and requests only a
single object in the response (``"size":1``). The response would be similar to that provided by the single cell query given above.

**Expression Endpoint**

The ``expression`` endpoint provides access to all fields in
the :ref:`CellExpression schema <CellExpressionSchema>`. There are two
type of endpoints; one for retrieving a single expression property given its
identifier, and another for performing a query across all
expression properties in the data repository.

Unlike repertoire data, data repositories are expected to store
millions or billions of cell expression records, where performing
"simple" queries can quickly become computationally expensive. Data
repositories will need to optimize their databases for
performance. Therefore, the ADC API does not require that all fields
be queryable and only a limited set of query capabilities must be
supported. The queryable fields are described in the Fields section
below.

*Retrieve a Cell Expression Property*

Given a ``expression_id``, a single ``Expression`` object will
be returned.

.. code-block:: bash

  curl https://covid19-1.ireceptor.org/airr/v1/expression/{expression_id}

Where expression_id is the ID of an expression object in the repository. The response will provide the ``CellExpression`` data in JSON format.

.. code-block:: json

  {"Info":{
    "title": "airr-api-ireceptor",
    "description": "AIRR Data Commons API for iReceptor",
    "version": "3.0",
    "last_update": null,
    "contact": {
        "name": "iReceptor",
        "url": "http://www.ireceptor.org",
        "email": "support@ireceptor.org"
    }
  }, "CellExpression":[
  {
    "expression_id": "61fc6c454f24ed3af5456a54",
    "cell_id": "AAACCTGCAGCTTAAC-1",
    "repertoire_id": "PRJCA002413-Healthy_Control_1-CELL",
    "data_processing_id": "PRJCA002413-Healthy_Control_1",
    "property": {
        "label": "ISG15",
        "id": "ENSG:ENSG00000187608"
    },
    "value": 1,
  }]}

*Query against all Cell Expression data*

Supplying a ``repertoire_id`` or ``cell_id``, when it is known, should greatly speed
up the query as it can significantly reduce the amount of data to be
searched, though it isn't necessary.

This example queries for cell expression data with an ENSEMBL gene ID with the value ``ENSG:ENSG0000017575`` and
requests only a single object response (``"size":1``). The resultant data is provided
in JSON format and would be similar to that provided by the single expression property query given above.

.. code-block:: bash

  curl -d '{"filters":{"op":"=","content":{"field":"property.id","value":"ENSG:ENSG00000175756"}},"size":1}' -H 'content-type: application/json' http://covid19-1.ireceptor.org/airr/v1/expression


**Receptor Endpoint**

The ``receptor`` endpoint provides access to all fields in
the :ref:`Receptor schema <ReceptorSchema>`. There are two
type of endpoints; one for retrieving a single receptor given its
identifier, and another for performing a query across all
receptors in the data repository.

Unlike repertoire data, data repositories are expected to store
millions of receptor records, where performing
"simple" queries can quickly become computationally expensive. Data
repositories will need to optimize their databases for
performance. Therefore, the ADC API does not require that all fields
be queryable and only a limited set of query capabilities must be
supported. The queryable fields are described in the Fields section
below.

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
in the following Table. The fields also have the AIRR extension property ``adc-query-support: true``
in the AIRR Schema.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - sequence_id, repertoire_id, sample_processing_id, data_processing_id, clone_id, cell_id
      - Identifiers; sequence_id allows for query of that specific rearrangement object in the repository, while repertoire_id, sample_processing_id, and data_processing_id are links to the repertoire metadata for the rearrangement. The clone_id and cell_id are identifiers that group rearrangements based on clone assignment and single cell assignment.
    * - locus, v_call, d_call, j_call, c_call, productive, junction_aa, junction_aa_length
      - Commonly used rearrangement annotations.

**Data repository specific limits**

A data repository may impose limits on the size of the data returned. This might be because of limitations imposed by
the back-end database being used or because of the need to manage the load placed on the server. For example, 
MongoDB databases have document size limits (16 megabytes) which limit the size of a query that can be sent to a 
repository and the size of a single repertoire or rearrangement object that is returned. As a result a repository might
choose to set a maximum query size.

Size limits can be retrieved from the ``info`` endpoint. If the data repository does not provide a limit, then no limit is assumed.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field
      - Description
    * - ``max_size``
      - The maximum value for the ``size`` query parameter. Attempting to retrieve data beyond this maximum should trigger an error response. The error response should include information about why the query failed and what the maximum size limit is. 
    * - ``max_query_size``
      - The maximum size of the JSON query object.


Reference Implementation
--------------------------------

The AIRR Community provides a reference implementation for an ADC API
service with more information found :ref:`here <ADCAPIReference>`.
