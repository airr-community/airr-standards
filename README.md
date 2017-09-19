<img src="https://github.com/airr-community/airr-standards/blob/master/Images/miairr.png" alt="miairr" />

<p align="left"><i>Revolutizing the Immune Receptor Sequencing through Standardization</i></p>

***
## Welcome to the AIRR study submission guide

### Introduction

The AIRR Community has defined six high-level sets that will guide the publication, curation and sharing of AIRR-Seq data and metadata: Study and subject, sample collection, sample processing and sequencing, raw sequences, processing of sequence data, and processed AIRR sequences. The detailed data elements within these sets are defined  <a href="https://github.com/airr-community/airr-standards/raw/master/AIRR%20Minimal%20Standard%20Data%20Elements.xlsx">here </a>. An implementation of the AIRR data standard has been developed for the NCBI repositories (BioProject, BioSample, Sequence Read Archive (SRA) and GenBank). The association between each of these repositories and the AIRR sets is shown below:

### AIRR Community Accpted Elements

![Image](https://github.com/airr-community/airr-standards/blob/master/Images/dataelements.png)



### AIRR data submission to BioProject, BioSample and SRA

<hr>
The National Center for Biotechnology Information (NCBI) repositories constitute a major public resource for sharing diverse types of biomedical data. These repositories provide the necessary infrastructure for researchers to submit experimental data and associated metadata as part of the science-dissemination process. AIRR Minimal Standards WG has developed templates to submit AIRR data to the NCBI's BioProject, BioSample, Sequence Read Archive and GenBank (Figure below).


<img src="https://github.com/airr-community/airr-standards/blob/master/Images/airr-ncbi.png" alt="airr-ncbi" />

Follwoing is a tutorial to submit AIRR data to the NCBI

1. Go to https://submit.ncbi.nlm.nih.gov/subs/sra/ and login with your NCBI account (create an account if necessary).

2. Click on "create new submission". You will see a form as below. Fill the form with required information and click on "continue".

<img src="https://github.com/airr-community/airr-standards/blob/master/Images/manual1.png" alt="airr-ncbi" />

3. If you are submitting for the first time, check “Yes” on the "new BioProject" or "new BioSample" options to create a new project or BioSample, respectively.

<img src="https://github.com/airr-community/airr-standards/blob/master/Images/manual2.png" alt="airr-ncbi" />

4. Fill in the project information. Add as much relevant information you can add in description. It will help later in searching the particular submission.

<img src="https://github.com/airr-community/airr-standards/blob/master/Images/manual3.png" alt="airr-ncbi" />

5- The AIRR templates are not yet listed on the NCBI website. NCBI compliant AIRR templates can be download in the download section of this repository.
NCBI allows both web-based and command-line submissions and accepts .tsv files (for web-based submission) and XML (for bulk submission through command line and FTP). AIRR Minimal Standards WG is providing NCBI compliant AIRR templates  for the both types of submissions.
<a href="https://github.com/airr-community/airr-standards/raw/master/NCBI%20Templates/AIRR_BioSample_v1.0.xls">AIRR_BioSample_v1.0</a> and <a href="https://github.com/airr-community/airr-standards/raw/master/NCBI%20Templates/AIRR_SRA_v1.0.xls">AIRR_SRA_v1.0</a> are the templates (blank)  for the BioSample and SRA that you can fill-up using MS Excel. People had some difficulty in editing the files therefore we kept the MS Excel as default software to edit but **you must need to save the templates in .tsv format prior to upload at the NCBI**. 

### Filled AIRR-NCBI Metadata Examples   <a href="https://github.com/airr-community/airr-standards/blob/master/Filled_NCBI_Templates/F_AIRR_BS.tsv">BioSample</a>  <a href="https://github.com/airr-community/airr-standards/blob/master/Filled_NCBI_Templates/F_AIRR_SRA.tsv">SRA</a>

### Bulk Data Submission to the NCBI

In case you are planning to populate the AIRR template files programmatically, please use <a href="https://github.com/airr-community/airr-standards/blob/master/NCBI-XML%20Templates/AIRR_BS_SRA_v1.0.xml"> AIRR_BS_SRA_v1.0.xml</a> file (its filled with dummy data).

### AIRR data submission to GenBank

GenBank provides multiple tools (GUI and command-line) to submit data:

1- **BankIt**, a web-based submission tool with wizards to guide the submission process

2- **Sequin**, NCBI's stand-alone submission tool with wizards to guide the submission process is available by FTP for use on for Windows, macOS and Unix platforms.

3- **Tbl2asn** a command-line program, automates the creation of sequence records for submission to GenBank using many of the same functions as Sequin. It is used primarily for submission of complete genomes and large batches of sequences and is available by FTP for use on Windows, macOS and Unix platforms. Submission Portal, a unified system for multiple submission types.  Currently only ribosomal RNA (rRNA) or rRNA-ITS sequences can be submitted with the GenBank component of this tool.  This will be expanded in the future to include other types of GenBank submissions. Genome and Transcriptome Assemblies can be submitted through the Genomes and TSA portals, respectively.

4- **Barcode Submission Tool**, a web-based tool for the submission of sequences and trace read data for Barcode of Life projects based on the COI 

**Tbl2asn** is a recommended tool for the bulk submission of data. Tbl2asn is a command-line program that automates the creation of sequence records for
submission to GenBank. It uses many of the same functions as Sequin but is driven generally by data files. Tbl2asn generates .sqn files for submission to
GenBank. Additional manual editing is not required before submission. To prepare a tbl2asn submission please visit https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2/ 

### REQUIRED

**1- Template file containing a text ASN.1 Submit-block object (suffix .sbt).**

Creating the template file (.sbt)

*   Go to Create Submission Template page  https://submit.ncbi.nlm.nih.gov/genbank/template/submission/

*   Fill in the boxes

*   Click on "Create Template"

*   SAVE the file as template.sbt

**2 Nucleotide sequence and FASTA defline formats (.fsa)**

*   No size limit on nucleotide sequence, generally.

*   FASTA file should consist of a single definition line beginning with a '>'.

Minimum requirements for the FASTA defline are:

SeqID (sequence identifier) which is the text between the '>' and the first space. The SeqIDs limits are:
Must be <50 characters Can only include letters, digits, hyphens (-), underscores (_), periods (.), colons (:), asterisks (*), and number signs (#). Organism and related information (unless organism information is included with -j at the command line or in a .src file )

Optional defline information is in this list of source modifiers and includes:

Biological

*   strain [strain=S288C]

*   isolate [isolate=CWS1]

*   chromosome [chromosome=XVI]

Other elements

*   topology [topology=circular]

*   location [location=mitochondrion]

*   molecule [moltype=mRNA] (DNA is the default)

*   technique [tech=wgs]

*   protein name [protein=helicase] (if using -c)

*   genetic code [gcode=4]


Example FASTA:


>Sc_16 [organism=Saccharomyces cerevisiae]
tataggcgaatcgagtatattattttttctcaacatatgtat
atgaacatgagaatatatttataggaatgtataaaattgtga
cctctcctgctattttagttactgattttatgtatgtagggg
gaataggggctgcctttcttaatgcagttttaattttttctt
ttaattttttcttagtaaaattatttaaagtaaagattaatg
gaataaccattgcgcttttttttacagtttttggtttttcat
tttttggaaaaaatattttaaatattttacctttttatttag
ggggtattttatatagtatctatacttcaacagatttttctg
aacatatagttcctattgctttttcaagtgcattagcccctt
ttgtaagcagtgttgctttttatggagaaatatcctatgaaa
catcatatataaatgcaattttaattggtattttaattggtt
ttatagtggttcctttgtctaaaagtctttatgactttcatg
agggatatgatttatataatttaggttttacagcaggtt


3- Feature Table (suffix .tbl).

### AIRR suggested Feature Table to represent JUNCTION

<img src="https://github.com/airr-community/airr-standards/blob/master/Images/genbank.png" alt="genkbank" />

### How to prepare a GenBank submission. Guideline is available <a href="https://www.ncbi.nlm.nih.gov/books/NBK53709/#gbankquickstart.how_do_i_create_a_submis">here</a>

### Detailed specification
A **draft specification for AIRR Minimal Standard-compliant reporting to INSDC databases** can be found [here](https://www.overleaf.com/read/tytddwptgkhb).

### How to cite?

To be updated

### Support or Contact

If you are interested to know more about AIRR Standards or looking for help in NCBI templates. Please create an issue or send email to Ahmad
<a href="mailto:ahmad.chan@yale.edu">Syed **Ahmad** Chan Bukhari</a> or <a href="mailto:steven.kleinstein@yale.edu">Steven Kleinstein</a>
