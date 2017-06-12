# `rearrangement` schema/format

## Overall format

Data for `rearrangement` objects are stored as rows in a tab-delimited file and
should be compatible with any CSV reader.


**Encoding**

The file should be encoded as ASCII or UTF-8. Everything is case-sensitive.


**CSV dialect**

The record separator is a newline `\n` and the field separator is a tab `\t`.
Fields or data should not be quoted. A header line with the columns names is
always required.


**Boolean values**

Boolean values must be encoded as `T` for true and `F` for false.


**Null values**

All fields can be null. This should be encoded as an empty string.


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

Metadata should note whether the data file only contains "primary" records.


**Header**

A single line containing the column names (and also specifying field order).
Any field that corresponds to one of the defined fields should use the
specified field name. The order of the fields does not matter.  Custom fields
are allowed, and should follow the same naming scheme (Python-style
snake_case). Consider submitting a pull request if the field may be broadly
useful.


**Data**

The main data table. The `id` field does not function as a "primary key" in the
file, and so may be repeated. Possible data types are `string`s, `boolean`s,
`float`s, and `integer`s.

Because most rearrangement annotation tools report multiple possible VDJ
matches per read, the "best" matches are typically output in a single line with
the `primary` field set to `T`.  Alternative matches are specified in
additional rows with the same `id` and the `primary` field set to `F`.

INSERT FIGURE


**Mandated columns**

Some of the fields specified below are mandated and must always be present in a
rearrangements file.


**Ordering**

There is no requirement that the records are sorted in any way.  However,
multiple records with the same `id` should be next to each other.  (Put another
way, the data should be stored as if they were the result of `GROUP BY id`.)


**Fields**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `sequence_id` | `string` |  mandatory  | Read/sequence identifier |
| `sequence` | `string` |  mandatory  | Nucleotide sequence (e.g., the "read" sequence; revcomp'd if necessary) |
| `sample_id` | `string` |  mandatory  | The biological sample this read derives from (e.g., from BioSample database) |
| `constant` | `string` |  mandatory  | Constant region gene (e.g., IGHG4, IGHA2, IGHE, TRBC) |
| `functional` | `boolean` |  mandatory  | VDJ sequence is predicted to be functional |
| `rev_comp` | `boolean` |  mandatory  | Sequence is reverse complemented |
| `v_call` | `string` |  mandatory  | V allele assignment |
| `d_call` | `string` |  mandatory  | D allele assignment |
| `j_call` | `string` |  mandatory  | J allele assignment |
| `v_score` | `float` |  mandatory  | V alignment score |
| `d_score` | `float` |  mandatory  | D alignment score |
| `j_score` | `float` |  mandatory  | J alignment score |
| `v_cigar` | `string` |  mandatory  | V alignment CIGAR string |
| `d_cigar` | `string` |  mandatory  | D alignment CIGAR string |
| `j_cigar` | `string` |  mandatory  | J alignment CIGAR string |
| `cdr3_aa` | `string` |  mandatory  | Amino acid sequence for CDR3 |
| `cdr3_na` | `string` |  mandatory  | Nucleotide sequence for CDR3 |
| `v_evalue` | `float` |  | V alignment E-value (when applicable) |
| `d_evalue` | `float` |  | D alignment E-value (when applicable) |
| `j_evalue` | `float` |  | J alignment E-value (when applicable) |
| `v_identity` | `float` |  | V alignment identity |
| `d_identity` | `float` |  | D alignment identity |
| `j_identity` | `float` |  | J alignment identity |
| `vdj_score` | `float` |  | Score for aligners that consider the full sequence as a whole |
| `vdj_evalue` | `float` |  | E-value for aligners that consider the full sequence as a whole |
| `vdj_identity` | `float` |  | Identity for aligners that consider the full sequence as a whole |
| `fwr1_start` | `integer` |  | FWR1 start coordinate in sequence (transferred from germline) |
| `cdr1_start` | `integer` |  | CDR1 start coord in sequence (transferred from germline) |
| `fwr2_start` | `integer` |  | FWR2 start coord in sequence (transferred from germline) |
| `cdr2_start` | `integer` |  | CDR2 start coord in sequence (transferred from germline) |
| `fwr3_start` | `integer` |  | FWR3 start coord in sequence (transferred from germline) |
| `cdr3_start` | `integer` |  | CDR3 start coord in sequence (transferred from germline) |
| `cdr3_end` | `integer` |  | CDR3 end coord in sequence (transferred from germline) |
| `fwr4_end` | `integer` |  | FWR4 end coord in sequence (transferred from germline) |
| `duplicate_count` | `integer` |  | Number of duplicate reads for this sequence |
| `clone` | `string` |  | Clone assignment for this sequence |
