.. _DataRepresentations:

AIRR Data Representations
=============================

AIRR Data Representations are versioned specifications that consist of
a file format and a well-defined schema. The schema is provided in a
machine-readable YAML document that follows the OpenAPI v2.0
specification. The schema defines the data model, field names, data
types, and encodings for AIRR standard objects. Strict typing enables
interoperability and data sharing between different AIRR-seq analysis
tools and repositories, and some fields use a controlled vocabulary or
an ontology for value restriction. Specification extensions are
utilized to define AIRR-specific attributes.

FAIR Principles
---------------

We desire AIRR standard objects to be FAIR (findable, accessible,
interoperable and reusable) [Wilkinson_2016]_:

+ findable: by giving AIRR standard objects a globally unique identifier

+ accessible: by providing an API where AIRR standard objects can be queried and downloaded

+ interoperable: by defining a OpenAPI schema for the AIRR standard objects

+ reusable: by linking the AIRR standard objects together into a standard formats


AIRR Data Model
---------------

The MiAIRR standard defines the minimal information for submission and
publication of AIRR-seq datasets. The standard defines a set of data
elements for this information and organizes them into six high-level
sets.

+ Study, Subject and Diagnosis

+ Sample Collection

+ Sample Processing and Sequencing

+ Raw Sequences

+ Data Processing

+ Processed Sequences with Annotations

However beyond these sets, MiAIRR does not define any structure, data
model or relationship between the data elements. This provides
flexibility for the information to be stored in various database
repositories but is problematic for interoperability and reusability
of that information by computer programs. The AIRR Data Model
overcomes these issues by defining a schema for the MiAIRR data
elements, structuring them within schema objects, defining the
relationship between those objects, and defining a file format.

Here are the primary schema objects of the AIRR Data Model:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Schema Object
      - Description
    * - ``Study``
      - Information about the experimental study design, including the title of the study, laboratory contact information, funding, and linked publications.
    * - ``Subject``
      - Information about the study cohorts and individual subjects, including species, sex, age, and ancestry.
    * - ``Diagnosis``
      - Information about disease state(s), therapies, and study group membership (e.g., control versus disease).
    * - ``Sample``
      - Information about the origin and expected composition of the biological sample(s). This set aims to capture essential information about the collection of a sample, including its source (e.g., anatomical site), its provenance (provider), and the experimental condition (e.g., the time point during the course of a disease or treatment).
    * - ``CellProcessing``
      - Information about the cell subset being profiled, as defined by the investigator, and the flow cytometry or other markers used to select the subset. Additional information includes the number of cells per sample and whether cells were prepared in bulk or captured as single cells.
    * - ``NucleicAcidProcessing``
      - Information about nucleic acid sample type (e.g., RNA versus DNA) and how immune-receptor gene rearrangements were amplified and sequenced (for example, RACE-PCR versus multiplex PCR, paired PCR, and/or varying read length and sequencing chemistries).
    * - ``SequencingRun``
      - Information about the sequencing run, such as the number of reads, read lengths, quality control parameters, the sequencing kit and instrument(s) used, and run batch number. Also includes information about the raw data for the sequencing run (e.g., FASTQ files).
    * - ``DataProcessing``
      - Information about the data processing to transform the raw sequencing data into ``Rearrangements``.
    * - ``Repertoire``
      - Composite object that combines the schema objects ``Study``, ``Subject``, ``Diagnosis``, ``Sample``, ``CellProcessing``, ``NucleicAcidProcessing``, ``SequencingRun``, and ``DataProcessing``. Each ``Repertoire`` has a unique identifier ``repertoire_id`` for linking with other data files, e.g. ``Rearrangements``. ``Repertoires`` have their own schema and file format described :ref:`here <RepertoireSchema>`.
    * - ``Rearrangments``
      - Annotated sequences describing adaptive immune receptor chains. ``Rearrangements`` have their own schema and file format described :ref:`here <RearrangementSchema>`.
    * - ``Clones``
      - Information about inferred clones from a study. ``Clones`` have their own schema and file format described :ref:`here <CloneSchema>`.
    * - ``Cells``
      - Information about an observed Cell in a study. ``Cells`` have their own schema and file format described :ref:`here <CellSchema>`.
    * - ``CellExpression properties``
      - Information about expression properties observed for a specific cell. ``CellExpression`` properties have their own schema and file format described :ref:`here <CellExpressionSchema>`.
    * - ``Receptor``
      - Information about adaptive immune receptors (i.e., Ig and TCR) that are
        linked to observed Cells in a study. ``Receptors`` have their own schema
        and file format described :ref:`here <ReceptorSchema>`.
    * - ``GermlineSet``
      - Lists the receptor germline sequences that have been identified for a single locus within a particular species or sub-species, together with supporting evidence and additional metadata to assist with sequence annotation. Brings togteher the subsidiary objects ``AlleleDescription``, ``SequenceDelineationV``, ``RearrangedSequence``, ``UnrearrangedSequence``, ``Acknowledgement``.
    * - ``GenotypeSet``
      - Lists the receptor germline sequences that have been identified within a single subject, including both those that are listed within ``GermlineSets`` and those that have not been so listed. References the subsidiary object ``Genotype``, which covers a single locus.
 
  

Relationship between Schema Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MiAIRR categories are hierarchical, and includes information about
the study, the subjects, the collected samples and how they are
processed, details of the sequencing protocol, and information about
the data analysis. The top-down relationships are either 1-to-n
indicating the top level object can be related to any number of
sub-level objects, or n-to-n indicating any number of top level object
can be related to any number of sub-level objects. Lastly, 1-to-1
indicates the top level object is related to a single sub-level
object.

+ ``Study`` 1-to-n with ``Subject``. A study may contain any number of subjects.

+ ``Subject`` 1-to-n with ``Diagnosis``. Each subject may contain any number of diagnoses.

+ ``Subject`` 1-to-n with ``Sample``. Each subject may contain any number of samples.

+ ``Sample`` 1-to-n with ``CellProcessing``. A sample may have any number of cell processing records.

+ ``CellProcessing`` 1-to-n with ``NucleicAcidProcessing``. A cell processing record may have any number of nucleic acid processing records.

+ ``NucleicAcidProcessing`` 1-to-n with ``SequencingRun``. A nucleic acid processing records may have any number of sequencing runs.

+ ``SequencingRun`` n-to-n with ``DataProcessing``. Multiple sequencing runs can be combined in a data processing, and multiple data processing can be done on a sequencing run.

However, this hierarchy is deep and complicated. Therefore to simplify
the processing of this information, we denormalized the hierarchy
around the conceptual ``Repertoire`` object. This denormalization
represents many relationships as 1-to-1 which simplifies the
structure. A single ``Repertoire`` has these relationships with the
primary schema objects.

+ ``Repertoire`` 1-to-1 with ``Study``. A repertoire is for a single study, though a study may have multiple repertoires.

+ ``Repertoire`` 1-to-1 with ``Subject``. A repertoire is for a single subject, though a subject may have other repertoires defined.

+ ``SampleProcessing`` 1-to-1 with ``Sample``, ``CellProcessing``, ``NucleicAcidProcessing``, and ``SequencingRun``. A sample processing is a single chain from initial collection, through cell and nucleic acid processing, to sequencing.

+ ``Repertoire`` 1-to-n with ``SampleProcessing``. Generally a repertoire has a single sample processing, but sometimes studies perform technical replicates or re-sequencing to generate additional data, and these studies will have multiple sample processings, which are to be combined and analyzed together as part of the same repertoire.

+ ``Repertoire`` 1-to-n with ``DataProcessing``. A repertoire can be analyzed multiple times. More details about multiple data processing is provided below.

The trade-off with denormalization of the hierarchy is that it causes
duplication of data. For example, two repertoires for the same study
will have the ``Study`` information duplicated within each of the two
repertoire records; likewise multiple repertoires for the same subject
will have the ``Subject`` information duplicated.

While the denormalized ``Repertoire`` simplifies read-only access to
the MiAIRR information, it complicates data entry and write access to
the information because updates need to be propagated to all of the
duplicate records. Therefore, ``Repertoire`` was designed to be easily
transformed into a normalized form, representing the full hierarchy of
the objects, by utilizing the `study_id`, `subject_id`, `sample_id`, and
`sample_processing_id` fields to uniquely identify the ``Study``, ``Subject``, ``Sample``, and
``SampleProcessing`` objects across multiple repertoires. The exception is that
``CellProcessing`` and ``NucleicAcidProcessing`` do not have their own
unique identifiers, so they are included within ``SampleProcessing``.


AIRR extension properties
~~~~~~~~~~~~~~~~~~~~~~~~~

The OpenAPI V2 and V3 specification provides the ability to define extension
properties on schema objects. These are additional properties on
the schema definition directly, not to be confused with additional
properties on the data. These extension properties allow those schema
definitions to be annotated with MiAIRR and AIRR specific
information. Instead of creating separate extensions for each
property, a single extension ``x-airr`` property is defined, which is
an object that contains any number of properties. Within the AIRR
schema, ``AIRR_Extension`` defines the schema for the ``x-airr``
object and the properties within it. Here is a list of the currently
supported AIRR extension properties:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Extension
      - Description
    * - ``miairr``
      - Present if the annotated property is a MiAIRR data standard
        element. Always has a :ref:`requirement level <RequirementLevels>`
        assigned to it.
    * - ``nullable``
      - Assumes ``miairr``. False if the annotated property must not be
        ``NULL`` by the MiAIRR standard, otherwise True or null. This extension
        is not valid for OpenAPI V3 as it has the ``nullable`` builtin property.
    * - ``set``
      - Assumes ``miairr``. The MiAIRR set for the annotated property.
    * - ``subset``
      - Assumes ``miairr``. The MiAIRR subset for the annotated property.
    * - ``name``
      - Assumes ``miairr``. The MiAIRR field name.
    * - ``format``
      - Describes the format for the annotated property. Value is either
        ``free text``, ``controlled vocabulary`` or ``ontology``.
    * - ``ontology``
      - If ``format=ontology`` then this provides additional information
        about the ontology including draft status, name, URL and top
        node term.
    * - ``identifier``
      - True if the field is an identifier required to link metadata and/or individual
        sequence records across objects in the complete AIRR Data Model and ADC API.
            default: false
    * - ``adc-query-support``
      - True if an ADC API implementation must support queries on the field.
        If false, query support for the field in ADC API implementations is optional.
    * - ``deprecated``
      - True if the field has been deprecated from the schema.
    * - deprecated-description:
      - Information regarding the deprecation of the field.
    * - deprecated-replaced-by:
      - The deprecated field is replaced by this list of fields.


Schema Definitions
-----------------------------

.. toctree::
   :maxdepth: 2

   Requirement levels of fields <airr_schema_requirement_levels>
   Repertoire Schema <metadata>
   Rearrangement Schema <rearrangements>
   Alignment Schema (Experimental) <alignments>
   Clone and Lineage Tree Schema (Experimental) <clone>
   Cell Schema (Experimental) <cell>
   Cell Expression Schema (Experimental) <cellexpression>
   Germline Schema (Experimental) <germline>
   Receptor Schema (Experimental) <receptor>

