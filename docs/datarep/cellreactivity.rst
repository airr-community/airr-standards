.. _CellReactivitySchema:

Cell Reactivity Schema
=====================================

The ``CellReactivity`` object contains information that describes the
binding of a compound resembling an Ig or TCR antigen by a single,
intact cell. It is critical to note that while such experimental
measurements are related to the antigen reactivity of individual
Receptors expressed by the cell, the relation is rather complex as
multiple Receptor species, different expression levels and background
binding of the compound would need to be taken into account. Therefore
the AIRR Schema provides a separate record for this information, which
is only indirectly linked (via ``Cell``) to the ``Receptor`` object.


File Format Specification
-------------------------

The file format has not been specified yet.


.. _CellReactivityFields:

Cell Reactivity Fields
----------------------

:download:`Download as TSV <../_downloads/CellReactivity.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in CellReactivity_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}


Within the ``CellReactivity`` object, it is expected that the properties
``antigen_source_species``, ``peptide_start``, ``peptide_end`` and
``peptide_sequence_aa`` have an inseparable relationship with
``antigen_type``. They only present a valid value when ``antigen_type``
is ``protein`` or ``peptide``, otherwise they MUST contain a NULL value.
In the former case, ``peptide_sequence_aa`` SHOULD present the actual
peptide sequence of the protein used experimentally, while the
``antigen`` field SHOULD reference to a database entry of the protein
from which the peptide was derived from. Both ``peptide_start`` and
``peptide_end`` indicate the (1-based) start and end location of
``peptide_sequence_aa`` in the reference sequence. Note that highly-
repetitive proteins might contain the same peptide at multiple locations
of their full-length sequence. While it is generally recommended to
always use the position of the first occurence for the ``peptide_start``
and ``peptide_end`` annotation, this also stresses the importance to
compare actual peptide sequences, not only coordinates.

The five MHC properties (``mhc_*``), which are specifically required for
records in which ``ligand_type`` is ``MHC:peptide`` or ``MHC:non-peptide``
should be NULL for all other ``ligand_types``.

