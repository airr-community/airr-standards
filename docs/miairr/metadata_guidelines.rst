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
+                    |                               +----------------------------------+
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


Specific Use Cases and Experimental Setups
==========================================

Synthetic libraries
-------------------

In synthetic libraries (e.g. phage or yeast display), particles present
genetically engineered constructs (e.g. scFv fusion receptors) on their
surface. As this deviates substantially from other workflows, the
following annotation SHOULD/MUST be used:

-  In general, ``Subject`` should be interpreted as the initial library
   that undergoes a mutation/selection procedure.
-  ``synthetic``: MUST be set to ``true``
-  ``species``:  It is assumed that every synthetic library is derived
   from V and J genes that exist in some vertebrate species. This field
   SHOULD encode this species. Importantly, it MUST NOT encode the
   phage vector, the bacterial host or the comparable biological
   component of the library system that constitutes the presenting
   particle.
-  ``sample_type``: SHOULD be ``NULL``.
-  ``single_cell``: Only ``true`` if individual particles are isolated and
   sequenced. Note that colonies or plaques, even if containing
   genetically identical particles, *per se* do not match this
   definition and therefore MUST be annotated as ``false``.
-  ``cell_storage``: SHOULD be used for non-cellular particles
   analogously.
-  ``physical_linkage``: For scFv constructs the ``hetero_prelinkeded``
   term MUST be used. VHH (i.e. camelid) libraries SHOULD annotate
   ``none`` as there is only a single rearrangement envolved.


10X Chromium
------------

The current 10X V(D)J Kits (07/2020, Rev. G) perform a fully nested PCR,
in which only the reverse primers (i.e., complementary to the constant
region) are Ig/TCR specific, while the forward primers anneal to the
sequence of the template switch primer. For the purpose of annotation,
this is considered a gene-specific amplification, therefore such
experiments SHOULD be annotated as follows:

-  ``single_cell``: MUST be ``true``
-  ``library_generation_method``: SHOULD be ``RT(specific)+TS(UMI)+PCR``
-  ``pcr_target`` MAY contain multiple entries, one for each locus that
   is potentially amplified. Within each entry (i.e., each ``PCRTarget``
   object) the following annotations SHOULD be provided:

   -  ``pcr_target_locus``: The locus described by this object, using
      the controlled vocabulary defined in the AIRR schema. Note that
      each object can only describe one locus, multiple loci require
      multiple ``PCRTarget`` objects.
   -  ``forward_pcr_primer_target_location``: ``NULL`` (as it cannot be
      reliably determined.
   -  ``reverse_pcr_primer_target_location``: Locus and position
      according to the respective set of reverse primers.
