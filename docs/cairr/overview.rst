CAIRR Pipeline (DRAFT)
=====================

**CAIRR is a pipeline to submit MiAIRR-compliant AIRR-seq studies to the NCBI through the CEDAR workbench**

**Introduction**

AIRR sequencing (AIRR-seq) has tremendous potential to understand the dynamics of the immune repertoire in vaccinology, infectious disease, autoimmunity, and cancer biology. The adaptation of high-throughput sequencing (HTS) for AIRR (Adaptive Immune Receptor Repertoire) studies has made possible to characterize the AIRR at unprecedented depth and the outcome of such sequencing produces big data. Effective sharing of AIRR-seq big data could potentially reveal amazing scientific insights. The AIRR Community has proposed MiAIRR (Minimum information about an Adaptive Immune Receptor Repertoire Sequencing Experiment), a standard for reporting AIRR-seq studies. The MiAIRR standard has been implemented using the National Center for Biotechnology Information (NCBI) repositories. Submissions of AIRR-seq data to the NCBI repositories typically use a combination of web-based and flat-file templates and include only a minimal amount of terminology validation. As a result, AIRR-seq studies  at the NCBI are often described using inconsistent terminologies, limiting scientists’ ability to access, find, interoperate, and reuse the data sets and to understand how the experiments were performed. CEDAR (Center for Expanded Data Annotation and Retrieval) develops technologies involving the use of data standards and ontologies to improve metadata quality. In order to improve metadata quality and ease AIRR-seq study submission process, we have developed an AIRR-seq data submission pipeline named CEDAR-AIRR (CAIRR). CAIRR leverages CEDAR’s technologies to:  i) create web-based templates whose entries are controlled by ontology terms, ii) generate and validate metadata and iii) submit the ontology-linked metadata and sequence files (FASTQ) to the NCBI BioProject, BioSample, and Sequence Read Archive (SRA) databases. Thus, CAIRR provides a web-based metadata submission interface that supports compliance with MiAIRR standards. The interface enables ontology-based validation for several data elements, including: organism, disease, cell type and subtype, and tissue. This pipeline will facilitate the NCBI submission process and improve the metadata quality of AIRR-seq studies. 

**Submission Guideline**


**Before You Start**

We assume you have already obtained an account on the system you will be testing on (either CEDAR staging (https://staging.cedar.metadatacenter.edu)  or CEDAR production (https://cedar.metadatacenter.edu). If you want to test submission to the NCBI (either their test system, or their production system), you will also need a BioProject already set up. (Soon CEDAR will allow you to create a BioProject, but not quite yet!)

You should also have an email from one of us at Stanford with a CEDAR link (your template URL) to start your metadata completion process. 

**Submission Steps**


1- Click on this link `CEDAR Login <https://auth.staging.metadatacenter.org/auth/realms/CEDAR/protocol/openid-connect/auth?client_id=cedar-angular-app&redirect_uri=https%3A%2F%2Fcedar.staging.metadatacenter.org%2F&state=64bbf164-f029-4b35-bc4b-503e001f324e&nonce=269a0ee8-66e3-427a-9fcb-663e961d8608&response_mode=fragment&response_type=code&scope=openid/>`_. This will take you to the CEDAR login-in panel.

2- If you are new user user, you have to create an account or existing users will login through their account information

3- After login into the system, you will see `MiAIRR RC2 <https://cedar.staging.metadatacenter.org/dashboard?folderId=https:%2F%2Frepo.staging.metadatacenter.org%2Ffolders%2F4f2be12f-d096-4b45-8dc6-a7ec2e145f37>`_.


4- Right click on the template (MiAIRR RC2) file and click on the “populate” option from menu.

5- Enter related Metdata.

6- To upload FASTQ files, Please first save the entered metdata and go the previous window (Use Go back page option from your browser). You will see a new MiAIRR RC2 instance (filled template) will appear. Select the instance and click on the upload icon on top right cornor (in the toolbar) of the page.

7- An upload dialogue will appear, choose NCBI SRA and upload your FASTQ file. Upon submisison you will start receiving acknowledgement messages.


**Cite MiAIRR Pipeline**

To be Updated

**Tell Us About It**

Please let us know how it went. 

We also welcome entry of issues and requests in our github repository issues, and emails can be sent to cedar-users@lists.stanford.edu. 


