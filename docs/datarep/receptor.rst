.. _ReceptorSchema:

Receptor Schema (Experimental)
==============================

General
-------

The purpose of the ``Receptor`` object is to represent reactivity data
of actual *Receptors*, i.e., Ig or TCR, either directly or indirectly.
To this end, the ``Receptor`` object has two main sections:

1. The ``receptor_*`` properties: These properties describe the receptor
   as an abstract and global concept, i.e., the actual Ig/TCR protein
   complex MAY or MAY NOT have been observed in the current study.
   However, the Rearrangements encoding the respective chains MUST
   be present in the studies as well as the information linking them
   (see below). This allows data curators to provide potential
   reactivities of a potential receptor by referencing to its entry in
   an external database (e.g., IEDB).
2. The ``reactivity_measurements`` array: This structure contains
   one or more entries, describing reactivities of the receptor that
   have been observed in the current study.

The ``Receptor`` object explicitly requires full sequence information
of the two associated variable domains. This is considered to be an
acceptable restriction from an AIRR-seq perspective, where sequencing
typically precedes or takes place in combination with the determination
of receptor reactivity.


Relations to other AIRR Schema objects
--------------------------------------

The ``Receptor`` object is only directly linked to the ``Cell`` object,
which then in turn contains the references to the records in the
``Rearrangements`` that encode the respective chains of the receptor.
Therefore a given rearrangement cannot directly reference to a receptor,
which is also not a meaningful thing to do, as the paired chain would
be unclear, but is necessary to determine a receptors reactivity.


Annotation guidelines
---------------------

Reactivity information SHOULD be provided if it was either directly
recorded in the current study or is indirectly available in a public
database, where it can be linked. If no information about the receptor,
besides the translated amino acid sequence of the associated chains is
available, the respective object MAY still be created if the curator
considers this information to be beneficial, e.g., if there is some
evidence (surface expression, reaction to superantigens) that the
receptor is functional and present on the surface. In the absence of any
such data, ``Receptor`` objects SHOULD NOT be created.


Note on cells expressing more than a single receptor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cells that express more than a single IGH/TRB/TRD or a single
IGK/IGL/TRA/TRG chain are regularly observered as allelic exclusion is
never complete and its efficiency is rather low for loci like TRA.
Such dual-expressing cells can technically be accommodated in the
current AIRR Schema as an individual ``Cell`` object can link to more
than two rearrangemts and to more than a single ``Receptor``. In the
case of two potential receptors, both MAY be created as an objects, if
the general annotation rules are met (i.e., the direct or indirect
presence of reactivity information) for each of them. Note that the 
annotation of **cell**-based reactivity information is currently not
supported for dual-expressing cells, in this case additional information
confirming the reactivity of one of the receptors would be required. 


Representation of bi-specific antibodies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The goal of the AIRR Standards is primarily to represent naturally
occuring receptors. While bi-specific antibodies may arise in
dual IGK/IGL expressing B cells their individual reactivity is
not measured on a regular basis. Therefore they are currently not
supported in the ``Receptor`` schema.

