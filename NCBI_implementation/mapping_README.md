### Introduction
The three `mapping_MiAIRR_*.tsv` tables in this directory provide the mapping scheme between the MiAIRR data elements and their respective
counterparts (hereafter "attributes") of the three NCBI repositories BioProject, BioSample and SRA.

### Table structure
The tables have five columns:

1. The field name of the MiAIRR data element as defined by the AIRR Formats WG
2. The attribute designation in the respective NCBI repository
3. The relation between MiAIRR field name and NCBI attribute:
    * `IDENTICAL  `: The identical keyword exists in MiAIRR and the NCBI repository; it defines similar content.
    * `MAPPED     `: Non-identical keywords are used by MiAIRR and NCBI to define similar content; a 1:1 mapping of the keywords is required.
    * `MAPPED_NODE`: Non-identical keywords are used by MiAIRR and NCBI to define similar content. In addition, NCBI splits the content into several
    sub-keys, which requires some string manipulation for a 1:n mapping.
    * `AIRR_CUSTOM`: The NCBI repositories does *not* specify an attribute for this content, so the MiAIRR field name is directly used as custom
    keyword.
4. Whether an attribute is required by the NCBI repository (Note that _all_ data elements are **required** by MiAIRR)
5. Notes on related attributes

### References
#### BioProject
* https://ftp.ncbi.nlm.nih.gov/bioproject/Schema.v.1.2/ (relevant information in the files `Core.xsd` and `Submission.xsd`).
