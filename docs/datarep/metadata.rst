.. _MetadataRepresentations:

Repertoire Schema
=============================

A ``Repertoire`` is an abstract organizational unit of analysis that
is defined by the researcher and consists of study metadata, subject
metadata, sample metadata, cell processing metadata, nucleic acid
processing metadata, sequencing run metadata, a set of raw sequence
files, data processing metadata, and a set of ``Rearrangements``. A
``Repertoire`` gathers all of this information together into a
composite object, which can be easily accessed by computer programs
for data entry, analysis and visualization.

A ``Repertoire`` is specific to a single subject otherwise it can
consist of any number of samples (which can be processed in different
ways), any number of raw sequence files, and any number of
rearrangements. It can also consist of any number of data processing
metadata objects that describe the processing of raw sequence files
into ``Rearrangements``.

Typically, a ``Repertoire`` corresponds to the biological concept of
the immune repertoire for that single subject which the researcher
experimentally measures and computationally analyzes. However,
researchers can have different interpretations about what constitutes
the biological immune repertoire; therefore, the ``Repertoire`` schema
attempts to be flexible and broadly useful for all AIRR-seq studies.

Another researcher can take the same raw sequencing data and
associated metadata and create their own ``Repertoire`` that is
different from the original researcher's. A common example is to
define a repertoire that is a subset such as "productive
rearrangements for IGHV4" whereas the original researcher defined a
more generic "B cell repertoire". This new ``Repertoire`` would have
much of the same metadata as the original ``Repertoire``, except
associated with a different study, and with additional information in
the data processing metadata that describes how the rearrangements
were filtered down to just the "productive rearrangements for
IGHV4". Likewise, another researcher may get access to the original
biosample material and perform their own sample processing and
sequencing, which also would be a new ``Repertoire``. That new
``Repertoire`` could combine samples from the original researcher's
``Repertoire`` with the new sample data as a large dataset for the
subject.


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
    * - ``SoftwareProcessing``
      - Information about the data processing to transform the raw sequencing data into ``Rearrangements``.
    * - ``Repertoire``
      - Composite object that combines the schema objects ``Study``, ``Subject``, ``Diagnosis``, ``Sample``, ``CellProcessing``, ``NucleicAcidProcessing``, ``SequencingRun``, and ``SoftwareProcessing``. Each ``Repertoire`` has a unique identifier ``repertoire_id`` for linking with other data files, e.g. ``Rearrangements``.
    * - ``Rearrangments``
      - Annotated sequences describing adaptive immune receptor chains. ``Rearrangements`` have their own schema and file format described :ref:`here <RearrangementSchema>`.

Relationship between Schema Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MiAIRR metadata is hierarchical, and includes information about
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

+ ``SequencingRun`` n-to-n with ``SoftwareProcessing``. Multiple sequencing runs can be combined in a software processing, and multiple software processing can be done a sequencing run.

However, this hierarchy is deep and complicated. Therefore to simplify
the processing of this information, we denormalized the hierarchy
around the conceptual ``Repertoire`` object. This denormalization
represents many relationships as 1-to-1 which simplifies the
structure. A single ``Repertoire`` has these relationships with the
primary schema objects.

+ ``Repertoire`` 1-to-1 with ``Study``. A repertoire is for a single study, though a study may have multiple repertoires.

+ ``Repertoire`` 1-to-1 with ``Subject``. A repertoire is for a single subject, though a subject may have other repertoires defined.

+ ``Sample`` 1-to-1 with ``CellProcessing``, ``NucleicAcidProcessing``, and ``SequencingRun``. A sample is associated with a single chain of sample processing from initial collection, through cell and nucleic acid processing, to sequencing.

+ ``Repertoire`` 1-to-n with ``Sample``. Generally a repertoire has a single sample, but sometimes studies perform technical replicates or re-sequencing to generate additional data, and these studies will have multiple samples, which are to be combined and analyzed together as part of the same repertoire.

+ ``Repertoire`` 1-to-n with ``SoftwareProcessing``. A repertoire can be analyzed multiple times. More details about multiple software processing is provided below.

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
the objects, by utilizing the `study_id`, `subject_id`, and
`sample_id` fields to uniquely identify the ``Study``, ``Subject`` and
``Sample`` objects across multiple repertoires. The exception is that
``CellProcessing`` and ``NucleicAcidProcessing`` do not have their own
unique identifiers, so they are included within ``Sample``.

**Multiple Software Processing on a Repertoire**

Software processing can be a complicated multi-stage
process. Documenting the process in a formal way is challenging
because of the diversity of actions that may be performed. The MiAIRR
standard requires documentation of the process but in an informal way
with free text descriptions. A ``Repertoire`` might undergo multiple
different software processing for any number of reasons, e.g. to
compare the results from different toolchains, or to compare different
settings for the same toolchain.

It is expected that all of the ``Samples`` of a ``Repertoire`` will be
processed together within a ``SoftwareProcessing``. That is, a
``SoftwareProcessing`` that only uses some but not all samples in a
``Repertoire`` could be confusing to users and appear as though data
is missing. Likewise, processing some samples within a ``Repertoire``
with one ``SoftwareProcessing`` and the remaining samples with a
different ``SoftwareProcessing`` could also confuse users. Because
``SoftwareProcessing`` is unstructured information, it is not possible
to validate that all ``Samples`` in a ``Repertoire`` are being
processed together, so this expectation cannot be strictly
enforced.

Having multiple ``SoftwareProcessing`` for a ``Repertoire`` will
create multiple sets of ``Rearrangements`` that are distinct and
separate from each other. Analysis tools need to be careful not to mix
these sets of ``Rearrangements`` from different ``SoftwareProcessing``
because it can generate incorrect results. The identifier
``software_processing_id`` was added so ``Rearrangements`` can
identify their specific ``SoftwareProcessing``.

**Linking Data**

Each ``Repertoire`` has a unique ``repertoire_id`` identifier. This
identifier should be globally unique so that repertoires from multiple
studies can be combined together without conflict. The
``repertoire_id`` is used to link other AIRR data to a
``Repertoire``. Specifically, the :ref:`Rearrangements Schema
<RearrangementSchema>` includes ``repertoire_id`` for referencing the
specific ``Repertoire`` for that ``Rearrangement``.

If a ``Repertoire`` has multiple ``SoftwareProcessing`` then
``software_processing_id`` should be used to distinguish the
appropriate ``SoftwareProcessing`` within the ``Repertoire``. The
``Rearrangements`` contains ``software_processing_id`` for this
purpose. The ``software_processing_id`` is only unique within a
``Repertoire`` so ``repertoire_id`` should first be used to get the
appropriate ``Repertoire`` object and then ``software_processing_id``
used to acquire the appropriate ``SoftwareProcessing``.

It is expected that typical ``Repertoires`` might only have a single
``SoftwareProcessing``, in which case ``repertoire_id`` and
``software_processing_id`` will be semantically equivalent and only the
former should be used.

**Duality between Repertoires and Rearrangements**

There is an important duality relationship between ``Repertoires`` and
``Rearrangements``, specifically with the experimental protocols
described in the ``Repertoire`` versus the annotations on
``Rearrangements``. A ``Repertoire`` defines an experimental design
for what a researcher intends to measure or observe, while the
``Rearrangements`` are what was actually measured and
observed. Technically, the border between the two occurs at
sequencing, that is when the biological physical entity (prepared DNA)
is measured and recorded as information (nucleotide sequence).

This duality is important when considering how to answer certain
questions. For example, ``locus`` for ``Rearrangements`` may have the
value "IGH" which indicates that B cell heavy chain receptors were
measured, yet the ``Repertoire`` might have "T cell" in
``cell_subset`` which indicates the researcher intended to measure T
cells. This conflict between the two indicates something is
wrong. Differences can occur in many ways, as with errors in the
experimental protocol, or software processing might have incorrectly
processed the raw sequencing data leading to invalid annotations.

AIRR extension properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OpenAPI V2 specification provides the ability to define extension
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
      - True if the annotated property is a MiAIRR standard data element, otherwise False or null.
    * - ``required``
      - Assumes ``miairr=True``. True if the annotated property is required by the MiAIRR standard, otherwise False or null.
    * - ``nullable``
      - Assumes ``miairr=True``. True if the annotated property can be null by the MiAIRR standard, otherwise False or null.
    * - ``set``
      - Assumes ``miairr=True``. The MiAIRR set for the annotated property.
    * - ``subset``
      - Assumes ``miairr=True``. The MiAIRR subset for the annotated property.
    * - ``name``
      - Assumes ``miairr=True``. The MiAIRR name.
    * - ``format``
      - Describes the format for the annotated property. Value is either ``free text``, ``controlled vocabulary`` or ``ontology``.
    * - ``ontology``
      - If ``format=ontology`` then this provides additional information about the ontology including draft status, name, URL and top node term.


File Format Specification
-----------------------------

Files are YAML/JSON with a structure defined below. Files should be
encoded as UTF-8. Identifiers are case-sensitive. Files should have the
extension ``.yaml``, ``.yml``, or ``.json``.

File Structure
~~~~~~~~~~~~~~

+ The file as a whole is considered a dictionary (key/value pair) structure with the keys ``Info`` and ``Repertoire``.

+ The file can (optionally) contain an ``Info`` object, at the beginning of the file, based upon the ``Info`` schema in the OpenAPI V2 specification. If provided, ``version`` in ``Info`` should reference the version of the AIRR schema for the file.

+ The file should correspond to a list of ``Repertoire`` objects, using ``Repertoire`` as the key to the list.

+ Each ``Repertoire`` object should contain a top-level key/value pair for ``repertoire_id`` that uniquely identifies the repertoire.

+ Some fields require the use of a particular ontology or controlled vocabulary.

+ The structure is the same regardless of whether the data is stored in a file or a data repository. For example, The :ref:`Data Commons REST API <DataCommons>` will return a properly structured JSON object that can be saved to a file and used directly without modification.

References
-----------------------------

The metadata API defines the set of fields in the metadata. INCLUDE LINK.

An example metadata file is included in the repository as ``florian.airr.yaml``.
