.. _ReceptorSchema:

Receptor Schema (Experimental)
==============================

General
-------

Receptor data SHOULD provided if it is non-trivial, i.e., if some
information or reactivity is available (either locally or via an
external identifier). If no information about the receptor, besides
the translated amino acid sequence of the associated chains it
available, the respective object MAY be created if the curator
considers this information to be beneficial, e.g., if there is some
evidence (surface expression, reaction to superantigens) that the
receptor is functional and present on the surface.


The AIRR Receptor object explicitly requires full sequence
information of the associated V regions. This is considered to be an
acceptable restriction from an AIRR-seq perspective, where sequencing
typically precedes or happens in combination with the determination of
reactivity.


Note on cells expressing more than a single receptor
====================================================

Cells that express more than a single IGH/TRB/TRD or a single
IGK/IGL/TRA/TRG chain are regularly observered as allelic exclusion
never complete and its efficiency ranges from very high (>99%),
e.g., TRB and IGH to rather low, (e.g., TRA).


Representation of bi-specific antibodies
========================================

The goal of the AIRR Standards is primarily to represent

(This Fixes #293)
