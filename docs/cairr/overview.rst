CAIRR Pipeline 
=====================

**The CAIRR pipeline for submitting standards-compliant B and T cell receptor repertoire sequencing studies to the NCBI**

**Quick Summary**

Just want to get to it? Here is a 2-minute YouTube video.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Db5WqHUgpOI?ecver=1" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

1- Go to http://cairr.miairr.org to start a metadata instance. Create an account/log in to CEDAR if you need to.

2- Fill out your metadata.

3- Return to your Workspace and select the metadata you just created. 

4- To submit your metadata and associated data files, click on the Submit to Repository button in the toolbar . 

   .. image:: ./images/cedar_repo_icon.png

5- Choose your computer files to submit, then click “SUBMIT”.


You should see the files load into CEDAR, which will immediately upload them into NCBI. (Note: CEDAR does not save your data files, only your metadata.) Error messages will be reported initially via CEDAR, and later via the email you provided.

**CREATE AIRR METADATA** 

Clicking on the following link will open up a metadata form in CEDAR for you to enter your AIRR metadata.

http://cairr.miairr.org

For more details, read on.

**Introduction**

AIRR sequencing (AIRR-seq) has tremendous potential to understand the dynamics of the immune repertoire in vaccinology, infectious disease, autoimmunity, and cancer biology. The adaptation of high-throughput sequencing (HTS) for AIRR (Adaptive Immune Receptor Repertoire) studies has made possible to characterize the AIRR at unprecedented depth and the outcome of such sequencing produces big data. Effective sharing of AIRR-seq big data could potentially reveal amazing scientific insights. The AIRR Community has proposed MiAIRR (Minimum information about an Adaptive Immune Receptor Repertoire Sequencing Experiment), a standard for reporting AIRR-seq studies. The MiAIRR standard has been implemented using the National Center for Biotechnology Information (NCBI) repositories. Submissions of AIRR-seq data to the NCBI repositories typically use a combination of web-based and flat-file templates and include only a minimal amount of terminology validation. As a result, AIRR-seq studies  at the NCBI are often described using inconsistent terminologies, limiting scientists’ ability to access, find, interoperate, and reuse the data sets and to understand how the experiments were performed. CEDAR (Center for Expanded Data Annotation and Retrieval) develops technologies involving the use of data standards and ontologies to improve metadata quality. In order to improve metadata quality and ease AIRR-seq study submission process, we have developed an AIRR-seq data submission pipeline named CEDAR-AIRR (CAIRR). CAIRR leverages CEDAR’s technologies to:  i) create web-based templates whose entries are controlled by ontology terms, ii) generate and validate metadata and iii) submit the ontology-linked metadata and sequence files (FASTQ) to the NCBI BioProject, BioSample, and Sequence Read Archive (SRA) databases. Thus, CAIRR provides a web-based metadata submission interface that supports compliance with MiAIRR standards. The interface enables ontology-based validation for several data elements, including: organism, disease, cell type and subtype, and tissue. This pipeline will facilitate the NCBI submission process and improve the metadata quality of AIRR-seq studies. 

**Submission Process**

You will need a CEDAR system account; you can self-register at  https://cedar.metadatacenter.org.  You will also need the identifier of a BioProject already entered in the NCBI BioProject database. (Soon CEDAR will allow you to create a BioProject, but not quite yet!)

**Submission Steps**

Create your metadata. Go to http://cairr.miairr.org, and CEDAR should open in your browser. (If you are not already logged in, you may need to log in before being redirected to the metadata page.) It will look something like this. 


   .. image:: ./images/miairr_cedartemplate.png


If you do not want your metadata to be public immediately in NCBI, fill out the Submissions Release Data field at the top of the form. Then click on any of the three metadata sections to open them up.

Note that our BioProject metadata you enter can not be submitted to NCBI yet, but soon we will enable that service; meanwhile we are saving this information in CEDAR.

Click on the SAVE button often; if you navigate away from the page or close the page your unsaved changes will be lost (after a warning). Use VALIDATE to validate your metadata via NCBI’s validation service. When done, use the left arrow at the top to navigate back to your Workspace. You should see your latest saved metadata there.

**Submit your metadata**

From your Workspace in CEDAR, select your metadata instance. You should now be able to click on the activated Submit to Repository button. You will be prompted to specify your data files to upload. (Their names should match the names you entered in the SRA section of the form.) Finally, click on the SUBMIT button. When you complete the submission process, CEDAR will display messages indicating completion results as they are logged by NCBI. (If the upload icon is gray  instead of white, you probably haven’t selected an NCBI-eligible metadata form.)

**Cite MiAIRR Pipeline**

Bukhari, Syed Ahmad Chan, Martin J. O'Connor, Marcos Martínez-Romero, Attila L. Egyedi, Debra Debra Willrett, John Graybeal, Mark A. Musen, Florian Rubelt, Kei H. Cheung, and Steven H. Kleinstein. "The CAIRR pipeline for submitting standards-compliant B and T cell receptor repertoire sequencing studies to the NCBI." Frontiers in Immunology 9 (2018): 1877. DOI: 10.3389/fimmu.2018.01877 (now in press)


**Tell Us About It**

Please let us know how it went!  If you are willing, we’d love to have your comments in a `short survey <https://www.surveymonkey.com/r/your-metadata-experience>`_, it should just take 5 minutes or so. 

We also welcome entry of issues and requests in our `github repository issues <https://github.com/metadatacenter/cedar-project/issues>`_, and emails can be sent to cedar-users@lists.stanford.edu. Both of these resources are publicly visible. 
