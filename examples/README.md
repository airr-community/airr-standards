#AIRR Format Proposals

Main design goals:

* CSV data for ease-of-use and flexibility. Data sets should be readable by
  standard CSV parsers (e.g., pandas, R, etc)

* SQL semantics compatibility. Maintain tabular, non-nested data structures so
  that SQL engines can read large data sets as well.

* Support output of multiple VDJ alignments per read

* YAML metadata, for ease-of-use and flexibility

In each directory is a toy CSV data set from a smidge of data provided by
@javh.


**Proposal 1**

Read/sequence ID is not a primary key, and can be present multiple times per
data set. Multiple V, D, or J alignments can be represented for each read
without breaking relational semantics. Compatible with common CSV readers and
SQL engines. Would require group-by for most operations, though all lines for a
given read are required to be adjacent.


**Proposal 2**

There are 2 possible output files.

The first "primary" file only includes the "best" alignment for each V, D, or
J. This file should be sufficient for most downstream use cases for people.
Fully CSV/SQL compatible. The read/sequence ID should be unique in the data
set (i.e., a primary key).

The second file is just like the data file from Proposal 1.  This could be used
for applications that require all possible V/D/J alignments.

There are several ways to mandate this option:

* All tools are required to output both types of files.

* The user can specify which of the two files they want (or specify to output
  both)

* A tool can choose which of the two types of files it outputs, and the tools
  must indicate in the metadata which file type it is writing.


**Proposal 3**

Identical to proposal 2 except for the metadata. In the previous versions, the
metadata for the data set is incorporated as a header.  In this case, the
metdata is in a separate file next to the data files.


**Metadata**

We are proposing using YAML for metadata.

The content is still undefined, but at a minimum it should probbaly include the
airr-format version, some kind of data set identifier, and a pointer to a
germline set. It could (should) also include all the minimal-standards WG
fields.

As described in these proposals, the YAML data is in the first rows of the CSV
file prefixed by '#'. This will allow standard CSV parsers to read the file,
while making it easy to extract the YAML data.
