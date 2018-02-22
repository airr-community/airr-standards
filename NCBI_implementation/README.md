![Image](https://github.com/airr-community/airr-standards/raw/master/images/miairr_logo.png)

_Minimum information about an Adaptive Immune Receptor Repertoire Sequencing Experiment_

***

### Guide for submission of AIRR-seq data to NCBI

This site provides a detailed “how-to” guide for submission of AIRR-seq data to **NCBI repositories** (BioProject,
BioSample, SRA and GenBank). For other implementations of the MiAIRR standard see
[here](https://github.com/airr-community/airr-standards).

One of the primary initiatives of the AIRR (Adaptive Immune Receptor Repertoire) Community has been to develop a set of
metadata standards for the submission of immune receptor repertoire sequencing datasets. This work has been carried out
by the AIRR Community Standards Working Group. In order to support reproducibility, standard quality control, and data
deposition in a common repository, the AIRR Community has agreed to six high-level data sets that will guide the
publication, curation and sharing of AIRR-Seq data and metadata: Study and subject, sample collection, sample
processing and sequencing, raw sequences, processing of sequence data, and processed AIRR sequences. The detailed data
elements within these sets are defined
[here](https://github.com/airr-community/airr-standards/blob/master/AIRR_Minimal_Standard_Data_Elements.tsv). The
association between these AIRR sets, the associated data elements, and each of the NCBI repositories is shown below:

![Image](https://github.com/airr-community/airr-standards/raw/master/images/MiAIRR_data_elements_NCBI_targets.png)

Submission of AIRR sequencing data and metadata to NCBI's public data repositories consists of five sequential steps:

1. Submit study information to [NCBI BioProject](https://submit.ncbi.nlm.nih.gov/subs/bioproject/) using the NCBI web interface.
2. Submit sample-level information to the [NCBI BioSample repository](https://submit.ncbi.nlm.nih.gov/subs/biosample/) using the [AIRR-BioSample templates](https://github.com/airr-community/airr-standards/raw/master/NCBI_implementation/templates_XLS/AIRR_BioSample_v1.0.xls).
3. Submit raw sequencing data to [NCBI SRA](https://submit.ncbi.nlm.nih.gov/subs/sra/) using the [AIRR-SRA data templates](https://github.com/airr-community/airr-standards/raw/master/NCBI_implementation/templates_XLS/AIRR_SRA_v1.0.xls).
4. Generate a DOI for the protocol describing how raw sequencing data were processed using [Zenodo](https://zenodo.org) or an equivalent DOI-granting service.
5. Submit processed sequencing data with sequence-level annotations to [GenBank](https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2/) using AIRR feature tags.

For step-by-step instructions on carrying out theses steps an AIRR study submission, see [here](http://docs.airr-community.org/en/latest/miairr/overview.html).


### How to cite?

Rubelt F _et al._
Adaptive Immune Receptor Repertoire Community recommendations for sharing immune-repertoire sequencing data.
Nat Immunol 18:1274 (2017)
[[PubMed]](https://www.ncbi.nlm.nih.gov/pubmed/29144493) [[DOI]](https://doi.org/10.1038/ni.3873) [[SharedIt - free to read]](https://rdcu.be/E7sS)

<!---
The following link could give a false impression on contribution to the MiAIRR standard, therefore please keep it
commented out until the actual MiAIRR publication it out and can be referenced too.
[![DOI](https://zenodo.org/badge/104967269.svg)](https://zenodo.org/badge/latestdoi/104967269)
-->


### Further information

For further information on this and other AIRR Community Data Standards see [here](https://github.com/airr-community/airr-standards).
