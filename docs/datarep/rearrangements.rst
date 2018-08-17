.. _RearrangementSchema:

Rearrangement Schema
===============================

See the :ref:`format overview <DataRepresentations>` for details on how
to structure this data.

Definition Clarifications
------------------------------

**Junction versus CDR3**

We work with the IMGT definitions of the junction and CDR3 regions.  Specifically,
the IMGT ``JUNCTION`` includes the conserved cysteine and tryptophan/phenylalanine
residues, while ``CDR3`` excludes those two residues. Therefore, our ``junction``
and ``junction_aa`` fields which represent the extracted sequence include the two
conserved residues, while the coordinate fields (``cdr3_start`` and ``cdr3_end``)
exclude them.

**Productive**

The schema does not define a strict definition of a productive rearrangement.
However, the IMGT definition is recommended:

1. Coding region has an open reading frame
2. No defect in the start codon, splicing sites or regulatory elements.
3. No internal stop codons.
4. An in-frame junction region.

**Locus names**

A naming convention for locus names is not strictly enforced, but the IMGT
locus names are recommended. For example, in the case of human data, this would
be the set: IGH, IGK, IGL, TRA, TRB, TRD, or TRG.

**Gene and allele names**

Gene call examples use the IMGT nomenclature, but no specific gene or allele
nomenclature is mandated. Species denotations may or may not be included in the
gene name, as appropriate. For example, "Homo sapiens IGHV4-59*01", "IGHV4-59*01" and
"AB019438" are all valid entries for the same allele.

**Alignments**

There is no required alignment scheme for the nucleotide and amino acid alignment
fields. These fields may, or may not, include numbering spacers (e.g., IMGT-numbering gaps),
variations in case to denote mismatches, deletions, or other features appropriate to the tool that
performed the alignment. The only strict requirement is that the query ("sequence") and
reference ("germline") **must** be properly aligned.

Fields
------------------------------

:download:`Download as TSV <../_downloads/Rearrangement.tsv>`.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Priority
      - Description
    {%- for field, fieldprops in airr_schema.Rearrangement.properties.items() %}
    * - ``{{ field }}``
      - ``{{ fieldprops.type }}``
      - {{ '**required**' if field in airr_schema.Rearrangement.required else 'optional' }}
      - {{ fieldprops.description | trim }}
    {%- endfor %}