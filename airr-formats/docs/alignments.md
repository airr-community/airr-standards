# `alignment` schema/format

See the formatting overview for details on how to structure this data.

CIGAR strings must use hard/softclipping to align the full read to the full
germline reference segment.

**Fields**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `rearrangement_id` | `string` |  mandatory  | Read/sequence identifier (identifies corresponding annotated rearrangement) |
| `sequence` | `string` |  mandatory  | Nucleotide sequence (e.g., the "read" sequence; revcomp'd if necessary) |
| `segment` | `string` |  mandatory  | The gene segment for this alignment (e.g., V, D, J, C) |
| `rev_comp` | `boolean` |  mandatory  | Sequence is reverse complemented |
| `call` | `string` |  mandatory  | Allele assignment |
| `score` | `number` |  mandatory  | Alignment score |
| `cigar` | `string` |  mandatory  | Alignment CIGAR string |
| `identity` | `number` |  mandatory  | Alignment identity (percent) |
| `probability` | `number` |  | Alignment probability (when applicable) |
| `loglikelihood` | `number` |  | Alignment log likelihood (when applicable) |
| `rank` | `integer` |  | Alignment rank |
