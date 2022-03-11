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

.. _TSVSpecification:

File Format Specification
------------------------------

Data for ``Rearrangement`` or ``Alignment`` objects are stored as rows in a
*tab-delimited* file and should be compatible with any TSV reader.

Encoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+ The file should be encoded as ASCII or UTF-8.
+ Everything is case-sensitive.

Dialect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+ The record separator is a newline ``\n`` and the field separator is a tab ``\t``.
+ Fields or data should not be quoted.
+ A header line with the AIRR-specified column names is always required.
+ Values must not contain tab or newline characters.
+ Values should avoid ``@``, ``#``, and quote (``"`` or ``'``) characters,
  as the result may be implementation dependent.
+ Nested delimiters are not supported by the schema explicitly and should be avoided.
  However, if multiple values must be reported in a single column for an application
  specific reason, then the use of a comma as the delimiter is recommended.

File names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AIRR formatted TSV files should end with ``.tsv``.

File Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data file has two sections in this order:

1.  Header. A single line with column names.
2.  Data values. One record per line.

A comment section preceding the header (e.g., ``#`` or ``@`` blocks) is not part of the
specification, but such a section is reserved for potential inclusion in a future
release. As such, a comment section should not be included in the file as it *may*
be incompatible with a future specification.

Header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A single line containing the column names and specifying the field order.
Any field that corresponds to one of the defined fields should use the
specified field name.

Required columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some of the fields are defined as ``required`` and therefore must always be present
in the header.  Note, however, that all columns allow for null values.  Therefore,
required columns exist to define a core set of fields that are always present in
the table structure, but do not mandate that a value be reported.

Custom columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are no restrictions on inclusion of additional custom columns in the
Rearrangements file, provided such columns do not use the same name as an
existing required or optional field. It is recommended that custom fields
follow the same naming scheme as existing fields. Meaning, ``snake_case``
with narrowing scope when read from left to right. For example,
``sequence_id`` is the "*identifier* of the *query sequence*".

Consider submitting a pull request for a field name reservation to the
`airr-standards repository <https://github.com/airr-community/airr-standards>`_
if the field may be broadly useful.

Ordering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are no requirements that fields or records be sorted or
ordered in any specific way. However, the field ordering provided by the
schema is a recommended default, with top-to-bottom equating to left-to-right.

.. _TSVDataValues:

Data Values
------------------------------

The possible data types are ``string``, ``boolean``, ``number`` (floating point),
``integer``, and ``null`` (empty string).

Boolean values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Boolean values must be encoded as ``T`` for true and ``F`` for false.

Null values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All fields may contain null values. This includes columns that are described as
``required``. A null value should be encoded as an empty string.

Coordinate numbering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All alignment sequence coordinates use the same scheme as IMGT and INSDC
(DDBJ, ENA, GenBank), with the exception that partial coordinate information
should not be used in favor of simply assigning the start/end of the alignment.
Meaning, coordinates should be provided as 1-based values with closed intervals,
without the use of ``>`` or ``<`` annotations that denoted a partial region.

CIGAR specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alignments details are specified using the CIGAR format as defined in the
`SAM specifications <https://samtools.github.io/hts-specs/SAMv1.pdf>`__, with
some vocabulary restrictions on the use of clipping, skipping, and
padding operators.

The CIGAR string defines the reference sequence as the germline sequence of the
given gene or region; e.g., for ``v_cigar`` the reference
is the V gene germline sequence. The query sequence is what was input into the
alignment tool, which must correspond to what is contained in the ``sequence``
field of the Rearrangement data. For the majority of use cases, this will
necessarily exclude alignment spacers from the CIGAR string, such as IMGT
numbering gaps. However, any gaps appearing in the query sequence
should be accounted for in the CIGAR string so that the alignment between
the query and reference is correctly represented.

The valid operator sets and definitions are as follows:

.. csv-table::
    :header: Operator, Description
    :widths: 20 80

    "=", "An identical non-gap character."
    "X", "A differing non-gap character."
    "M", "A positional match in the alignment. This can be either an identical (=) or differing (x) non-gap character."
    "D", "Deletion in the query (gap in the query)."
    "I", "Insertion in the query (gap in the reference)."
    "S", "Positions that appear in the query, but not the reference. Used exclusively to denote the start position of the alignment in the query. Should precede any N operators."
    "N", "A space in the alignment. Used exclusively to denote the start position of the alignment in the reference. Should follow any S operators."

Note, the use of either the ``=``/``X`` or ``M`` syntax is valid, but should be used consistently.
While leading ``S`` and ``N`` operators are required, tailing ``S`` and ``N`` operators are optional.

For example, an D gene alignment that starts at position 419 in the query ``sequence``
(leading ``418S``), that is 16 nucleotides long with no indels (middle ``16M``),
has an 10 nucleotide 5' deletion (leading ``10N``), a 5 nucleotide 3' deletion (trailing ``5N``),
and ends 72 nucleotides from the end of the query ``sequence`` (trailing ``71S``) would
have the following D gene CIGAR string (``d_cigar``) and positional information:

.. csv-table::
    :header: Field, Value
    :widths: 50 50

    d_cigar, 418S10N16M71S5N
    d_sequence_start, 419
    d_sequence_end, 434
    d_germline_start, 11
    d_germline_end, 26


Definition Clarifications
------------------------------

Junction versus CDR3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We work with the IMGT definitions of the junction and CDR3 regions.  Specifically,
the IMGT ``JUNCTION`` includes the conserved cysteine and tryptophan/phenylalanine
residues, while ``CDR3`` excludes those two residues. Therefore, our ``junction``
and ``junction_aa`` fields which represent the extracted sequence include the two
conserved residues, while the coordinate fields (``cdr3_start`` and ``cdr3_end``)
exclude them.

Productive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The schema does not define a strict definition of a productive rearrangement.
However, the IMGT definition is recommended:

1. Coding region has an open reading frame
2. No defect in the start codon, splicing sites or regulatory elements.
3. No internal stop codons.
4. An in-frame junction region.

Locus names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A naming convention for locus names is not strictly enforced, but the IMGT
locus names are recommended. For example, in the case of human data, this would
be the set: IGH, IGK, IGL, TRA, TRB, TRD, or TRG.

Gene and allele names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gene call examples use the IMGT nomenclature, but no specific gene or allele
nomenclature is strictly mandated. Species denotations may or may not be included in the
gene name, as appropriate. For example, "Homo sapiens IGHV4-59*01", "IGHV4-59*01" and
"AB019438" are all valid entries for the same allele.

However, when using an established reference database to assign gene calls
adherence to the exact nomenclature used by the reference database is strongly
recommended, as this will facilitate mapping to the database entries, cross-study
comparison, and upload to public repositories.

Alignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no required alignment scheme for the nucleotide and amino acid alignment
fields. These fields may, or may not, include numbering spacers (e.g., IMGT-numbering gaps),
variations in case to denote mismatches, deletions, or other features appropriate to the tool that
performed the alignment. The only strict requirement is that the query (``sequence``) and
reference (``germline``) **must** be properly aligned.

Frameshifts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For purposes of annotating alignments, a frameshift is defined as a frameshift that is
maintained until the end of the aligned gene, where frames are designated numerically as
1 (in-frame), 2, or 3. For example, an V gene alignment that starts in
frame 1 and ends in frame 2, disrupting the conserved cystine, would be defined as a frameshift.
Whereas, a V gene alignment with an internal frameshift that corrects with a second frameshift,
back to the original frame 1 prior to the conserved cystine, would not need to be annotated
as a frameshift.


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

:download:`Download as TSV <../_downloads/Rearrangement.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Rearrangement_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}