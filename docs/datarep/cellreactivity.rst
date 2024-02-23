.. _CellReactivitySchema:

Cell Reactivity Schema (Experimental)
=====================================

File Format Specification
-------------------------

The file format has not been specified yet.

.. _CellReactivityFields:

Cell Reactivity Fields
------------------------------

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
