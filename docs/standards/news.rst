.. this Changelog is based on the merged pull requests involving the ````airr-schema.yaml```` file since Jan 9 2018

Schema Release Notes
================================================================================

Version 1.4.0:
--------------------------------------------------------------------------------

**Version 1.4 schema release.**

New General Purpose Schema:

1. Introduced the experimental ``DataFile`` object, which defines a JSON file
   holding Repertoire metadata, data processing analysis objects, or any object
   in the AIRR Data Model.
2. Introduced the experimental ``RepertoireSet`` Schema for describing sets
   of repertoires to be analyzed together.
3. Introduced the experimental ``InfoObject`` Schema, which provides information
   about data and ADC API responses.
4. Introduced the experimental ``TimePoint`` Schema for defining the time point
   at which an observation or other action was performed.

New Germline and Genotype Schema:

The following experimental schema were introduced to support storage of
VDJ germline reference sequences, VDJ genotypes, and MHC genotypes:

1. ``GermlineSet``: Defines a collection of ``AlleleDescriptions`` from the
   same strain or species.
2. ``AlleleDescription``: Details of a putative or confirmed Ig receptor
   gene/allele inferred from one or more observations.
3. ``RearrangedSequence``: Details of a directly observed rearranged sequence
   or an inference from rearranged sequences contributing support for a gene
   or allele.
4. ``UnrearrangedSequence``: Details of an unrearranged sequence contributing
   support for a gene or allele.
5. ``SequenceDelineationV``: Delineation of a V-gene in a particular system.
6. ``GenotypeSet``: Defines a collection a VDJ genotypes for a given subject.
7. ``Genotype``: Enumerates the alleles and gene deletions inferred in a
   single subject for a single locus.
8. ``MHCGenotypeSet``: Defines a collection of MHC genotypes for a given
   subject.
9. ``MHCGenotype``: Details the genotype of major histocompatibility complex
   (MHC) class I, class II and non-classical loci.
10. ``Acknowledgement``: Defines contributors to the germline or genotype
    description.

New Single-cell Schema:

The following experimental schema were introduced to improve support
for single-cell data and extend the ``Cell`` schema.

1. ``CellExpression``: Defines a container to store single-cell expression
   level measurements.
2. ``Receptor``: Describes a complete receptor protein sequence and its
   reactivity.

Rearrangement Schema:

1. Added the optional fields ``v_frameshift``, ``j_frameshift``,
   ``d_frame`` and ``d2_frame`` defining annotations related to alignment
   reading frames.
2. Added the optional field ``umi_count`` to represent the count of distinct
   UMIs for a sequence.
3. Modified the definition of ``duplicate_count`` to remove ambiguity with the
   new ``umi_count`` field in a single-cell context. There is now a distinction
   between duplicate observed sequences (``duplicate_count``) and UMIs
   (``umi_count``).
4. The optional ``quality`` and ``quality_alignment`` alignment fields were
   added to store Phred quality scores for base calls in the ``sequence`` and
   ``sequence_alignment`` fields, respectively.
5. The following optional fields were added to denote constant region
   (``c_call``) alignment positions: ``c_sequence_start``, ``c_sequence_end``,
   ``c_germline_start``, ``c_germline_end``, ``c_alignment_start``,
   ``c_alignment_end``.

Study Schema:

1. Added the optional fields ``study_contact`` to store contact information for
   the primary study contact.
2. Modified the enumerated values supported by ``keywords_study`` to the
   following set:
   ``contains_ig``, ``contains_tr``, ``contains_paired_chain``,
   ``contains_schema_rearrangement``, ``contains_schema_clone``,
   ``contains_schema_cell``, ``contains_schema_receptor``

Subject Schema:

1. Added the optional ``genotype`` field linking to the new ``GenotypeSet`` and
   ``MHCGenotypeSet`` objects.

Sample Schema:

1. Added the required field ``collection_time_point_relative_unit`` defining
   the units for the sample collection timestamp.
2. Modified the type of the field ``collection_time_point_relative`` from a
   string to a number defined in combination with the new unit ontology field
   ``collection_time_point_relative_unit``.

NucleicAcidProcessing Schema:

1. Added the required field ``template_amount_unit`` defining the units for the
   input template quantification.
2. Modified the type of the ``template_amount`` field from a string to a number
   defined in the combination with the new unit ontology field
   ``template_amount_unit`.

Clone Schema:

1. Added the optional ``clone_count`` field to specify absolute count of clonal
   members.
2. Added the optional ``umi_count`` field to specify the total UMI count of all
   clonal members.

Cell Schema:

1. Removed the field ``expression_tabular`` whose functionality has been
   replaced by the new ``CellExpression`` schema.

Version 1.3.1: October 13, 2020
--------------------------------------------------------------------------------

**Version 1.3 documentation patch release.**

Alignment Schema:

1. Added the deprecation tags for ``rearrangement_id``, which were
   accidentally left out of the v1.3.0 release.


Version 1.3.0: May 28, 2020
--------------------------------------------------------------------------------

**Version 1.3 schema release.**

New Schema:

1. Introduced the ``Repertoire`` Schema for describing study meta data.
2. Introduced the ``PCRTarget`` Schema for describing primer target locations.
3. Introduced the ``SampleProcessing`` Schema for describing experimental processing
   steps for a sample.
4. Replaced the ``SoftwareProcessing`` schema with the ``DataProcessing`` schema.
5. Introduced experimental schema for clonal clusters, lineage trees, tree nodes,
   and cells as ``Clone``, ``Tree``, ``Node``, and ``Cell`` objects, respectively.

General Updates:

1. Added multiple additional attributes to a large number of schema propertes as AIRR
   extension attributes in the ``x-airr`` field. The new ``Attributes`` object
   contains definitions for these ``x-airr`` field attributes.
2. Added the top level ``required`` property to all relevant schema objects.
3. Added the ``title`` attribute containing the short, descriptive name to all
   relevant schema object fields.
4. Added an ``example`` attribute containing an example data value to multiple
   schema object fields.

AIRR Data Commons API:

1. Added OpenAPI V2 specification (``specs/adc-api.yaml``) for AIRR Data Commons
   API major version 1.

Ontology Support:

1. Added ``Ontology`` and ``CURIEResolution`` objects to support ontologies.
2. Added vocabularies/ontologies as JSON string for: Cell subset, Target substrate, Library generation method,
   Complete sequences, Physical linkage of different loci.

..
    2. #296 by bussec was merged on Jan 4, 2020
    3. #155 by bussec was merged on Oct 16, 2018 • Approved

Rearrangement Schema:

1. Added the ``complete_vdj`` field to annotate whether a V(D)J alignment was
   full length.
2. Added the ``junction_length_aa`` field defining the length of the junction
   amino acid sequence.
3. Added the ``repertoire_id``, ``sample_processing_id``, and
   ``data_processing_id`` fields to serve as linkers to the appropriate metadata
   objects.
4. Added a controlled vocabulary to the ``locus`` field:
   ``IGH``, ``IGI``, ``IGK``, ``IGL``, ``TRA``, ``TRB``, ``TRD``, ``TRG``.
5. Deprecated the ``rearrangement_set_id`` and ``germline_database`` fields.
6. Deprecated ``rearrangement_id`` field and made the ``sequence_id``
   field be the primary unique identifer for a rearrangement record,
   both in files and data repositories.
7. Added support secondary D gene rearrangement through the additional fields:
   ``d2_call``, ``d2_score``, ``d2_identity``, ``d2_support``, ``d2_cigar``
   ``np3``, ``np3_aa``, ``np3_length``, ``n3_length``, ``p5d2_length``,
   ``p3d2_length``, ``d2_sequence_start``, ``d2_sequence_end``,
   ``d2_germline_start``, ``d2_germline_start``, ``d2_alignment_start``,
   ``d2_alignment_end``, ``d2_sequence_alignment``, ``d2_sequence_alignment_aa``,
   ``d2_germline_alignment``, ``d2_germline_alignment_aa``.
8. Updated field definitions with more concise V(D)J call descriptions.

..
    8. #257 by bcorrie was merged on Oct 7 • Approved

Alignment Schema:

1. Deprecated the ``rearrangement_set_id`` and ``germline_database`` fields.
2. Added the ``data_processing_id`` field.

Study Schema:

1. Added the ``study_type`` field containing an ontology defined term
   for the study design.

Subject Schema:

1. Deprecated the ``organism`` field in favor of the new ``species`` field.
2. Deprecated the ``age`` field.
3. Introduced age ranges: ``age_min``, ``age_max``, and ``age_unit``.

..
    3. #254 by franasa was merged on Oct 11 • Approved

Diagnosis Schema:

1. Changed the type of the ``disease_diagnosis`` field from ``string`` to ``Ontology``.

Sample Schema:

1. Changed the type of the ``tissue`` field from ``string`` to ``Ontology``.

CellProcessing Schema:

1. Changed the type of the ``cell_subset`` field from ``string`` to ``Ontology``.
2. Introduced the ``cell_species`` field which denotes the species from which the
   analyzed cells originate.

..
    2. #260 by bussec was merged on Nov 8, 2019; #281 Reverted ``locus_species``  by bcorrie was merged on Nov 27, 2019

NucleicAcidProcessing Schema:

1. Defined the ``template_class`` field as type ``string``.
2. Added a controlled vocabulary the ``library_generation_method`` field.
3. Changed the controlled vocabulary terms of ``complete_sequences``.
   Replacing ``complete & untemplated`` with ``complete+untemplated`` and adding
   ``mixed``.
4. Added the ``pcr_target`` field referencing the new ``PCRTarget`` schema object.

..
    4. #288 by bussec was merged on Dec 10, 2019

SequencingRun Schema:

1. Added the ``sequencing_run_id`` field which serves as the object identifer
   field.
2. Added the ``sequencing_files`` field which links to the RawSequenceData
   schema objects defining the raw read data.

RawSequenceData Schema:

1. Added the ``file_type`` field defining the sequence file type. This field is a
   controlled vocabulary restricted to: ``fasta``, ``fastq``.
2. Added the ``paired_read_length`` field defining mate-pair read lengths.
3. Defined the ``read_direction`` and ``paired_read_direction`` fields as type ``string``.

DataProcessing Schema:

1. Replaces the SoftwareProcessing object.
2. Added ``data_processing_id``, ``primary_annotation``, ``data_processing_files``,
   ``germline_database`` and ``analysis_provenance_id`` fields.


Version 1.2.1: Oct 5, 2018
--------------------------------------------------------------------------------

**Minor patch release.**

1. Schema gene vs segment terminology corrections
2. Added ``Info`` object
3. Updated ``cell_subset`` URL in AIRR schema

..
    1. #153 by javh was merged on Sep 13 • Approved
    2. #150 by schristley was merged on Aug 28
    3. #221 by bussec was merged on Aug 7

Version 1.2.0: Aug 18, 2018
--------------------------------------------------------------------------------

**Peer reviewed released of the Rearrangement schema.**

1. Definition change for the coordinate fields of the Rearrangement and Alignment schema.
   Coordinates are now defined as 1-based closed intervals, instead of 0-based half-open
   intervals (as previously defined in v1.1 of the schema).
2. Removed foreign ``study_id`` fields
3. Introduced ``keywords_study`` field

..
    2. #134 by schristley was merged on Jul 12
    3. #200 by bussec was merged on Jun 13 • Approved

Version 1.1.0: May 3, 2018
--------------------------------------------------------------------------------

**Initial public released of the Rearrangement and Alignment schemas.**

1. Added ``required`` and ``nullable`` constrains to AIRR schema.
2. Schema definitions for MiAIRR attributes and ontology.
3. Introduction of an ``x-airr`` object indicating if field is required by MiAIRR.
4. Rename ``rearrangement_set_id`` to ``data_processing_id``.
5. Rename ``study_description`` to ``study_type``.
6. Added ``physical_quantity`` format.
7. Raw sequencing files into separate schema object.
8. Rename Attributes object.
9. Added ``primary_annotation`` and ``repertoire_id``.
10. Added ``diagnosis`` to repertoire object.
11. Added ontology for ``organism``.
12. Added more detailed specification of ``sequencing_run``, ``repertoire`` and
    ``rearrangement``.
13. Added repertoire schema.
14. Rename ``definitions.yaml`` to ``airr-schema.yaml``.
15. Removed ``c_call``, ``c_score`` and ``c_cigar`` from required as this is not
    typical reference aligner output.
16. Renamed ``vdj_score``, ``vdj_identity``, ``vdj_evalue``, and ``vdj_cigar``
    to ``score``, ``identity``, ``evalue``, and ``cigar``.
17. Added missing ``c_identity`` and ``c_evalue`` fields to ``Rearrangement`` spec.
18. Swapped order of `N` and `S` operators in CIGAR string.
19. Some description clean up for consistency in ``Rearrangement`` spec.
20. Remove repeated objects in ``definitions.yaml``.
21. Added ``Alignment`` object to ``definitions.yaml``.
22. Updated MiARR format consistency check TSV with junction change.
23. Changed definition from functional to productive.

..
    1. #182 by bussec was merged on Apr 1 • Approved
    2. #182 by bussec was merged on Apr 1 • Approved
    3. #182 by bussec was merged on Apr 1 • Approved
    4. #182 by bussec was merged on Apr 1 • Approved
    5. #182 by bussec was merged on Apr 1 • Approved
    6. #182 by bussec was merged on Apr 1 • Approved
    7. #182 by bussec was merged on Apr 1 • Approved
    8. #182 by bussec was merged on Apr 1 • Approved
    9. #156 by schristley was merged on Mar 4 • Approved
    10. #156 by schristley was merged on Mar 4 • Approved
    11. #156 by schristley was merged on Mar 4 • Approved
    12. #156 by schristley was merged on Mar 4 • Approved
    13. by schristley was merged on Mar 4 • Approved
    14. in progress.. #124 by javh was merged on Apr 20
    15. #106 by javh was merged on Apr 18, 2018
    16. #106 by javh was merged on Apr 18, 2018
    17. #94 on Mar 22, 2018
    18. #94 on Mar 22, 2018
    19. #94 on Mar 22, 2018
    20. #78 on Jan 26, 2018 #53
    21. #78 on Jan 26, 2018 #67
    22. #75 on Jan 9, 2018. also: #84, #85, #89
    23. #75 on Jan 9, 2018. also: #84,. #85,. #89


Version 1.0.1: Jan 9, 2018
--------------------------------------------------------------------------------

**MiAIRR v1 official release and initial draft of Rearrangement and Alignment schemas.**
