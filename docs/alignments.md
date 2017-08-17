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
