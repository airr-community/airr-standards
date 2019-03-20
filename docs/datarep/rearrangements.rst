.. _RearrangementSchema:

Rearrangement Schema
===============================

A Rearrangement is a sequence which describes a rearranged adaptive
immune receptor chain (e.g., antibody heavy chain or TCR beta chain)
along with a host of annotations. These annotations are defined by the
AIRR Rearrangement schema and comprises eight categories.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Category
      - Description
    * - Input
      - The input sequence to the V(D)J assignment process.
    * - Identifiers
      - Primary and foreign key identifiers for linking AIRR data across files and databases.
    * - Primary Annotations
      - The primary outputs of the V(D)J assignment process, which includes the gene locus, V, D, J, and C gene calls, various flags, V(D)J junction sequence, copy number (``duplicate_count``), and the number of reads contributing to a consensus input sequence (``consensus_count``).
    * - Alignment Annotations
      - Detailed alignment annotations including the input and germline sequences used in the alignment; score, identity, statistical support (E-value, likelihood, etc); and the alignment itself through CIGAR strings for each aligned gene.
    * - Alignment Positions
      - The start/end positions for genes in both the input and germline sequences.
    * - Region Sequence
      - Sequence annotations for the framework regions (FWRs) and complementarity-determining regions (CDRs).
    * - Region Positions
      - Positional annotations for the framework regions (FWRs) and complementarity-determining regions (CDRs).
    * - Junction Lengths
      - Lengths for junction sub-regions associated with aspects of the V(D)J recombination process.

Format Specification
------------------------------

The :ref:`format specification <FormatSpecification>` describes the file format
and details on how to structure this data.

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

The specification includes two classes of fields. Those that are
required and those that are optional. Required is defined as a column
that must be present in the header of the TSV. Optional is defined as
column that may, or may not, appear in the TSV. All fields, including
required fields, are nullable by assigning an empty string as the
value. There are no requirements for column ordering in the schema,
although the Python and R reference APIs enforce ordering for the sake
of generating predictable output. The set of optional fields that
provide alignment and region coordinates (“_start” and “_end” fields)
are defined as 1- based closed intervals, similar to the SAM, VCF,
GFF, IMGT, and INDSC formats (GenBank, ENA, and DDJB;
http://www.insdc.org).

Most fields have strict definitions for the values that they
contain. However, some commonly provided information cannot be
standardized across diverse toolchains, so a small selection of fields
have context-dependent definitions. In particular, these
context-dependent fields include the optional “_score,” “_identity,”
and “_support” fields used for assessing the quality of alignments
which vary considerably in definition based on the methodology
used. Similarly, the “_alignment” fields require strict alignment
between the corresponding observed and germline sequences, but the
manner in which that alignment is conveyed is somewhat flexible in
that it allows for any numbering scheme (e.g., IMGT or KABAT) or lack
thereof.

By default, data elements representing sequences in the schema contain
nucleotide sequences except for data elements ending in “_aa,” which
are amino acid translations of the associated nucleotide sequence.

While the format contains an extensive list of reserved field names,
there are no restrictions on inclusion of custom fields in the TSV
file, provided such custom fields have a unique name. Furthermore,
suggestions for extending the format with additional reserved names
are welcomed through the issue tracker on the GitHub repository
(https://github.com/airr-community/airr-standards).

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