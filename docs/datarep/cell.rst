.. _CellSchema:

Cell Schema (Experimental)
==========================

The cell object acts as point of reference for all data that can be
related to an individual cell, either by direct observation or
inference.

File Format Specification
-------------------------

The file format has not been specified yet.

.. _CellFields:

Cell Fields
------------------------------

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
