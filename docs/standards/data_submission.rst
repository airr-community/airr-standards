.. _Data_Submission:

=========================
Data Submission and Query
=========================

Data Submission Guides for AIRR-seq studies
-------------------------------------------

There are multiple data repositories that accept submission of AIRR-seq datasets.
Each provides different capabilities but all comply with the MiAIRR standard.

.. toctree::
    :maxdepth: 1
    :caption: National Center for Biotechnology Information (NCBI)

    MiAIRR to NCBI submission guide <../miairr/miairr_ncbi_overview>
    CEDAR's CAIRR submission pipeline <../cairr/overview>

.. toctree::
    :maxdepth: 1
    :caption: VDJServer Community Data Portal

    VDJServer Community Data Portal <../miairr/vdjserver>

Data Submission for Inferred Genes and Alleles
----------------------------------------------

In 2017, The AIRR Community established the Inferred Allele Review Committee (IARC) to
evaluate inferred alleles for inclusion in relevant germline databases. IARC has worked,
together with colleagues at IMGT and the US National Institutes of Health, to establish a
systematic submission and review process. OGRDB was created and designed to support that
process, and provide a real-time record of affirmed sequences.

.. toctree::
    :maxdepth: 1
    :caption: Inferred Immune Receptor Genes

    OGRDB <../ogrdb/ogrdb>

Data Query and Download
-----------------------

Submission of AIRR-seq datasets to public data repositories means that other
researchers can query, download and reuse that data for novel analyses.

**AIRR Data Commons**

These data repositories all implement the AIRR Data Commons (ADC) API programmatic access to
query and download AIRR-seq data. 

+ iReceptor Public Archive

+ VDJServer Community Data Portal

**Other Public AIRR-Seq Repositories**

There are additional data repositories that provide access to AIRR-seq data but which
did not implement the ADC API for programmatic access. Information about some of these
repositories are provided in a `B-T.CR forum post`_.

.. _`B-T.CR forum post`: https://b-t.cr/t/publicly-available-airr-seq-data-repositories/610

**Germline Gene Inference and Usage**

+ OGRDB <../ogrdb/ogrdb> provides a list of alleles affirmed by the AIRR Community's 
  Inferred Allele Review Committee, together with supporting information.

+ `VDJbase`_ provides gene usage information derived from a growing base of AIRR-seq repertoires,
  including inferred genotypes and haplotypes.

.. _`VDJbase`: https://www.vdjbase.org
