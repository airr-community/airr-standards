.. _DataCommonsAPIEndpoints:

API Endpoints
-------------

The ADC API is versioned with the version number (``v1``) as part of the
base path for all endpoints. The ADC API provides a query endpoint for each of
the primary, high-level objects in the AIRR Standard to retrieve AIRR-seq related data
about that type of object. The ``repertoire`` endpoint allows querying
upon any field in the :ref:`Repertoire schema
<RepertoireSchema>` including study, subject, sample, cell
processing, nucleic acid processing, sequencing run, raw sequencing
files, and data processing information. Queries on the content of raw
sequencing files is not support but is supported on file attributes
such as name, type and read information. Queries on other objects such
as ``Rearrangement``, ``Clone``, ``Cell``, ``CellExpression``, ``CellReactivity``, and ``Receptor``,
are provide respectively by the ``rearrangement``,
``clone``, ``cell``, ``expression``, ``reactivity``, and ``receptor`` endpoints.

The standard workflow to retrieve all of the data for an AIRR-seq
study involves performing a query on the ``repertoire`` endpoint to
retrieve the repertoires in the study, and one or more queries on the
other object endpoints (e.g. ``rearrangement``) to download the data
of that type for each repertoire. The endpoints are designed so the API
response can be saved directly into a file and be used by AIRR
analysis tools, including the AIRR python and R reference libraries,
without requiring modifications or transformation of the data.

Each ADC API endpoint provides specific functionality as summarized in the
following table:

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
    * - ``/v1/reactivity/{cell_reactivity_id}``
      - Retrieve a CellReactivity given its ``cell_reactivity_id``
      - ``GET``
      - Upon success, returns the ``CellReactivity`` information in JSON format according to the :ref:`CellReactivity schema <CellReactivitySchema>`.
    * - ``/v1/reactivity``
      - Query CellReactivity properties
      - ``POST``
      - Upon success, returns a list of ``CellReactivity`` objects in JSON format according to the :ref:`CellReactivity schema <CellReactivitySchema>`.

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
    "reactivity_measurements": [ "61fc6c454f24ed3af5456a54" ],
    "repertoire_id": "PRJCA002413-ERS1-CELL",
    "data_processing_id": "PRJCA002413-ERS1",
    "expression_study_method": "single-cell transcriptome",
    "expression_raw_doi": null,
    "expression_index": null,
    "virtual_pairing": false
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
    "value": 1
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

**CellReactivity Endpoint**

The ``reactivity`` endpoint provides access to all fields in the
:ref:`CellReactivitySchema`. There are two type of endpoints: One for
retrieving a single reactivity object given its identifier, and another for
performing a query across all cell reactivity in the data repository.

To allow data repositories to optimize their databases for performance,
the ADC API does not require that all fields in the ``CellReactivity`` object
to be queryable and only a limited set of query capabilities must be
supported. The queryable fields are described in the Fields section
below.

*Retrieve CellReactivity data*

Given a ``cell_reactivity_id``, a single ``CellReactivity`` object will be returned.

.. code-block:: bash

  curl https://covid19-1.ireceptor.org/airr/v1/reactivity/{cell_reactivity_id}

Where ``cell_reactivity_id`` is the ID of a ``CellReactivity`` object in the
repository. The response will provide the object in JSON format.

.. code-block:: json

  {"Info": {
    "title": "airr-api-ireceptor",
    "description": "AIRR Data Commons API for iReceptor",
    "version": "4.0",
    "last_update": null,
    "contact": {
        "name": "iReceptor",
        "url": "http://www.ireceptor.org",
        "email": "support@ireceptor.org"
    }
  }, "CellReactivity": [
    {
      "cell_reactivity_id": "61fc6c454f24ed3af5456a54",
      "ligand_type" : "MHC:peptide",
      "antigen_type" : "peptide",
      "antigen" : { "id" : "NCBI:YP_009725307.1", "label" : "RNA-dependent RNA polymerase (nsp12)"},
      "antigen_source_species" : { "id" : "NCBITAXON:2697049", "label" : "Severe acute respiratory syndrome coronavirus 2"},
      "peptide_start" : 738,
      "peptide_end" : 746,
      "peptide_sequence_aa" : "DTDFVNEFY",
      "mhc_class" : "MHC-I",
      "mhc_gene_1	id:" : "MRO:0000046, label: HLA-A",
      "mhc_allele_1" : "HLA-A*01:01",
      "reactivity_method" : "dextramer barcoding",
      "reactivity_readout" : "barcode count",
      "reactivity_value" : 23,
      "reactivity_unit" : "absolute count"
    }]
  }

*Query against all CellReactivity data*

This example queries for receptor reactivity data that has a ``peptide_sequence_aa`` of ``DTDFVNEFY`` and
requests only a single object of that type (``"size":1``). The resultant
data is provided in JSON format and would be similar to that provided
by the cell reactivity query response given above.

.. code-block:: bash

  curl -d '{"filters":{"op":"=","content":{"field":"peptide_sequence_aa","value":"DTDFVNEFY"}},"size":1}' -H 'content-type: application/json' http://covid19-1.ireceptor.org/airr/v1/reactivity


**Receptor Endpoint**

The ``receptor`` endpoint provides access to all fields in the
:ref:`ReceptorSchema`. There are two type of endpoints: One for
retrieving a single receptor given its identifier, and another for
performing a query across all receptors in the data repository.

To allow data repositories to optimize their databases for performance,
the ADC API does not require that all fields in the ``Receptor`` object
to be queryable and only a limited set of query capabilities must be
supported. The queryable fields are described in the Fields section
below.

*Retrieve a Receptor*

Given a ``receptor_id``, a single ``Receptor`` object will be returned.

.. code-block:: bash

  curl https://covid19-1.ireceptor.org/airr/v1/receptor/{receptor_id}

Where ``receptor_id`` is the ID of a ``Receptor`` object in the
repository. The response will provide the object in JSON format.

.. code-block:: json

  {"Info": {
    "title": "airr-api-ireceptor",
    "description": "AIRR Data Commons API for iReceptor",
    "version": "3.0",
    "last_update": null,
    "contact": {
        "name": "iReceptor",
        "url": "http://www.ireceptor.org",
        "email": "support@ireceptor.org"
    }
  }, "Receptor": [
    {
      "receptor_id": "IG-MM-BALB-123456",
      "receptor_hash": "aa1c4b77a6f4927611ab39f5267415beaa0ba07a952c233d803b07e52261f026",
      "receptor_type": "Ig",
      "receptor_variable_domain_1_aa": "QVQLQQPGAELVKPGASVKLSCKASGYTFTSYWMHWVKQRPGRGLEWIGRIDPNSGGTKYNEKFKSKATLTVDKPSSTAYMQLSSLTSEDSAVYYCARYDYYGSSYFDYWGQGTTLTVSS",
      "receptor_variable_domain_1_locus": "IGH",
      "receptor_variable_domain_2_aa": "QAVVTQESALTTSPGETVTLTCRSSTGAVTTSNYANWVQEKPDHLFTGLIGGTNNRAPGVPARFSGSLIGDKAALTITGAQTEDEAIYFCALWYSNHWVFGGGTKLTVL",
      "receptor_variable_domain_2_locus": "IGL",
      "receptor_ref": [ "IEDB_RECEPTOR:29263" ],
      "reactivity_measurements": [ "61fc6c454f24ed3af5456a54" ]
    }
  ]}

*Query against all Receptor data*

This example queries for receptor data that has a TCR receptor type and
requests only a single object response (``"size":1``). The resultant
data is provided in JSON format and would be similar to that provided
by the single expression property query given above.

.. code-block:: bash

  curl -d '{"filters":{"op":"=","content":{"field":"receptor_type","value":"TCR"}},"size":1}' -H 'content-type: application/json' http://covid19-1.ireceptor.org/airr/v1/receptor

