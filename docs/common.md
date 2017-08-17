# AIRR formats overview

Data for `airr-formats` objects are stored as rows in a *tab-delimited* file
and should be compatible with any CSV reader.


**Encoding**

The file should be encoded as ASCII or UTF-8. Everything is case-sensitive.


**CSV dialect**

The record separator is a newline `\n` and the field separator is a tab `\t`.
Fields or data should not be quoted. A header line with the AIRR-mandated column
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

File names should end with `.tsv`. If any metadata is incorporated into the
filename, consider including it in the metadata header as well.


**Identifiers/illegal characters**

Data must not contain tabs or newlines.  Data should avoid `#` and quote
characters, as the result may be implementation dependent.


**Structure**

The file has 3 sections in this order:

1.  Metadata
2.  Header (single line with column names)
3.  Data (one record per line)


**Metadata**

Each line in the metadata section should be prefixed with a `#`. When all the
`#` symbols are stripped, the remainder should be parsable as YAML data. The
first line not prefixed with a `#` marks the end of the metadata section. All
metadata should be encoded into the header rather than (in addition to?) the
filename.

In cases where repeated keys are allowed, metadata should note whether the data
file only contains "primary" records.


**Header**

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
