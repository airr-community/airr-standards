.. this Changelog is based on the merged pull requests involving the ````airr-schema.yaml```` file since Jan 9 2018

.. toctree::
   :maxdepth: 1
   :caption:  AIRR Standards Release Notes

Release Notes
==============


Version 1.2.?: current
--------------------------------------------------------------------------------

+ Expanded description for ``pcr_target``
 .. #288 by bussec was merged on Dec 10, 2018
+ Fix capitalization of ``age_unit`` description
 .. #290 by bcorrie was merged on Dec 10, 2018
+ Fix name: fields for ``age`` fields
 .. #285 by bcorrie was merged on Nov 27, 2018
+ Reverted ``locus_species`` until we resolve how to handle ontologies
 .. #281 by schristley was merged on Nov 24, 2018
+ Added species information to ``cell_subset`` and ``locus`` fields
 .. #260 by bussec was merged on Nov 8
+ Added ``sample_processing_id``
 .. #263 by schristley was merged on Oct 21
+ Added vocabularies/ontologies as JSON string for: Cell subset, Target substrate, Library generation method, Complete sequences, Physical linkage of different loci
 .. #155 by bussec was merged on Oct 16, 2018 • Approved
+ Include format JSON string
 .. #155 by bussec was merged on Oct 16, 2018 • Approved
+ Introduced age ranges, ``age_min``, ``age_max``, and ``age_unit``
 .. #254 by franasa was merged on Oct 11 • Approved
+ Updated schema with more concise vdj call descriptions
 .. #257 by bcorrie was merged on Oct 7 • Approved

Version 1.2.1: Oct 5, 2018
--------------------------------------------------------------------------------

+ Schema gene vs segment terminology corrections
 .. #153 by javh was merged on Sep 13 • Approved
+ Added ``Info`` object
 .. #150 by schristley was merged on Aug 28
+ Updated ``cell_subset`` URL in AIRR schema
 .. #221 by bussec was merged on Aug 7

Version 1.2.0: Aug 18, 2018
--------------------------------------------------------------------------------

+ Removed foreign 'study_id' fields
 .. #134 by schristley was merged on Jul 12
+ Introduced ``keywords_study`` field
 .. #200 by bussec was merged on Jun 13 • Approved

Version 1.1.0: May 3, 2018
--------------------------------------------------------------------------------

+ Added ``required`` and ``nullable`` constrains to AIRR schema
 .. #182 by bussec was merged on Apr 1 • Approved
+ Schema definitions for MiAIRR attributes and ontology
 .. #182 by bussec was merged on Apr 1 • Approved
+ Introduction of an ``x-airr`` object indicating if field is required by MiAIRR
 .. #182 by bussec was merged on Apr 1 • Approved
+ Rename ``rearrangement_set_id`` to ``data_processing_id``
 .. #182 by bussec was merged on Apr 1 • Approved
+ Rename ``study_description`` to ``study_type``
 .. #182 by bussec was merged on Apr 1 • Approved
+ Added ``physical quantity`` format
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
 .. #66. in progress .. #124 by javh was merged on Apr 20
+ Removed c_call, c_score and c_cigar from required as this is not typical reference aligner output
 .. #106 by javh was merged on Apr 18, 2018
+ Renamed vdj_score, vdj_identity, vdj_evalue, and vdj_cigar to ``score``, ``identity``, ``evalue``, and ``cigar``
 .. #106 by javh was merged on Apr 18, 2018
+ Added missing ``c_identity`` and ``c_evalue`` fields to Rearrangements spec
 .. #94 on Mar 22, 2018
+ Swapped order of N and S operators in CIGAR string
 .. #94 on Mar 22, 2018
+ Some description clean up for consistency in Rearrangement spec
 .. #94 on Mar 22, 2018
+ Remove repeated objects in ``definitions.yaml``
 .. #78 on Jan 26, 2018 #53
+ Added Alignment object to ``definitions.yaml``
 .. #78 on Jan 26, 2018 #67
+ Updated MiARR-Formats consistency check TSV with junction change
 .. #75 on Jan 9, 2018. also: #84, #85, #89
+ Changed definition from functional to productive
 .. #75 on Jan 9, 2018. also: #84,. #85,. #89


Version 1.0.1: Jan 9, 2018
--------------------------------------------------------------------------------

