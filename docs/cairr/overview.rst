.. _CAIRR_Pipeline:

==============
CAIRR Pipeline 
==============

Introduction: The CAIRR pipeline for submitting standards-compliant B and T cell receptor repertoire sequencing studies to the NCBI
-----------------------------------------------------------------------------------------------------------------------------------

AIRR sequencing (AIRR-seq) has tremendous potential to understand the dynamics
of the immune repertoire in vaccinology, infectious disease, autoimmunity, and
cancer biology. The adaptation of high-throughput sequencing (HTS) for AIRR
(Adaptive Immune Receptor Repertoire) studies has made possible to characterize
the AIRR at unprecedented depth and the outcome of such sequencing produces big
data. Effective sharing of AIRR-seq big data could potentially reveal amazing
scientific insights. The AIRR Community has proposed MiAIRR (Minimum
information about an Adaptive Immune Receptor Repertoire Sequencing
Experiment), a standard for reporting AIRR-seq studies. The MiAIRR standard has
been implemented using the National Center for Biotechnology Information (NCBI)
repositories. Submissions of AIRR-seq data to the NCBI repositories typically
use a combination of web-based and flat-file templates and include only a
minimal amount of terminology validation. As a result, AIRR-seq studies  at the
NCBI are often described using inconsistent terminologies, limiting scientists'
ability to access, find, interoperate, and reuse the data sets and to
understand how the experiments were performed. CEDAR (Center for Expanded Data
Annotation and Retrieval) develops technologies involving the use of data
standards and ontologies to improve metadata quality. In order to improve
metadata quality and ease AIRR-seq study submission process, we have developed
an AIRR-seq data submission pipeline named CEDAR-AIRR (CAIRR). CAIRR leverages
CEDAR's technologies to:  i) create web-based templates whose entries are
controlled by ontology terms, ii) generate and validate metadata and iii)
submit the ontology-linked metadata and sequence files (FASTQ) to the NCBI
BioProject, BioSample, and Sequence Read Archive (SRA) databases. Thus, CAIRR
provides a web-based metadata submission interface that supports compliance
with MiAIRR standards. The interface enables ontology-based validation for
several data elements, including: organism, disease, cell type and subtype, and
tissue. This pipeline will facilitate the NCBI submission process and improve
the metadata quality of AIRR-seq studies. 

Submission Steps
----------------

The submission steps are described in the `MiAIRR-to-NCBI Submission Manual
(Option 1. Submission via the CEDAR system)
<../miairr/manual_miairr_ncbi.rst#option-1-submission-via-the-cedar-system-cairr-submission-pipeline>`_.
You will need a CEDAR system account; you can self-register at
https://cedar.metadatacenter.org.  You will also need the identifier of a
BioProject already entered in the NCBI BioProject database.

Citing the MiAIRR Pipeline
--------------------------

Bukhari, Syed Ahmad Chan, Martin J. O'Connor, Marcos Martínez-Romero, Attila L.
Egyedi, Debra Debra Willrett, John Graybeal, Mark A. Musen, Florian Rubelt, Kei
H. Cheung, and Steven H. Kleinstein. `The CAIRR pipeline for submitting
standards-compliant B and T cell receptor repertoire sequencing studies to the
NCBI <https://www.ncbi.nlm.nih.gov/pubmed/30166985>`_. Frontiers in Immunology
9 (2018): 1877. DOI: 10.3389/fimmu.2018.01877

Tell Us About It
----------------

Please let us know how it went!  If you are willing, we would love to have your
comments in a `short survey
<https://www.surveymonkey.com/r/your-metadata-experience>`_, it should just
take 5 minutes or so. 

We also welcome entry of issues and requests in our `github repository issues
<https://github.com/metadatacenter/cedar-project/issues>`_, and emails can be
sent to cedar-users@lists.stanford.edu. Both of these resources are publicly
visible. 

Support or Contact
------------------

Having trouble with NCBI submission process through our pipeline? Please email
to `Syed Ahmad Chan Bukhari <mailto:ahmad.chan@yale.edu>`_ or to `Marcos
Martínez-Romero <mailto:marcosmr@stanford.edu>`_ and we will help you sort it
out.
