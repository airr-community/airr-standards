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
| `junction_nt` | `string` |  mandatory  | Nucleotide sequence of the junction region (CDR3 plus conserved residues) |
| `junction_aa` | `string` |  mandatory  | Amino acid sequence of the junction region (CDR3 plus conserved residues) |
| `v_evalue` | `float` |  | V alignment E-value (when applicable) |
| `d_evalue` | `float` |  | D alignment E-value (when applicable) |
| `j_evalue` | `float` |  | J alignment E-value (when applicable) |
| `v_identity` | `float` |  | V alignment identity |
| `d_identity` | `float` |  | D alignment identity |
| `j_identity` | `float` |  | J alignment identity |
| `vdj_score` | `float` |  | Score for aligners that consider the full sequence as a whole |
| `vdj_evalue` | `float` |  | E-value for aligners that consider the full sequence as a whole |
| `vdj_identity` | `float` |  | Identity for aligners that consider the full sequence as a whole |
| `vdj_cigar` | `string` |  | VDJ alignment CIGAR string |
| `v_start` | `integer` |  | Position of first V nucleotide in 'sequence' field |
| `v_germ_start` | `integer` |  | Position of 'v_start' field in IMGT numbered germline V(D)J sequence |
| `fwr1_start` | `integer` |  | FWR1 start coordinate in sequence (transferred from germline) |
| `fwr1_end` | `integer` |  | FWR1 end coordinate in sequence (transferred from germline) |
| `cdr1_start` | `integer` |  | CDR1 start coord in sequence (transferred from germline) |
| `cdr1_end` | `integer` |  | CDR1 end coord in sequence (transferred from germline) |
| `fwr2_start` | `integer` |  | FWR2 start coord in sequence (transferred from germline) |
| `fwr2_end` | `integer` |  | FWR2 end coord in sequence (transferred from germline) |
| `cdr2_start` | `integer` |  | CDR2 start coord in sequence (transferred from germline) |
| `cdr2_end` | `integer` |  | CDR2 end coord in sequence (transferred from germline) |
| `fwr3_start` | `integer` |  | FWR3 start coord in sequence (transferred from germline) |
| `fwr3_end` | `integer` |  | FWR3 end coord in sequence (transferred from germline) |
| `cdr3_start` | `integer` |  | CDR3 start coord in sequence (transferred from germline) |
| `cdr3_end` | `integer` |  | CDR3 end coord in sequence (transferred from germline) |
| `fwr4_start` | `integer` |  | FWR3 start coord in sequence (transferred from germline) |
| `fwr4_end` | `integer` |  | FWR4 end coord in sequence (transferred from germline) |
| `v_end` | `integer` |  | End coordinate of the V segment (generally inside the CDR3) |
| `d_start` | `integer` |  | Start coordinate of the D segment |
| `d_germ_start` | `integer` |  | Position of 'd_start' field in IMGT numbered germline V(D)J sequence |
| `d_end` | `integer` |  | End coordinate of the D segment |
| `j_start` | `integer` |  | Start coordinate of the J segment (generally inside the CDR3) |
| `j_germ_start` | `integer` |  | Position of 'j_start' field in IMGT numbered germline V(D)J sequence |
| `j_end` | `integer` |  | End coordinate of the J segment |
| `junction_length` | `integer` |  | Number of junction nucleotides in sequence_vdj |
| `np1_length` | `integer` |  | Number of of nucleotides between sample V and D sequences |
| `np2_length` | `integer` |  | Number of of nucleotides between sample D and J sequences |
| `n1_length` | `integer` |  | Nucleotides 5' of the D-segment |
| `n2_length` | `integer` |  | Nucleotides 3' of the D-segment |
| `p3v_length` | `integer` |  | Palindromic nucleotides 3' of the V-segment |
| `p5d_length` | `integer` |  | Palindromic nucleotides 5' of the D-segment |
| `p3d_length` | `integer` |  | Palindromic nucleotides 3' of the D-segment |
| `p5j_length` | `integer` |  | Palindromic nucleotides 5' of the J-segment |
| `duplicate_count` | `integer` |  | Number of duplicate reads for this sequence |
| `consensus_count` | `integer` |  | Number of reads contributing to the consensus for this sequence |
| `clone` | `string` |  | Clone assignment for this sequence |
