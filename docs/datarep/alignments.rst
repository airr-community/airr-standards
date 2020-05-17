.. _AlignmentSchema:

Alignment Schema (Experimental)
===============================

An Alignment is the output from a V(D)J assignment process for a
single V, D, J, or C gene for a sequence. It is not necessary
that the V(D)J assignment process performs a sequence alignment
algorithm, as the schema can support any algorithmic process. Multiple
Alignment records are supported and expected for a single sequence
with context-dependent fields (``score``, ``identity``, ``support``,
``rank``) for assessing the quality of assignments that can vary
considerably in definition based on the methodology used.

Note, this schema definition is still experimental and should not be
considered final.

File Format Specification
------------------------------

The :ref:`format specification <FormatSpecification>` describes the file format
and details on how to structure this data.

Fields
-------------------------------

:download:`Download as TSV <../_downloads/Alignment.tsv>`

.. list-table::
    :widths: 20, 10, 20, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Alignment_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}
