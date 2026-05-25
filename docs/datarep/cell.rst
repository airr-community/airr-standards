.. _CellSchema:

Single-cell Schema
==========================

The cell object acts as point of reference for all data that can be
related to an individual cell, either by direct observation or
inference.

File Format Specification
-------------------------

Files are YAML/JSON with an AIRR Data File structure. Files should be
encoded as UTF-8. Identifiers are case-sensitive. Files should have the
extension ``.yaml``, ``.yml``, or ``.json``.

Schema Field Definitions
------------------------

.. _CellFields:

Cell Fields
~~~~~~~~~~~

:download:`Download as TSV <../_downloads/Cell.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Cell_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _ExpressionFields:

Expression Fields
~~~~~~~~~~~~~~~~~

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
