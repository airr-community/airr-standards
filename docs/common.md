# AIRR formats overview

Data for `airr-formats` objects are stored as rows in a *tab-delimited* file and
should be compatible with any CSV reader. Metadata is stored as a companion JSON
or YAML file according to the MiAIRR specifications.


**Encoding**

The file should be encoded as ASCII or UTF-8. Everything is case-sensitive.


**CSV dialect**

The record separator is a newline `\n` and the field separator is a tab `\t`.
Fields or data should not be quoted. A header line with the AIRR-specified column
names is always required.


**Coordinate numbering**

To minimize ambiguity of locations/annotations, all sequence coordinates use
Python-style semantics for locations and intervals. This means 0-indexed coords
with half-open intervals.  See [this example](https://stackoverflow.com/a/509297/510187)
for additional clarity.


**Boolean values**

Boolean values must be encoded as `T` for true and `F` for false.


**Null values**

*All fields can be null.* (Even for columns that are described as
"mandatory".) This should be encoded as an empty string.


**File names**

AIRR-formatted data files should end with `.tsv`. If any metadata is
incorporated into the filename, consider including it in the accompanying
metadata file as well. Accompanying metadata files should end in `.meta.json` or
`.meta.yaml`.


**Identifiers/illegal characters**

Data must not contain tab or newline characters.  Data should avoid `#` and quote
characters, as the result may be implementation-dependent.


**Structure**

The data file has 2 sections in this order:

1.  Header (single line with column names)
2.  Data (one record per line)

The metadata file should be readable as a JSON or YAML object according to the
MiAIRR spec.


**Header line**

A single line containing the column names (and also specifying field order).
Any field that corresponds to one of the defined fields should use the
specified field name. The order of the fields does not matter.  Custom fields
are allowed, and should follow the same naming scheme (Python-style
`snake_case`). Consider submitting a pull request if the field may be broadly
useful.


**Data**

The main data table. Possible data types are `string`s, `boolean`s, `float`s,
and `integer`s.


**Mandated columns**

Some of the fields specified below are "mandated" and so must always be present
in a rearrangements file (in the header).  Note, however, that all columns allow
"null" values.  Therefore, mandated columns exist to define a core set of fields
that are always present in the table structure, but do not mandate that a value
be reported.


**Ordering**

Unless specified otherwise, there is no requirement that the records are sorted
in any way.  However, multiple records with the same primary key should be next
to each other.  (Put another way, the data should be stored as if they were the
result of `GROUP BY primary_key`.)


**CIGAR specification**

Alignments details are specified using the CIGAR format as defined in the
[SAM specifications](https://samtools.github.io/hts-specs/SAMv1.pdf), with
vocabulary restrictions. The following are valid operations.

| Operator | Description |
| -------- | ----------- |
| =	 	   | An identical non-gap character. |
| X	 	   | A differing non-gap character. |
| M	 	   | A positional match in the alignment. This can be either an identical (=) or differing (x) non-gap character. |
| D	 	   | Deletion in the query (gap in the query). |
| I	 	   | Insertion in the query (gap in the reference). |
| N	 	   | A space in the alignment. Used exclusively to denote the start position of the alignment in the reference. Should precede any S operators. |
| S	 	   | Positions that appear in the query, but not the reference. Used exclusively to denote the start position of the alignment in the query. |
