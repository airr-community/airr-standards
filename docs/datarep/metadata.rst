.. _RepertoireSchema:

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


**Multiple Data Processing on a Repertoire**

Data processing can be a complicated multi-stage
process. Documenting the process in a formal way is challenging
because of the diversity of actions that may be performed. The MiAIRR
standard requires documentation of the process but in an informal way
with free text descriptions. A ``Repertoire`` might undergo multiple
different data processing for any number of reasons, e.g. to
compare the results from different toolchains, or to compare different
settings for the same toolchain.

It is expected that all of the ``Samples`` of a ``Repertoire`` will be
processed together within a ``DataProcessing``. That is, a
``DataProcessing`` that only uses some but not all samples in a
``Repertoire`` could be confusing to users and appear as though data
is missing. Likewise, processing some samples within a ``Repertoire``
with one ``DataProcessing`` and the remaining samples with a
different ``DataProcessing`` could also confuse users. Because
``DataProcessing`` is unstructured information, it is not possible
to validate that all ``Samples`` in a ``Repertoire`` are being
processed together, so this expectation cannot be strictly
enforced.

Having multiple ``DataProcessing`` for a ``Repertoire`` will
create multiple sets of ``Rearrangements`` that are distinct and
separate from each other. Analysis tools need to be careful not to mix
these sets of ``Rearrangements`` from different ``DataProcessing``
because it can generate incorrect results. The identifier
``data_processing_id`` was added so ``Rearrangements`` can
identify their specific ``DataProcessing``.

**Linking Data**

Each ``Repertoire`` has a unique ``repertoire_id`` identifier. This
identifier should be globally unique so that repertoires from multiple
studies can be combined together without conflict. The
``repertoire_id`` is used to link other AIRR data to a
``Repertoire``. Specifically, the :ref:`Rearrangements Schema
<RearrangementSchema>` includes ``repertoire_id`` for referencing the
specific ``Repertoire`` for that ``Rearrangement``.

If a ``Repertoire`` has multiple ``DataProcessing`` then
``data_processing_id`` should be used to distinguish the
appropriate ``DataProcessing`` within the ``Repertoire``. The
``Rearrangements`` contains ``data_processing_id`` for this
purpose. The ``data_processing_id`` is only unique within a
``Repertoire`` so ``repertoire_id`` should first be used to get the
appropriate ``Repertoire`` object and then ``data_processing_id``
used to acquire the appropriate ``DataProcessing``.

It is expected that typical ``Repertoires`` might only have a single
``DataProcessing``, in which case ``repertoire_id`` and
``data_processing_id`` will be semantically equivalent and only the
former should be used.

If a ``Repertoire`` has multiple sample processing objects in the sample
array then ``sample_processing_id`` should be used to distinguish the
the approrpiate sample processing object within the ``Repertoire``. The 
``Rearrangement`` object can contain a ``sample_processing_id`` to uniquely
identify a sample processing object within a ``Repertoire``. Like
``data_processing_id``, the ``sample_processing_id`` is only unique within
the ``Repertoire`` so ``repertoire_id`` should first be used to get the 
appropiate ``Repertoire`` object and then ``sample_processing_id`` should
be used to determine the appropiate sample processing object that is associated
with the ``Rearrangement``. If the ``Rearrangement`` object does not have a
``sample_processing_id`` then it can be assumed that the rearrangement is
associated with all of the samples in the ``Repertoire`` (e.g. the rearrangement
is a collapsed rearrangement across multiple samples).

It is expected that  ``Repertoires`` might often have a single
sample processing object, in which case ``repertoire_id`` and
``sample_processing_id`` will be semantically equivalent and only the
former should be used.

Finally, if it is necessary to link a ``Rearrangement`` object with a unique 
pairing of sample processing and ``DataProcessing``, the ``repertoire_id`` of
the ``Rearrangement`` object should be used to identify the correct ``Repertoire``
object and then the ``data_processing_id`` should be used to identify the correct
``DataProcessing`` metadata and the ``sample_processing_id`` should be used to
identify the correct sample processing metadata within that ``Repertoire``.

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
experimental protocol, or data processing might have incorrectly
processed the raw sequencing data leading to invalid annotations.

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

+ The structure is the same regardless of whether the data is stored in a file or a data repository. For example, The :ref:`ADC API <DataCommonsAPI>` will return a properly structured JSON object that can be saved to a file and used directly without modification.

Repertoire Fields
------------------------------

:download:`Download as TSV <../_downloads/Repertoire.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Repertoire_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _StudyFields:

Study Fields
------------------------------

:download:`Download as TSV <../_downloads/Study.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Study_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _SubjectFields:

Subject Fields
------------------------------

:download:`Download as TSV <../_downloads/Subject.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Subject_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _DiagnosisFields:

Diagnosis Fields
------------------------------

:download:`Download as TSV <../_downloads/Diagnosis.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Diagnosis_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _SampleFields:

Sample Fields
------------------------------

:download:`Download as TSV <../_downloads/Sample.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Sample_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _CellProcessingFields:

Tissue and Cell Processing Fields
---------------------------------

:download:`Download as TSV <../_downloads/CellProcessing.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in CellProcessing_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _NucleicAcidProcessingFields:

Nucleic Acid Processing Fields
---------------------------------

:download:`Download as TSV <../_downloads/NucleicAcidProcessing.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in NucleicAcidProcessing_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _PCRTargetFields:

PCR Target Locus Fields
---------------------------------

:download:`Download as TSV <../_downloads/PCRTarget.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in PCRTarget_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _RawSequenceDataFields:

Raw Sequence Data Fields
---------------------------------

:download:`Download as TSV <../_downloads/RawSequenceData.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in RawSequenceData_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _SequencingRunFields:

Sequencing Run Fields
---------------------------------

:download:`Download as TSV <../_downloads/SequencingRun.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in SequencingRun_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _DataProcessingFields:

Data Processing Fields
---------------------------------

:download:`Download as TSV <../_downloads/DataProcessing.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in DataProcessing_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

