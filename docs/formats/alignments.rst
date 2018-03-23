``alignment`` schema/format
===========================

See the formatting overview for details on how to structure this data.

CIGAR strings must use hard/softclipping to align the full read to the full
germline reference segment.

**Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Description
    {%- for field, fieldprops in airr_schema.Alignment.properties.items() %}
    * - ``{{ field }}``
      - ``{{ fieldprops.type }}``
      - {{ fieldprops.description | trim }}
    {%- endfor %}
