.. _ReceptorSchema:

Receptor Schema
===============

The purpose of the ``Receptor`` object is to provide an structure for
information referring to actual *Receptors*, i.e., Ig or TCR, both for
outgoing and incoming links. To this end, the ``Receptor`` object
describes the receptor as an abstract and global concept, i.e., the
actual Ig/TCR protein complex, which MAY or MAY NOT have been observed
in the current study. However, the rearrangements encoding the
respective chains MUST be present in the study as well as the
information linking them (see below). In addition the object allow
references to entries in external database (e.g., IEDB).

The ``Receptor`` object explicitly requires full sequence information
of the two associated variable domains. This is considered to be an
acceptable restriction from an AIRR-seq perspective, where sequencing
typically precedes or takes place in combination with the determination
of receptor reactivity.


Identifiers
-----------

The ``Receptor`` objects has two properties that serve as identifiers:

*  ``receptor_id`` is a **local** identifier and its uniqueness MUST NOT
   be assumed beyond the scope of the study the receptor was reported
   in. This property can be used, e.g., to represent designations for
   Ig/TCR used in a manuscript.
*  ``receptor_hash`` is the SHA256 hash of the receptors variable domain
   amino acid sequences, which serves as a **globally unique**
   identifier that can be independently calculated by repositories
   without requiring prior communication. It is calculated as follows,
   where ``base16`` designates the function described in `RFC4648
   Section 6`_:

   .. code-block::

      lower_case(
          base16(
              sha256(
                  concatenate(
                      upper_case(receptor_variable_domain_1_aa),
                      upper_case(receptor_variable_domain_2_aa)
                  )
              )
          )
      )


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

References to information describing the same receptor located in other
databases (i.e., outgoing links) SHOULD be provided as as CURIEs in the
``receptor_ref`` property. Entries in this array MUST refer to objects
that a conceptually similar to the *Receptor* concept used by the AIRR
Schema. Linkage to potentially existing reactivity information needs
is expected to happen in the external database, not in the ``Receptor``
record.

``Receptor`` objects SHOULD be created even in the absence of additional
external information, as this will enhance the discoverability of
AIRR-seq experiments in which a receptor might have been present. This
especially applies to experiments that provide further evidence (e.g.,
surface expression, reaction to superantigens) showing that a receptor
is functional and present on the surface.


Note on cells expressing more than a single receptor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cells that express more than a single IGH/TRB/TRD or a single
IGK/IGL/TRA/TRG chain are regularly observered as allelic exclusion is
never complete and its efficiency is rather low for loci like TRA.
Such dual-expressing cells can technically be accommodated in the
current AIRR Schema as an individual ``Cell`` object can link to more
than two rearrangemts and to more than a single ``Receptor``. In the
case of two potential receptors, both MAY be created as objects, if the
general annotation rules are met for each of them. Note that the
annotation of cell-based reactivity information is handled by the
:ref:`CellReactivitySchema` object.


Representation of bi-specific antibodies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The goal of the AIRR Standards is primarily to represent naturally
occuring receptors. While bi-specific antibodies may arise in
dual IGK/IGL expressing B cells their individual reactivity is
not measured on a regular basis. Therefore they are currently not
supported in the ``Receptor`` schema.


.. _ReceptorFields:

Receptor Fields
-----------------------------

:download:`Download as TSV <../_downloads/Receptor.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Receptor_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}



.. === References and Links ===

.. _`RFC4648 Section 6`: https://datatracker.ietf.org/doc/html/rfc4648#section-6
