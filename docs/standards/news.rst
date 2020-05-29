.. this Changelog is based on the merged pull requests involving the ````airr-schema.yaml```` file since Jan 9 2018

.. toctree::
   :maxdepth: 1
   :caption:  AIRR Standards Release Notes

Release Notes
==============

Version 1.3.0: May 28, 2020
--------------------------------------------------------------------------------

**Version 1.3 schema release.**

New Schema:

+ Introduced the ``Repertoire`` Schema for describing study meta data.

+ Introduced the PCRTarget Schema for describing primer target locations.

+ Introduced the SampleProcessing Schema for describing experimental processing
  steps for a sample.

+ Replaced the SoftwareProcessing schema with the DataProcessing schema.

+ Introduced experimental schema for clonal clusters, lineage trees, tree nodes,
  and cells as Clone, Tree, Node, and Cell objects, respectively.

General Updates:

+ Added multiple additional attributes to a large number of schema propertes as AIRR
  extension attributes in the ``x-airr`` field. The new ``Attributes`` object
  contains definitions for these ``x-airr`` field attributes.

+ Added the top level ``required`` property to all relevant schema objects.

+ Added the ``title`` attribute containing the short, descriptive name to all
  relevant schema object fields.

+ Added an ``example`` attribute containing an example data value to multiple
  schema object fields.

Ontology Support:

+ Added ``Ontology`` and ``CURIEResolution`` objects to support ontologies.

+ Added EBI OLS as default source for ``ontologies``

.. #296 by bussec was merged on Jan 4, 2020

+ Added vocabularies/ontologies as JSON string for: Cell subset, Target substrate, Library generation method,
  Complete sequences, Physical linkage of different loci

.. #155 by bussec was merged on Oct 16, 2018 • Approved

Rearrangement Schema:

+ Added the ``complete_vdj`` field to annotate whether a V(D)J alignment was
  full length.

+ Added the ``junction_length_aa`` field defining the length of the junction
  amino acid sequence.

+ Added the ``repertoire_id``, ``sample_processing_id``, and
  ``data_processing_id`` fields to serve as linkers to the appropriate metadata
  objects.

+ Added a controlled vocabulary to the ``locus`` field:
  ``IGH``, ``IGI``, ``IGK``, ``IGL``, ``TRA``, ``TRB``, ``TRD``, ``TRG``.

+ Deprecated the ``rearrangement_set_id`` and ``germline_database`` fields.

+ Deprecated ``rearrangement_id`` field and made the ``sequence_id``
  field be the primary unique identifer for a rearrangement record,
  both in files and data repositories.

+ Added support secondary D gene rearrangement through the additional fields:
  ``d2_call``, ``d2_score``, ``d2_identity``, ``d2_support``, ``d2_cigar``
  ``np3``, ``np3_aa``, ``np3_length``, ``n3_length``, ``p5d2_length``,
  ``p3d2_length``, ``d2_sequence_start``, ``d2_sequence_end``,
  ``d2_germline_start``, ``d2_germline_start``, ``d2_alignment_start``,
  ``d2_alignment_end``, ``d2_sequence_alignment``, ``d2_sequence_alignment_aa``,
  ``d2_germline_alignment``, ``d2_germline_alignment_aa``.

+ Updated field definitions with more concise V(D)J call descriptions.

.. #257 by bcorrie was merged on Oct 7 • Approved

Alignment Schema:

+ Deprecated the ``rearrangement_set_id`` and ``germline_database`` fields.

+ Added the ``data_processing_id`` field.

Study Schema:

+ Added the ``study_type`` field containing an ontology defined term
  for the study design.

Subject Schema:

+ Deprecated the ``organism`` field in favor of the new ``species`` field.

+ Introduced age ranges: ``age_min``, ``age_max``, and ``age_unit``.

.. #254 by franasa was merged on Oct 11 • Approved

+ Deprecated the ``age`` field.

Diagnosis Schema:

+ Changed the type of the ``disease_diagnosis`` field from ``string`` to ``Ontology``.

Sample Schema:

+ Changed the type of the ``tissue`` field from ``string`` to ``Ontology``.

CellProcessing Schema:

+ Changed the type of the ``cell_subset`` field from ``string`` to ``Ontology``.

+ Introduced the ``cell_species`` field which denotes the species from which the
  analyzed cells originate.

.. #260 by bussec was merged on Nov 8, 2019; #281 Reverted ``locus_species``  by bcorrie was merged on Nov 27, 2019


NucleicAcidProcessing Schema:

+ Defined the ``template_class`` field as type ``string``.

+ Added a controlled vocabulary the ``library_generation_method`` field.

+ Added the ``pcr_target`` field referencing the new ``PCRTarget`` schema object.

.. #288 by bussec was merged on Dec 10, 2019

+ Changed the controlled vocabulary terms of ``complete_sequences``.
  Replacing ``complete & untemplated`` with ``complete+untemplated`` and adding
  ``mixed``

SequencingRun Schema:

+ Added the ``sequencing_run_id`` field which serves as the object identifer
  field.

+ Added the ``sequencing_files`` field which links to the RawSequenceData
  schema objects defining the raw read data.

RawSequenceData Schema:

+ Added the ``file_type`` field defining the sequence file type. This field is a
  controlled vocabulary restricted to: ``fasta``, ``fastq``.

+ Added the ``paired_read_length`` field defining mate-pair read lengths.

+ Defined the ``read_direction`` and ``paired_read_direction`` fields as type ``string``.

DataProcessing Schema:

+ Replaces the SoftwareProcessing object.

+ Added ``data_processing_id``, ``primary_annotation``, ``data_processing_files``,
  ``germline_database`` and ``analysis_provenance_id`` fields.

AIRR Data Commons API:

+ Added OpenAPI V2 specification (``specs/adc-api.yaml``) for AIRR Data Commons API major version 1.

Python library:

+ Interface functions to load (``load_repertoire``), write
  (``write_repertoire``) and validate (``validate_repertoire``)
  AIRR repertoire files.

+ Interface function (``repertoire_template``) will return a complete
  repertoire object where all fields have ``null`` values.

+ Command-line tool (``airr-tools``) interface for validation has
  changed to support both AIRR rearrangement and repertoire files.

Version 1.2.1: Oct 5, 2018
--------------------------------------------------------------------------------

**Minor patch release.**

+ Schema gene vs segment terminology corrections

.. #153 by javh was merged on Sep 13 • Approved

+ Added ``Info`` object

.. #150 by schristley was merged on Aug 28

+ Updated ``cell_subset`` URL in AIRR schema

.. #221 by bussec was merged on Aug 7

Version 1.2.0: Aug 18, 2018
--------------------------------------------------------------------------------

**Peer reviewed released of the Rearrangement schema.**

+ Definition change for the coordinate fields of the Rearrangement and Alignment schema.
  Coordinates are now defined as 1-based closed intervals, instead of 0-based half-open
  intervals (as previously defined in v1.1 of the schema).

+ Removed foreign ``study_id`` fields

.. #134 by schristley was merged on Jul 12

+ Introduced ``keywords_study`` field

.. #200 by bussec was merged on Jun 13 • Approved

Version 1.1.0: May 3, 2018
--------------------------------------------------------------------------------

**Initial public released of the Rearrangement and Alignment schemas.**

+ Added ``required`` and ``nullable`` constrains to AIRR schema.

.. #182 by bussec was merged on Apr 1 • Approved

+ Schema definitions for MiAIRR attributes and ontology.

.. #182 by bussec was merged on Apr 1 • Approved

+ Introduction of an ``x-airr`` object indicating if field is required by MiAIRR

.. #182 by bussec was merged on Apr 1 • Approved

+ Rename ``rearrangement_set_id`` to ``data_processing_id``

.. #182 by bussec was merged on Apr 1 • Approved

+ Rename ``study_description`` to ``study_type``

.. #182 by bussec was merged on Apr 1 • Approved

+ Added ``physical_quantity`` format

.. #182 by bussec was merged on Apr 1 • Approved

+ Raw sequencing files into separate schema object

.. #182 by bussec was merged on Apr 1 • Approved

+ Rename Attributes object

.. #182 by bussec was merged on Apr 1 • Approved

+ Added ``primary_annotation`` and ``repertoire_id``

.. #156 by schristley was merged on Mar 4 • Approved

+ Added ``diagnosis`` to repertoire object

.. #156 by schristley was merged on Mar 4 • Approved

+ Added ontology for ``organism``

.. #156 by schristley was merged on Mar 4 • Approved

+ Added more detailed specification of ``sequencing_run``, ``repertoire`` and ``rearrangement``

.. #156 by schristley was merged on Mar 4 • Approved

+ Added repertoire schema

.. #156 by schristley was merged on Mar 4 • Approved

+ Rename ``definitions.yaml`` to ``airr-schema.yaml``

.. #66. in progress.. #124 by javh was merged on Apr 20

+ Removed ``c_call``, ``c_score`` and ``c_cigar`` from required as this is not
  typical reference aligner output

.. #106 by javh was merged on Apr 18, 2018

+ Renamed ``vdj_score``, ``vdj_identity``, ``vdj_evalue``, and ``vdj_cigar`` to ``score``,
  ``identity``, ``evalue``, and ``cigar``

.. #106 by javh was merged on Apr 18, 2018

+ Added missing ``c_identity`` and ``c_evalue`` fields to ``Rearrangement`` spec

.. #94 on Mar 22, 2018

+ Swapped order of `N` and `S` operators in CIGAR string

.. #94 on Mar 22, 2018

+ Some description clean up for consistency in ``Rearrangement`` spec

.. #94 on Mar 22, 2018

+ Remove repeated objects in ``definitions.yaml``

.. #78 on Jan 26, 2018 #53

+ Added ``Alignment`` object to ``definitions.yaml``

.. #78 on Jan 26, 2018 #67

+ Updated MiARR format consistency check TSV with junction change

.. #75 on Jan 9, 2018. also: #84, #85, #89

+ Changed definition from functional to productive

.. #75 on Jan 9, 2018. also: #84,. #85,. #89

Version 1.0.1: Jan 9, 2018
--------------------------------------------------------------------------------

**MiAIRR v1 official release and initial draft of Rearrangement and Alignment schemas.**