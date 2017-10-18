# `rearrangement` schema/format

See the formatting overview for details on how to structure this data.

**Fields**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `sequence_id` | `string` |  mandatory  | Read/sequence identifier |
| `sequence` | `string` |  mandatory  | Nucleotide sequence (e.g., the "read" sequence; revcomp'd if necessary) |
| `sample_id` | `string` |  mandatory  | The biological sample this read derives from (e.g., from BioSample database) |
| `constant` | `string` |  mandatory  | Constant region gene (e.g., IGHG4, IGHA2, IGHE, TRBC) |
| `functional` | `boolean` |  mandatory  | VDJ sequence is predicted to be functional |
| `rev_comp` | `boolean` |  mandatory  | Sequence is reverse complemented |
| `cell_index` | `string` |  | Cell index for single-cell sequencing. Also used for associating paired chains (e.g., heavy/light, alpha/beta) |
| `v_call` | `string` |  mandatory  | V allele assignment |
| `d_call` | `string` |  mandatory  | D allele assignment |
| `j_call` | `string` |  mandatory  | J allele assignment |
| `c_call` | `string` |  mandatory  | C gene assignment |
| `v_score` | `float` |  mandatory  | V alignment score |
| `d_score` | `float` |  mandatory  | D alignment score |
| `j_score` | `float` |  mandatory  | J alignment score |
| `c_score` | `float` |  mandatory  | C alignment score |
| `v_cigar` | `string` |  mandatory  | V alignment CIGAR string |
| `d_cigar` | `string` |  mandatory  | D alignment CIGAR string |
| `j_cigar` | `string` |  mandatory  | J alignment CIGAR string |
| `c_cigar` | `string` |  mandatory  | C alignment CIGAR string |
| `cdr3_aa` | `string` |  mandatory  | Amino acid sequence for CDR3 |
| `cdr3_nt` | `string` |  mandatory  | Nucleotide sequence for CDR3 |
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
| `v_end` | `integer` |  | End coordinate of the V segment (generally inside the CDR3) |
| `d_start` | `integer` |  | Start coordinate of the D segment |
| `d_end` | `integer` |  | End coordinate of the D segment |
| `j_start` | `integer` |  | Start coordinate of the J segment (generally inside the CDR3) |
| `cdr3_end` | `integer` |  | CDR3 end coord in sequence (transferred from germline) |
| `fwr4_end` | `integer` |  | FWR4 end coord in sequence (transferred from germline) |
| `duplicate_count` | `integer` |  | Number of duplicate reads for this sequence |
| `clone` | `string` |  | Clone assignment for this sequence |
