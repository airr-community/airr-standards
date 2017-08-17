# `alignment` schema/format

See the formatting overview for details on how to structure this data.

**Fields**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `id` | `string` |  mandatory  | Read/sequence identifier |
| `sequence` | `string` |  mandatory  | Nucleotide sequence (e.g., the "read" sequence; revcomp'd if necessary) |
| `segment` | `string` |  mandatory  | The gene segment for this alignment (e.g., V, D, J, C) |
| `rev_comp` | `boolean` |  mandatory  | Sequence is reverse complemented |
| `call` | `string` |  mandatory  | Allele assignment |
| `score` | `float` |  mandatory  | Alignment score |
| `cigar` | `string` |  mandatory  | Alignment CIGAR string |
| `identity` | `float` |  mandatory  | Alignment identity (percent) |
| `probability` | `float` |  | Alignment probability (when applicable) |
| `loglikelihood` | `float` |  | Alignment log likelihood (when applicable) |
| `rank` | `integer` |  | Alignment rank |

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
