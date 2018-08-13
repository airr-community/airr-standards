.. _DataRepresentations:

Data Representations
====================

Field Definitions
--------------------

.. toctree::
   :maxdepth: 2

   Rearrangement Schema <rearrangements>
   Alignment Schema (Experimental) <alignments>

Format Specification
--------------------

Data for ``Rearrangement`` or ``Alignment`` objects are stored as rows in a
*tab-delimited* file and should be compatible with any TSV reader.

**Encoding**

The file should be encoded as ASCII or UTF-8. Everything is case-sensitive.

**CSV dialect**

The record separator is a newline ``\n`` and the field separator is a tab ``\t``.
Fields or data should not be quoted. A header line with the AIRR-specified column
names is always required.

**Coordinate numbering**

All alignment sequence coordinates use the same scheme as IMGT and INSDC
(DDBJ, ENA, GenBank), with the exception that partial coordinate information
should not be used in favor of simply assigning the start/end of the alignment.
Meaning, coordinates should be provided as 1-based values with closed intervals,
without the use of ``>`` or ``<`` annotations that denoted a partial region.

**Boolean values**

Boolean values must be encoded as ``T`` for true and ``F`` for false.

**Null values**

*All fields can be null.* Even for columns that are described as
"required". A null value should be encoded as an empty string.

**File names**

AIRR-formatted data files should end with ``.tsv``.

**Identifiers/illegal characters**

Data must not contain tab or newline characters.  Data should avoid ``#`` and quote
characters, as the result may be implementation dependent.

**Structure**

The data file has two sections in this order:

1.  Header (single line with column names)
2.  Data (one record per line)

**Header line**

A single line containing the column names (and also specifying field order).
Any field that corresponds to one of the defined fields should use the
specified field name. The order of the fields does not matter.  Custom fields
are allowed, and should follow the same naming scheme (Python-style
``snake_case``). Consider submitting a pull request if the field may be broadly
useful.

**Data**

The main data table. Possible data types are ``string``, ``boolean``, ``number``
(floating point), and ``integer``.

**Required columns**

Some of the fields are defined as "required" and therefore must always be present
in the header.  Note, however, that all columns allow for null values.  Therefore,
required columns exist to define a core set of fields that are always present in
the table structure, but do not mandate that a value be reported.

**Custom columns**

There are no restrictions on inclusion of additional custom columns in the
rearrangments file, provided such columns do not use the same name as an
existing required or optional field.

**Ordering**

Unless specified otherwise, there is no requirement that the records are sorted
in any way.  However, multiple records with the same primary key should be next
to each other.  Put another way, the data should be stored as if they were the
result of ``GROUP BY primary_key``.

**CIGAR specification**

Alignments details are specified using the CIGAR format as defined in the
`SAM specifications <https://samtools.github.io/hts-specs/SAMv1.pdf>`__, with
some vocabulary restrictions on the use of clipping, skipping and padding operators.
The following table defines the valid operator set.

.. csv-table::
    :header: Operator, Description
    :widths: auto

    "=", "An identical non-gap character."
    "X", "A differing non-gap character."
    "M", "A positional match in the alignment. This can be either an identical (=) or differing (x) non-gap character."
    "D", "Deletion in the query (gap in the query)."
    "I", "Insertion in the query (gap in the reference)."
    "S", "Positions that appear in the query, but not the reference. Used exclusively to denote the start position of the alignment in the query. Should precede any N operators."
    "N", "A space in the alignment. Used exclusively to denote the start position of the alignment in the reference. Should follow any S operators."

Note, the use of either the ``=``/``X`` or ``M`` syntax is valid, but should be used consistently.
While leading ``S`` and ``N`` operators are required, tailing ``S`` and ``N`` operators are optional.