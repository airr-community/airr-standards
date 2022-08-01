.. _Metadata_Guidelines:

==============================
Metadata Annotation Guidelines
==============================

Purpose of this Document
========================

This document describes the RECOMMENDED ways to provide metadata
annotation for various experimental setups.


Clarification of Terms
======================

*  The key words "MUST", "MUST NOT", "REQUIRED", "SHOULD", "SHOULD NOT",
   "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
   interpreted as described in [RFC2119]_.


Individual fields
=================

library_generation_method
-------------------------

The ``library_generation_method`` describes how the nucleic acid
annotated in ``template_class`` that encodes the V(D)J-rearrangement
it reverse-transcribed, amplified and/or otherwise prepared for further
processing. Typically this procedure will precede further NGS platform-
specific steps, however these procedures MAY be combined. The field
uses a controlled vocabulary, the individual values are described below:


+--------------------+-------------------------------+----------------------------------+
| ``template_class`` | ``library_generation_method`` | Methodology                      |
+====================+===============================+==================================+
| ``DNA``            |  ``PCR``                      | Conventional PCR on genomic DNA  |
|                    |                               | of a vertebrate host (requires:  |
|                    |                               | ``synthetic`` == ``false`` )     |
|                    |                               +----------------------------------+
|                    |                               | Conventional PCR on DNA of a     |
|                    |                               | synthetic library (requires:     |
|                    |                               | ``synthetic`` == ``true`` )      |
+--------------------+-------------------------------+----------------------------------+
| ``RNA``            | ``RT(RHP)+PCR``               | RT-PCR using random hexamer      |
|                    |                               | primers                          |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(oligo-dT)+PCR``          | RT-PCR using oligo-dT primers    |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(oligo-dT)+TS+PCR``       | 5'-RACE PCR (i.e. RT is followed |
|                    |                               | by a template switch (TS) step)  |
|                    |                               | using oligo-dT primers           |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(oligo-dT)+TS(UMI)+PCR``  | 5'-RACE PCR using oligo-dT       |
|                    |                               | primers and template switch      |
|                    |                               | primers containing unique        |
|                    |                               | molecular identifiers (UMI),     |
|                    |                               | i.e., the 5' end is UMI-coded    |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(specific)+PCR``          | RT-PCR using transcript-specific |
|                    |                               | primers                          |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(specific)+TS+PCR``       | 5'-RACE PCR using transcript-    |
|                    |                               | specific primers                 |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(specific)+TS(UMI)+PCR``  | 5'-RACE PCR using transcript-    |
|                    |                               | specific primers and template    |
|                    |                               | switch primers containing UMIs   |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(specific+UMI)+PCR``      | RT-PCR using transcript-specific |
|                    |                               | primers containing UMIs (i.e.,   |
|                    |                               | the 3' end is UMI-coded)         |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(specific+UMI)+TS+PCR``   | 5'-RACE PCR using transcript-    |
|                    |                               | specific primers containing UMIs |
|                    |                               | (i.e., the 3' end is UMI-coded)  |
|                    +-------------------------------+----------------------------------+
|                    | ``RT(specific)+TS``           | RT-based generation of dsDNA     |
|                    |                               | **without** subsequent PCR. This |
|                    |                               | is used by RNA-seq kits.         |
+--------------------+-------------------------------+----------------------------------+
| any                |  ``other``                    | Any methodology not covered      |
|                    |                               | above                            |
+--------------------+-------------------------------+----------------------------------+


*_pcr_primer_target_location
----------------------------

The fields ``forward_pcr_primer_target_location`` and
``reverse_pcr_primer_target_location`` describe the location of the
innermost primer used for a given locus. This information is critical
to determine which positions of a sequence reflect a biological process
and which are an artifact of the experiment.

The terms "proximal" and "distal" in the field description refer to the
start of the respective V or C gene. Using human *TRAC* and a
hypothetical primer as an example::

   1   5    10   15   20   25   30   35   40   45   50   55  60   position (+1 = start of exon 1)
   |...|....|....|....|....|....|....|....|....|....|....|....|
                      TGCCGTGTACCAGCTGAGAG                        TRAC primer (reverse complement)
   ATATCCAGAACCCTGACCCTGCCGTGTACCAGCTGAGAGACTCTAAATCCAGTGACAAGT   Chr. 14:22,547,506-22,547,565 (GRCh38)
                     ^^                  ^
                   [a][b]               [c]                       markers

In this case:

*  +19 (marker ``[a]``) is the most distal untemplated nucleotide
*  +20 (marker ``[b]``) is the most proximal templated nucleotide
*  +39 (marker ``[c]``) is the most distal templated nucleotide


.. _Metadata_cell_subset:

cell_subset
-----------

The ``cell_subset`` field is ontology-controlled, i.e., if present, it
MUST refer to a Cell Ontology (CL) term via its ``id`` field. The field
SHOULD NOT be used for values other than ``lymphocyte`` (CL:0000542) and
its descendents. The reasoning behind this is that rearrangements of
IG and TR loci are typically confined to this population, so that other
nodes, do not provide further information. In addition, the field SHOULD
only be used if the subset has been purified to a level that is
comparable to flow cytometric cell sorting.

*  In general, the provided annotation MUST NOT contradict the
   experimentally determined phenotype. E.g., if the experiment shows
   that the population is CD27+ a term that is explicitly defined in CL
   as CD27- MUST NOT be used.
*  However, this does not mean that all markers listed in the
   description of an ontology term need to be confirmed, as long as
   the existing information is considered sufficient for classification
   and not contradictory (see above).
*  In case the experimentally isolated cells to not match any "leaf"
   term, e.g., due to the isolation of multiple populations that
   contradict the definitions, the general advice is to move up the
   CL hierarchy to the most distal term that is no-contradictory.
   In this case, ``cell_phenotype`` should be used to define the
   markers that were used experimentally.
*  Note that ontology-controlled fields allow exactly one term.
   Therefore, mixtures of defined cell populations either need to be
   demultiplexed, or -- if this is not possible -- use the last (i.e,,
   most distal) common term of all cell populations involved. Again,
   ``cell_phenotype`` can be used to provide the markers used in the
   experiment.


Specific Use Cases and Experimental Setups
==========================================

Peripheral Blood Mononuclear Cells (PBMCs)
------------------------------------------

PBMCs are frequently used starting material for AIRR-seq studies in
humans and are prepared by a density-gradient centrifugation using
Ficoll. As they constitute a mixture of myeloid and lymphoid cells,
the following points should be taken into consideration when annotating
experiments using PBMCs:

*  The ``cell_population`` and ``cell_phenotype`` fields should be
   ``NULL`` as PBMCs are neither sufficiently pure nor do they
   exclusively contain cells of the lymphocytic lineage (see
   :ref:`Metadata_cell_subset`).
*  Note that while Cell Ontology does provide a term
   ``peripheral blood mononuclear cell`` (CL:2000001), this is a sister
   node of ``lymphocyte`` (CL:0000542) and therefore outside of the
   current specification.
*  The typical annotation for PBMC is therefore as follows::

      sample_type:"peripheral venous puncture"
      tissue:
         label:"venous blood"
         id:"UBERON:0013756"
      tissue_processing"Ficoll gradient"
      cell_subset:NULL
      cell_phenotype:NULL


Synthetic libraries
-------------------

In synthetic libraries (e.g., phage or yeast display), particles present
genetically engineered constructs (e.g., scFv fusion receptors) on their
surface. As this deviates substantially from other workflows, the
following annotation SHOULD/MUST be used:

*  In general, ``Subject`` should be interpreted as the initial library
   that undergoes a mutation/selection procedure.
*  ``synthetic``: MUST be set to ``true``
*  ``species``:  It is assumed that every synthetic library is derived
   from V and J genes that exist in some vertebrate species. This field
   SHOULD encode that species. Importantly, it MUST NOT encode the
   phage vector, the bacterial host or a comparable biological component
   of the library system that constitutes the presenting particle.
*  ``sample_type``: SHOULD be ``NULL``.
*  ``single_cell``: Only ``true`` if individual particles are isolated and
   sequenced. Note that colonies or plaques, even if containing
   genetically identical particles, *per se* do not match this
   definition and therefore MUST be annotated as ``false``.
*  ``cell_storage``: SHOULD be used for non-cellular particles
   analogously.
*  ``physical_linkage``: For scFv constructs the ``hetero_prelinkeded``
   term MUST be used. VHH (i.e., camelid) libraries SHOULD annotate
   ``none`` as there is only a single rearrangement envolved.


10X Chromium
------------

The current 10X V(D)J Kits (07/2020, Rev. G) perform a fully nested PCR,
in which only the reverse primers (i.e., complementary to the constant
region) are Ig/TCR specific, while the forward primers anneal to the
sequence of the template switch primer. For the purpose of annotation,
this is considered a gene-specific amplification, therefore such
experiments SHOULD be annotated as follows:

*  ``single_cell``: MUST be ``true``
*  ``library_generation_method``: SHOULD be ``RT(specific)+TS(UMI)+PCR``
*  ``pcr_target`` MAY contain multiple entries, one for each locus that
   is potentially amplified. Within each entry (i.e., each ``PCRTarget``
   object) the following annotations SHOULD be provided:

   *  ``pcr_target_locus``: The locus described by this object, using
      the controlled vocabulary defined in the AIRR schema. Note that
      each object can only describe one locus, multiple loci require
      multiple ``PCRTarget`` objects.
   *  ``forward_pcr_primer_target_location``: ``NULL`` (as it cannot be
      reliably determined.
   *  ``reverse_pcr_primer_target_location``: Locus and position
      according to the respective set of reverse primers.
