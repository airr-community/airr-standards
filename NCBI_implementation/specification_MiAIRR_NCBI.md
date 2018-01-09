MiAIRR-to-NCBI Specifications
=============================

Preface
-------

### The MiAIRR standard ###

The MiAIRR standard (minimal information about adaptive immune receptor repertoires) is a minimal reporting standard for experiments using sequencing-based technologies to study adaptive immune receptors (e.g. T cell receptors or immunoglobulin). It is developed and maintained by the Minimal Standards Working Group of the Adaptive Immune Receptors Repertoire (AIRR) Community [[1]](#cite1) [http://airr-community.org]. The current version (1.0) of the standard has been recently published [[2]](#cite2) and was passed by the general assembly at the annual AIRR community meeting in December 2017. MiAIRR requires researchers to report six sets of information: (1) study, subject, diagnosis & intervention; (2) sample collection; (3) sample processing and sequencing; (4) raw sequencing data; (5) data processing; and (6) processed sequences with a basic analysis results. However, MiAIRR only describes the mandatory data items that have to be reported, but neither provides details how and where to deposit data nor specifies data types and formats. Therefore this document aims to provide both a submission manual for users as well as a detailed data specification for developers.

### Aim of this document ###
To specify how to data elements are mapped between MiAIRR and the various NCBI repositories.


Outline of INSDC reporting procedure
------------------------------------

**TODO: Outline the reporting procedure for data sets 1-4**

In terms of standard compliance it is currently REQUIRED [[a]](#footnote_a) to deposit nformation for MiAIRR data sets 5 and 6 in general-purpose sequence repositories for which an AIRR-accepted specification on information mapping MUST exist. However, users should note that in the future additional AIRR-sanctioned mechanisms for data deposition will become available as specified by the AIRR Common Repository Working Group. The mapping of data items in MiAIRR data sets 5 and 6 differs substantially in size and structure and therefore requires distinct reporting procedures:

* Set 5: This is free text information describing the work flow, tools and parameters of the sequence read processing. It is REQUIRED that this information is deposited as a freely available document, permanently linked via a DOI. Note that is currently neither a specific format for this document nor a recommended service provider for obtaining the DOI.
* Set 6: This is specified to contain the consensus sequence and the following information obtained from the initial analysis: V, D and J segment, C region and IMGT-JUNCTION [[b]](#footnote_b) [[3]](#cite3). These will be deposited in a general-purpose INSDC repository, using the record structure described below.

INSDC records were originally designed to hold individual Sanger sequences. Therefore each record will contain a header with information largely identical between all records in an AIRR sequencing study. Records can be concatenated for uploading.

The INSDC feature table (FT) [[4]](#cite4) is a sequence annotation standard used within the INSDC records and assigns information to specified positions on the reported sequence string. In regard to the correct location of the provided annotation, it should especially be noted that some V(D)J inference tools will return coordinates referring to the reference instead of the query sequence. As the sequence submitted in a record MUST be identical to the query sequence, the positions provided by the V(D)J inference tool MUST, if necessary, be translated back onto the query sequence. In case the start and/or end of a feature cannot be reliably determined or is not present in the reported sequence [[c]](#footnote_c), open intervals CAN be used for reporting. However, open intervals MUST NOT be used to deliberately obfuscate known positions.

In addition to the required information specified here [[Table 1]](#table1), users CAN use all valid FT keys/qualifiers to provide further annotation for the reported sequences. However, a record MUST still be compliant with this specification, if such OPTIONAL information would be removed, meaning that it is FORBIDDEN to move REQUIRED information into OPTIONAL keys/qualifiers. In addition, users MUST NOT use keys/qualifiers that could create ambiguity with the keys/qualifiers specified here.

<p id="table1" />

###### Table 1

| element   | FT key      | FT qualifier | FT value            | REQUIRED (if used by original study)       |
|-----------|-------------|--------------|---------------------|--------------------------------------------|
| V segment | `V_segment` | `/gene`      | see [Feature table] | yes                                        |
| D segment | `D_segment` | `/gene`      | see [Feature table] | yes; if _IGH_, _TRB_ or _TRD_ sequence     |
| J segment | `J_segment` | `/gene`      | see [Feature table] | yes                                        |
| C region  | `C_region`  | `/gene`      | see [Feature table] | yes                                        |
| JUNCTION  | `CDS`       | `/function`  | "JUNCTION"          | yes                                        |

Summary of the mapping of mandatory AIRR MiniStd data set 6 elements to the INSDC feature table (FT). Note that the overall record will contain additional information, such as cross-references linking the deposited sequence reads and metadata.


Element mapping
---------------

The broad strategy of element mapping to the various repositories is depicted in [[Table 2]](#table2).

<p id="table2" />

###### Table 2

| MiAIRR data set / subset              | target repository |
|---------------------------------------|-------------------|
| 1 / study                             | BioProject        |
| 1 / subject                           | - " -             |
| 1 / diagnosis & treatment             | - " -             |
| 2 / sample                            | BioSample         |
| 3 / processing (cells)                | - " -             |
| 3 / processing (nucleic acids)        | - " -             |
| 4 / raw sequences                     | SRA               |
| 5 / processing (data)                 | user-defined DOI  |
| 6 / Processed sequences & annotations | Genbank           |

Summary of the mapping of MiAIRR data sets to the various repositories


### Mapping of data sets 1-4 to BioProject/BioSample/SRA ###

**TODO: Include item-by-item mapping** [[9]](#cite9)


### Mapping of data set 5 to a user-defined repository ###

While several mandatory item have been defined in this data set, there is currently no mapping as the reporting procedure is implemented as a free text document. AIRR RECOMMENDS to use Zenodo [https://zenodo.org] for deposition of these documents, as it is hosted by CERN and supports versioned DOIs (termed "concept" DOI). Users SHOULD use the existing `AIRR` tag [https://zenodo.org/communities/airr] when submitting documents to increase the visiblity of their study.

### Mapping of data set 6 to INSDC ###

Users should note that while the FT is standardized, the overall sequences record structure diverges between the three INSDC repositories. The following section refers to items at or above the hierarchy level of the FT using the ENA specification [[5]](#cite5), the corresponding designations of GenBank are provided in parenthesis.

#### Record header

The header MUST contain all of the following elements:

* REQUIRED: header structure as specified by the respective INSDC repository [[5]](#cite5) [[6]](#cite6) [[7]](#cite7).
* REQUIRED: identifier of the associated SRA record (MiAIRR data set 4) as `DR` line (GenBank: `DBLINK`). Note that it is **not** possible to refer to individual raw reads, only the full SRA collections can be linked.
* REQUIRED: the term "AIRR" is included in the `KW` line (GenBank: `KEYWORDS`).
* REQUIRED: DOI of the associated free-text record containing the information on data processing (MiAIRR data set 5) as `RX` line (GenBank: `REMARK` within a `REFERENCE` [[d]](#footnote_d)).


#### Feature table

The feature table, indicated as `FT` line (GenBank: `FEATURES`), MUST or SHOULD contain the following keys/qualifiers:

##### General sequence information

* REQUIRED: key `source` containing the following qualifiers:
  * REQUIRED: qualifier `/organism` (required by [[4]](#cite4))
  * REQUIRED: qualifier `/mol_type` (required by [[4]](#cite4))
  * REQUIRED: qualifier `/citation` pointing to the reference in the header (`RN` line, GenBank: `REFERENCE`) that links to the section 5 document.
  * REQUIRED: qualifier `/rearranged` [[e]](#footnote_e)
  * REQUIRED: qualifier `/note` containing the `AIRR_READ_COUNT` keyword to indicate the read number used for the consensus. The criteria for selecting these reads and the procedure used to build the consensus SHOULD be reported as part of section 5.
  * OPTIONAL: qualifier `/note` containing the `AIRR_INDEX_CELL` keyword for single-cell experiments. The value of the keyword SHOULD be a non-negative integer and MUST be identical for sequences derived from the same cell of origin
  * RECOMMENDED: qualifiers `/assembly_gap` and `/linkage_evidence` to annotate non-overlapping paired-end sequences
  * RECOMMENDED: qualifier `/strain`, if `/organism` is "Mus musculus"


##### Segment and region annotation

The following keys MUST be used for annotation according to their FT definition, if the respective item has been reported by the original study:

* REQUIRED: key `V_region`. Note that this key MUST NOT be used to annotate V segment leader sequence [[f]](#footnote_f) [[g]](#footnote_g))
* REQUIRED: key `V_segment`, both coordinates MUST be within `V_region`. Note that this key MUST NOT be used to annotate V segment leader sequence [[f]](#footnote_f) [[g]](#footnote_g)).
* REQUIRED: key `D_segment`, both coordinates MUST be within `V_region`. This key is only REQUIRED for sequences of applicable loci (_IGH_, _TRB_, _TRD_ [[h]](#footnote_h)).
* REQUIRED: key `J_segment`, both coordinates MUST be within `V_region`.
* REQUIRED: key `C_region`, both coordinates MUST NOT overlap with `V_region`. If the region can be unambiguously identified, the respective official gene symbol MUST be reported using the `/gene` qualifier. If only the isotype (e.g. IgG) but not the subclass (e.g. IgG1) can be identified, a truncated gene symbol (e.g. IGHG instead of IGHG1) SHOULD be reported instead [[i]](#footnote_i).

Each `[VDJ]_segment` key MUST or SHOULD contain the following qualifiers:

* REQUIRED: qualifier `/gene`, containing the designation of the inferred segment, according to the database in the first `/db_xref` entry. This qualifier MUST NOT contain any allele information.
* RECOMMENDED: qualifier `/allele`, containing the designation of the inferred allele, according to the database in the first `/db_xref` entry. Note that while INSDC does not specify any format for this qualifier, AIRR compliance REQUIRES that this field only contains the allele string, i.e. without the gene name or separator characters.
* REQUIRED: qualifier `/db_xref`, linking to the reference record of the inferred segment in a germline database [[8]](#cite8). This qualifier can be present multiple times, however only the first entry is mandatory and MUST link to the database used for the segment designation given with `/gene`.
* RECOMMENDED: `/inference` to indicate the tool used for segment inference.

Annotation of sequences producing multiple hits with identical scores is problematic and is ultimately at the discretion of the depositing researcher. However, the algorithms used for tie-breaking SHOULD be documented in section 5. In addition, the following procedures MUST be followed:

* Certain gene, ambiguous allele: If multiple allele of the same gene match to the sequence, the `/allele` qualifier MUST NOT be used. As the REQUIRED `/db_xref` qualifier will ofter refer to a specific allele, all equal hits SHOULD be annoted via this qualifier (which can be use multiple times).
* Ambiguous gene: Pick one, annotate using the qualifiers as noted for ambiguous allele.


##### JUNCTION annotation

INSDC does currently not define a key to annotate JUNCTION [[j]](#footnote_j). Therefore the following procedure MUST be used:
* REQUIRED: key `CDS`, indicating the positions of
  1. the first bp of the first AA of JUNCTION
  2. the last bp of the last AA of JUNCTION as determined by the utilized V(D)J inference tool. Open coordinates MUST be used for both coordinates to allow for automated creation of the `/translated` qualifier providing the peptide sequence. Further note that a non-productive JUNCTION can have a length not divisible by three. This key contains the following qualifiers:
  * REQUIRED: qualifier `/codon_start` with the assigned value "1".
  * REQUIRED: qualifier `/function` with the assigned value "JUNCTION".
  * RECOMMENDED: qualifier `/inference`, indication the tool used for positional inference.


#### Record body

The record body starts with an `SQ` line (GenBank: `ORIGIN`) and MUST contain:

* the consensus sequence


References
----------

<p id="cite1" />

[1] Breden F _et al_. Reproducibility and Reuse of Adaptive Immune Receptor Repertoire Data. Front Immunol 8:1418 (2017) [[DOI]](https://doi.org/10.3389/fimmu.2017.01418)


<p id="cite2" />

[2] Rubelt F _et al_. AIRR Community Recommendations for Sharing Immune Repertoire Sequencing Data, Nat Immunol 18:1274 (2017) [[DOI]](https://doi.org/10.1038/ni.3873)


<p id="cite3" />

[3] IMGT-ONTOLOGY definitions. [[Link]](http://www.imgt.org/ligmdb/label#JUNCTION)


<p id="cite4" />

[4] The DDBJ/ENA/GenBank Feature Table Definition. [[Link]](http://www.insdc.org/documents/feature-table)


<p id="cite5" />

[5] European Nucleotide Archive Annotated/Assembled Sequences User Manual. [[Link]](http://ftp.ebi.ac.uk/pub/databases/ena/sequence/release/doc/usrman.txt)


<p id="cite6" />

[6] GenBank Flat File Format. [[Link]](https://ftp.ncbi.nih.gov/genbank/gbrel.txt)


<p id="cite7" />

[7] GenBank Sample Record. [[Link]](https://www.ncbi.nlm.nih.gov/Sitemap/samplerecord.html)


<p id="cite8" />

[8] Controlled vocabulary for `/db_xref` qualifier. [[Link]](http://www.insdc.org/documents/dbxref-qualifier-vocabulary)


<p id="cite9" />

[9] SRA Handbook. [[Link]](https://www.ncbi.nlm.nih.gov/books/NBK47528/)


Footnotes
---------

<p id="footnote_a"></p>

[a] See the "Glossary" section on how to interpret term written in all-caps.

<p id="footnote_b"></p>

[b] Note that according to IMGT definition this is a superset of the CDR3.

<p id="footnote_c"></p>

[c] This can occur e.g. in paired-end sequencing of head-to-head concatenated transcripts, where the 5' end of the V segment is present in the amplicon, but cannot be precisely determined.

<p id="footnote_d"></p>

[d] The current GenBank record specification does not include a separate key for DOIs.

<p id="footnote_e"></p>

[e] Although FT does specify a `/germline` qualifier for non-rearranged sequences it has not been included in this specification as there is no obvious use case for it. In addition, non-rearranged transcripts would lack a number of other features that are assumed to be present, first of all the JUNCTION.

<p id="footnote_f"></p>

[f] The FT explicitly states that `V_segment` does **not** cover the leader sequence. The definition of `V_region` is slightly more ambiguous, however in combination with the `V_segment` definition, it becomes clear that the leader is also not considered to be a part of `V_region`. Therefore the leader sequence should be implicitly annotated as the region between the start of `CDS` and the start of `V_region`.

<p id="footnote_g"></p>

[g] Previously the leader was implicitly annotated as the region between `CDS` start and `V_region` start. As it was decided to drop the "global" CDS to make it easier to accommodate for INDELs, this is currently not an option anymore.

<p id="footnote_h"></p>

[h] For simplicity, this document only uses human gene symbols. For other species the specification pertains to the respective orthologs.

<p id="footnote_i"></p>

[i] This approach has been approved by NCBI.

<p id="footnote_j"></p>

[j] NCBI confirmed that once there would be enough datasets using the `JUNCTION` tag as specified here, a motion for an INSDC-sanctioned key could be initiated.


Appendix
--------

### Example record (GenBank format) ###

```
LOCUS       AB123456                 420 bp    mRNA    linear   EST 01-JAN-2015
DEFINITION  <free text description>
ACCESSION   AB123456
VERSION     AB123456.7
KEYWORDS    <other keywords>; AIRR.
SOURCE      Mus musculus
  ORGANISM  Mus musculus
            Eukaryota; Metazoa; Chordata; Craniata; Vertebrata;
            Euteleostomi; Mammalia; Eutheria; Euarchontoglires; Glires; Rodentia;
            Sciurognathi; Muroidea; Muridae; Murinae; Mus.
REFERENCE   1  (bases 1 to 420)
  AUTHORS   Stibbons,P.
  TITLE     Section 5 information for experiment FOO1
  JOURNAL   published (01-JAN-2000) on Zenodo
  REMARK    DOI:10.1000/0000-12345678
REFERENCE   2  (bases 1 to 420)
  AUTHORS   Stibbons,P.
  TITLE     Direct Submission
  JOURNAL   Submitted (01-JAN-2000) Center for Transcendental Immunology, Unseen
            University, Ankh-Morpork, 12345, DISCWORLD
DBLINK      BioProject: PRJNA000001
            BioSample: SAMN000001
            Sequence Read Archive: SRR0000001
FEATURES             Location/Qualifiers
     source          1..420
                     /organism="Mus musculus"
                     /mol_type="mRNA"
                     /strain="C57BL/6J"
                     /citation=[1]
                     /rearranged
                     /note="AIRR_READ_COUNT:123”
     V_region        1..324
     V_segment       1..257
                     /gene="IGHV1-34"
                     /allele="01"
                     /db_xref="IMGT/LIGM:AC073565"
     D_segment       266..272
                     /gene="IGHD2-2"
                     /allele="01"
                     /db_xref="IMGT/LIGM:AJ851868"
     J_segment       291..324
                     /gene="IGHJ4"
                     /allele="01"
                     /db_xref="IMGT/LIGM:V00770"
     CDS             <258..>290
                     /codon_start=1
                     /function="JUNCTION"
                     /inference="COORDINATES:nucleotide motif:IgBLAST:1.6"
                     /translated="CARAGVYDGYTMDYW"
     C_region        325..420
                     /gene="Ighg2c"
ORIGIN
        1 agcctggggc ttcagtgaag atgtcctgca aggcttctgg ctacacattc actgactata
       61 acatacactg ggtgaagcag agccatggaa agagccttga gtggattgca tatattaatc
      121 ctaacaatgg tggttatggc tataacgaca agttcaggga caaggccaca ttgactgtcg
      181 acaggtcatc caacacagcc tacatggggc tccgcagcct gacctctgag gactctgcag
      241 tctattactg tgcaagagcg ggagtttacg acggatatac tatggactac tggggtcaag
      301 gaacctcagt caccgtctcc tcagccaaaa caacagcccc atcggtctat ccactggccc
      361 ctgtgtgtgg aggtacaact ggctcctcgg tgactctagg atgcctggtc aagggcaact
//
```


### Example record (ENA format) ###

```
ID   AB123456; SV 7; linear; mRNA; EST; MUS; 420 BP.
XX
AC   AB123456;
XX
DT   01-JAN-2000 (Rel. 001, Created)
DT   01-JAN-2015 (Rel. 101, Last updated, Version 7)
XX
DE   <free text description>
XX
KW   <other keywords>; AIRR.
XX
OS   Mus musculus
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
OC   Mammalia; Eutheria; Euarchontoglires; Glires; Rodentia;
OC   Sciurognathi; Muroidea; Muridae; Murinae; Mus.
XX
RN   [1]
RA   Stibbons P.;
RT   ;
RP   1-420
RL   Submitted (01-JAN-2000) to the INSDC.
RL   Center for Transcendental Immunology, Unseen University,
RL   Ankh-Morpork, 12345, DISCWORLD.
XX
RN   [2]
RA   Stibbons P.;
RT   Section 5 information for experiment FOO1;
RL   published (01-JAN-2000) on Zenodo
RX   DOI; 10.1000/0000-12345678.
XX
DR   BioProject; PRJNA000001.
DR   BioSample; SAMN000001.
DR   SRA; SRR0000001.
XX
FH   Key        	Location/Qualifiers
FH
FT   source           1..420
FT                    /organism="Mus musculus"
FT                    /mol_type="mRNA"
FT                    /strain=”C57BL/6J”
FT                    /citation=[2]
FT                    /rearranged
FT                    /note="AIRR_READ_COUNT:123”
FT   V_region         1..324
FT   V_segment        1..257
FT                    /gene=”IGHV1-34”
FT                    /allele="01"
FT                    /db_xref=”IMGT/LIGM:AC073565”
FT   D_segment        266..272
FT                    /gene=”IGHD2-2”
FT                    /allele="01"
FT                    /db_xref=”IMGT/LIGM:AJ851868”
FT   J_segment        291..324
FT                    /gene=”IGHJ4”
FT                    /allele="01"
FT                    /db_xref=”IMGT/LIGM:V00770”
FT   CDS              <258..>290
FT                    /codon_start=1
FT                    /function=”JUNCTION”
FT                    /inference="COORDINATES:nucleotide motif:IgBLAST:1.6"
FT                    /translated="CARAGVYDGYTMDYW"
FT   C_region         325..420
FT                    /gene=”Ighg2c”
XX
SQ   Sequence 420 BP; 108 A; 108 C; 109 G; 95 T; 0 other;
    agcctggggc ttcagtgaag atgtcctgca aggcttctgg ctacacattc actgactata       60
    acatacactg ggtgaagcag agccatggaa agagccttga gtggattgca tatattaatc       120
    ctaacaatgg tggttatggc tataacgaca agttcaggga caaggccaca ttgactgtcg       180
    acaggtcatc caacacagcc tacatggggc tccgcagcct gacctctgag gactctgcag       240
    tctattactg tgcaagagcg ggagtttacg acggatatac tatggactac tggggtcaag       300
    gaacctcagt caccgtctcc tcagccaaaa caacagcccc atcggtctat ccactggccc       360
    ctgtgtgtgg aggtacaact ggctcctcgg tgactctagg atgcctggtc aagggcaact       420
//
```


### Glossary ###

* MUST / REQUIRED: Indicates that an element or action is necessary to conform to the standard.
* SHOULD / RECOMMENDED: Indicates that an element or action is considered to be best practice by AIRR, but not necessary to conform to the standard.
* CAN / OPTIONAL: Indicates that it is at the discretion of the user to use an element or perform an action.
* MUST NOT / FORBIDDEN: Indicates that an element or action will be in conflict with the standard.


### Abbreviations ###

* AA: amino acid
* bp: base pair
* DOI: digital object identifier
* FT: INSDC Feature Table
* INSDC: International Nucleotide Sequence Database Collaboration
* SRA: sequence read archive
