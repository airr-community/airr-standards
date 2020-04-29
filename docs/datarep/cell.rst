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

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - MiAIRR
      - Description
    {%- for field in Cell_schema %}
    * - ``{{ field.name }}``
      - {{ field.type }}
      - ``{{ field.miairr }}``
      - {{ field.description | trim }}
    {%- endfor %}
