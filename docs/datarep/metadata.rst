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
were filtered down to just the "productive rearrangements for IGHV4".


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

The MiAIRR metadata is hierarchical, and includes information about the study,
the subjects, the collected samples and how they are processed, details of the
sequencing protocol, and information about the data analysis. However, to
simplify processing of metadata, all information is stored in a denormalized
fashion. In particular, metadata in the file is organized as a list of YAML/JSON
objects containing key/value pairs encoding all of the MiAIRR data. This
information is denormalized so that if, for example, there are two blood samples
from the same subject, all the subject metadata will be replicated into the
object describing the results from each blood sample. (Put another way, metadata
is denormalized/replicated into the lowest level of the hierarchy.) Each YAML
object will contain a unique identifier ``repertoire_id``. This identifier can
be used to connect to data objects (e.g., ``rearrangements``).

**Linking Data**

The AIRR Python and R clients provide tools for reading and validating AIRR
metadata. In particular, metadata objects should be joined to AIRR data through
the ``repertoire_id`` fields. This means that AIRR data (e.g., rearrangement or
alignment data) should contain a ``repertoire_id`` column that is a foreign key
into the metadata YAML file.

We expect that for most users in most situation, a ``repertoire_id`` and
``rearrangement_set_id`` will be semantically equivalent and only the former
should be used.

**Multiple Software Processing on a Repertoire**

**Duality between Repertoires and Rearrangements**

There is an important duality relationship between Repertoires and Rearrangements

AIRR extension attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

File Format Specification
-----------------------------

Metadata files are YAML/JSON with a structure defined below. Files should be
encoded as UTF-8. Identifiers are case-sensitive. Files should have the
extension ``.yaml``, ``.yml``, or ``.json``.

File Structure
~~~~~~~~~~~~~~

+ The metadata file should correspond to a list of metadata objects.

+ Each metadata object should contain a top-level key/value pair for
  ``repertoire_id`` and optionally for ``rearrangement_set_id``.

+ The remaining top level keys should coorespond to the top-level MiAIRR
  categories, including ``study``, ``subject``, ``sample``. Each of these keys
  will contain a sub-object with specified keys and identifiers.

+ The full valid set of keys for each subobject corresponds to the CRWG API
  specification found here.

+ Some fields (as specified in the API spec) require the use of a particular
  ontology.

References
-----------------------------

The metadata API defines the set of fields in the metadata. INCLUDE LINK.

An example metadata file is included in the repository as ``florian.airr.yaml``.
