.. _AlignmentSchema:

Alignment Schema
===========================

See the formatting overview for details on how to structure this data.

CIGAR strings must use hard/softclipping to align the full read to the full
germline reference segment.

**Fields**

:download:`Download as TSV <../_downloads/Alignment.tsv>`.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Priority
      - Description
    {%- for field, fieldprops in airr_schema.Alignment.properties.items() %}
    * - ``{{ field }}``
      - ``{{ fieldprops.type }}``
      - {{ '*required*' if field in airr_schema.Alignment.required else '' }}
      - {{ fieldprops.description | trim }}
    {%- endfor %}
