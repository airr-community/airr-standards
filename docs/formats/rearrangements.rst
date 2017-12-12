===============================
``rearrangement`` schema/format
===============================

See the formatting overview for details on how to structure this data.

**"Junction" versus "CDR3"**

We work with the IMGT definitions of the junction/CDR3 regions.  Specifically,
the IMGT ``JUNCTION`` includes the conserved cysteine and tryptophan/phenylalanine
residues, while ``CDR3`` excludes those two residues. Therfore, our ``junction_nt``
and ``junction_aa`` fields which represent the extracted sequence include the two
conserved residues, while the coordinate fields (``cdr3_start`` and ``cdr3_end``)
exclude them.


**Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Description
    {%- for field, fieldprops in airr_schema.Rearrangement.properties.items() %}
    * - ``{{ field }}``
      - ``{{ fieldprops.type }}``
      - {{ fieldprops.description | trim }}
    {%- endfor %}
