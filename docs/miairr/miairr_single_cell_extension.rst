======================================
Proposed MiAIRR Single-cell Extensions
======================================

Introduction
============

One of the goals of MiniStd WG is to extended the current MiAIRR
specificiation to provide mean for more detailed annotation on the
single-cell level. We already discussed chain-pairing in #169
(now in PR #200). In addition to this, we also aim to provide marker
expression and reactivity data. However, the corresponding raw data sets
usually contain data from a lot of events and partitioning can be
complex. Therefore in analogy to the MiAIRR Set 6 annotation, two levels
will be provided: First, a link to the raw data set along with a pointer
to the record(s) in question. Second, the most relevant parts of the
processed data to allow for fast search and compare operations.

In addition, we would like to be able to provide reactivity information
for individual Ig/TCRs. Although this will often occur in a single-cell
context, attaching the information to the ``pair_id`` (and not to
``cell_id``) is important as individual cells can express multiple
receptors, e.g. due to simultaneous expression of two TCR alpha chains.
Referencing to the reactivity record via ``pair_id`` resolves this issue
and at the same time allow the annotation of stochastically inferred
chain pairs, which inherently lack a ``cell_id``.


Provisional Standard
====================

Therefore the following proposed extension to the MiAIRR data standard
have been brough forward to the AIRR Community General Assembly in
May 2019 and were ratified as provisional standard:

-  Add the following record structure to the AIRR schema, so that it can
   be referenced via ``pair_id``.
     -  keyword describing the methodology used for measurement. Note that only methods that return an absolute and quantitative measurement can be used (affinity, binding energy, etc.). Examples: "SPR", "ITC".
     -  UID of the receptor at IEDB, which can hold additional and richer data records.
     -  DOI of raw data measurements
     -  n records of reactivity measurement
        -  ``antigen``: The antigen against which the receptor was tested. For TCRs this is the combination of MHC and peptide.
        -  ``reactivity_value``: The absolute (processed) value of the measurement.
        -  ``reactivity_unit``: The physical unit of the measurement, e.g. M or kJ mol-1
*  Add the following record structure to the AIRR schema, so that it can
   be referenced via ``cell_id``.
   *  keyword describing the methology used to assess expression.
      This values for this field MUST come from a controlled vocabulary.
      Current vocabulary: {"flow cytometry", "single-cell
      transcriptome"}.
   *  Reference to raw data
      *  DOI of raw data set containing the current event
      *  Index addressing the current event within the raw data set.
         Note that the index field is not necessarily numeric but can
         also hold a DNA barcode.
   *  *n* processed data records:
      *  ``expression_value``: transformed and normalized expression level
      *  ``expression_marker``: standardized designation of the transcript or epitope

Potential issues:
   *  ``expression_value``: Transformation is a not standardized
      procedure, especially for FC data. Also note that no gating
      information is provided as this raises questions about the exact
      type of transformation (e.g. hyperbolic sine) that are often
      difficult to answer.
   *   ``expression_marker``: To be interoperatable, this should come
      from an ontology. While this is simple for gene expression, flow
      cytometry markers are more difficult as there is no unified
      ontology for them. Also note that gene name != protein name != FC
      marker.
   *  ``antigen``: To allow meaningful comparisons across studies, this
      field must be populated from a controlled vocabulary, IEDB would
      be the obvious candidate for this, but need to check whether there
      are any potential restrictions in terms of molecule classes.
