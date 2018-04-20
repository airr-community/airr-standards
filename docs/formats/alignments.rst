.. _AlignmentSchema:

Alignment Schema (Experimental)
===============================

See the :ref:`format overview <DataRepresentations>` for details on
how to structure this data.

Note, this schema definition is still experimental and should not be
considered final.

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
