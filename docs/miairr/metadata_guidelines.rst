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

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119]_.

Synthetic Libraries
===================

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

References
==========

.. [RFC2119] Key words for use in RFCs to Indicate Requirement Levels
   <https://tools.ietf.org/html/rfc2119>
