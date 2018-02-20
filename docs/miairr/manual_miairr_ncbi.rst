================================================
MiAIRR-to-NCBI Submission Manual
================================================

:Authors: Christian E. Busse, Florian Rubelt and Syed Ahmad Chan Bukhari

Preface
=======

The MiAIRR standard
-------------------

The MiAIRR standard (minimal information about adaptive immune receptor
repertoires) is a minimal reporting standard for experiments using
sequencing-based technologies to study adaptive immune receptors (e.g.
T cell receptors or immunoglobulins). It is developed and maintained by
the Minimal Standards Working Group of the `Adaptive Immune Receptors
Repertoire (AIRR) Community`__ [Breden_2017]_. The current version (1.0)
of the standard has been recently published [Rubelt_2017]_ and was
passed by the general assembly at the annual AIRR Community meeting in
December 2017. MiAIRR requires researchers to report six sets of
information:

1. study, subject, diagnosis & intervention
2. sample collection
3. sample processing and sequencing
4. raw sequencing data
5. data processing
6. processed sequences with a basic analysis results

However, MiAIRR only describes the mandatory data items that have to be
reported, but neither provides details how and where to deposit data
nor specifies data types and formats. Therefore this document aims to
provide both a submission manual for users as well as a detailed data
specification for developers.

.. __: http://airr-community.org

Scope of this document
----------------------

Provide a user manual describing the submission of AIRR data using
the NCBI reference implementation described in [Rubelt_2017]_.
This implementation uses NCBI’s BioProject, BioSample, Sequence Read Archive (SRA)
and GenBank repositories and metadata standards to report AIRR data.

Data Submission Manual
======================

To facilitate AIRR data submissions to NCBI repositories, we have
developed the NCBI-compliant metadata submission templates both for
single and bulk AIRR data submissions. NCBI provides a web-based
interface to create a BioProject and allows to BioSample, Sequence Read
Archive (SRA) and GenBank metadata via tab-delimited files for single
BioProject related data files submission. To support the bulk submission
of metadata through the FTP, NCBI also has established an XML schema.
This will promote the standard and provide important feedback for its
iterative improvement. Since we propose to include a combination of raw
and processed sequence data, the AIRR standard will sometimes need to be
distributed and linked across multiple repositories (e.g., data in SRA
linked to related data in GenBank). In addition, the data elements that
comprise the standard will be mapped to ontologies in BioPortal through
NIH CDE (Common Data Element) terms. These linkages will support more
sophisticated validation and logical inference.

MiAIRR data submission to BioProject, BioSample and SRA
-------------------------------------------------------

Submissions via the web interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submitting AIRR data and associated metadata to the Bioproject,
BioSample and SRA repositories via NCBI’s web interface follows in
general the submission procedure described in
[NCBI_NBK47528]_, but uses AIRR-specific template
for metadata submission:

#. Go to https://submit.ncbi.nlm.nih.gov/subs/sra/ and login with your
   NCBI account (create an account if necessary).

#. Click on "create new submission". You will see a form as below.
   Fill the form with required information and click on "continue".
   .. image:: images/bioproject.png

#. If you are submitting for the first time, check “Yes” on the "new
   BioProject" or "new BioSample" options to create a new project or
   sample, respectively.
   .. image:: images/SRA.png

#. Fill in the project information. Add as much relevant information
   you can add in description. It will help later in searching the
   particular submission.
   .. image:: images/fillproject.png

#. The AIRR BioSample template is not yet listed on the NCBI website.
   The template sheet ``AIRR_BioSample_V1.0.xls`` can be downloaded from
   https://github.com/airr-community/airr-standards/tree/master/NCBI_implementation/NCBI%20Templates.
   Fill in the required field and save the file as *tab-delimited* text
   file (.TSV format), then upload it.

#. To submit the SRA metadata use the ``AIRR_SRA_v1.0.xls`` file. Make
   sure that the column ``sample_name`` uses sample names that match the
   record in the BioSample template (if new BioSamples are being
   submitted) or a previously entered record. Also this file must be
   saved as *tab-delimited* text file for upload.

#. Submit the raw sequence file.

#. Complete the submission.

Submissions via an XML template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the web interface, NCBI provides an FTP-based solution to
submit bulk metadata. The corresponding AIRR XML templates can be found
under
https://github.com/airr-community/airr-standards/tree/master/NCBI_implementation/NCBI-XML%20Templates.
Otherwise users should refer to the current SRA file upload manual
https://www.ncbi.nlm.nih.gov/sra/docs/submitfiles/. Users planning to
frequently submit AIRR-seq data to SRA using scripts to generate the XML
files MUST ensure that the templates are identical to the current
upstream version on Github.


MiAIRR data submission to GenBank/TLS
-------------------------------------

Processed sequence data will be submitted to the "Targeted Locus Study"
(TLS) section of GenBank. The details of this submission process are
currently still finalized. Basically the procedure is identical to a
conventional GenBank submission with the exception of additional
keywords marking it as TLS submission.

Non-functional records should be removed before the data submission or
use an alternative annotation as described in the specification
document.

GenBank provides multiple tools (GUI and command-line) to submit data:

-  BankIt, a web-based submission tool with wizards to guide the
   submission process

-  Sequin, NCBI’s stand-alone submission tool with wizards to guide the
   submission process is available by FTP for use on for Windows, macOS
   and Unix platforms.

-  Tbl2asn is the recommended tool for the bulk data submission. It is a
   command-line program that automates the creation of sequence records
   files (.sqn) for submission to GenBank, driven by multiple tabular
   unput data files. Documentation and download options can be found
   under https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2/.

