.. _ExpressionSchema:

Expression Schema
=====================================

File Format Specification
-------------------------

The file format has not been specified yet.

.. _ExpressionFields:

Expression Fields
------------------------------

:download:`Download as TSV <../_downloads/Expression.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Expression_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}
