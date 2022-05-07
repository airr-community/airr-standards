.. _CellExpressionSchema:

Cell Expression Schema (Experimental)
=====================================

File Format Specification
-------------------------

The file format has not been specified yet.

.. _CellExpressionFields:

Cell Fields
------------------------------

:download:`Download as TSV <../_downloads/CellExpression.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in CellExpression_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}
