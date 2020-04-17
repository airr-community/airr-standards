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

    VDJServer Community Data Portal <../miairr/vdjserver> (upload your data and publish for others to access)
    
.. toctree::
    :maxdepth: 1
    :caption: iReceptor Turnkey Repository

    iReceptor Turnkey Repository <../miairr/ireceptor> (install, host and manage your own repository)

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

The AIRR Data Commons is a network of distributed repositories that store AIRR-seq data and
adhere to the AIRR Community standards. We define the AIRR Data Commons as consisting of
the set of repositories that:

+ adhere to the `AIRR Common Repositories Working Group recommendations`_ for promoting, sharing, and use of AIRR-seq data, and
+ that implement the `ADC API <../api/adc_api.rst>`_ as a programmatic mechanism to access that data.

More information on repositories in the AIRR Data Commons and how to query these repositories
can be found on the `AIRR Data Commons page <../api/adc.rst>`_.

.. _`AIRR Common Repositories Working Group recommendations`: https://github.com/airr-community/common-repo-wg/blob/master/recommendations.md

**Other Public AIRR-Seq Repositories**

There are additional data repositories that provide access to AIRR-seq data but which
did not implement the ADC API for programmatic access. Information about some of these
repositories are provided in a `B-T.CR forum post`_.

.. _`B-T.CR forum post`: https://b-t.cr/t/publicly-available-airr-seq-data-repositories/610

**Germline Gene Inference and Usage**

+ :ref:`OGRDB <OGRDB>` provides a list of alleles affirmed by the AIRR Community's
  Inferred Allele Review Committee, together with supporting information.

+ `VDJbase`_ provides gene usage information derived from a growing base of AIRR-seq repertoires,
  including inferred genotypes and haplotypes.

.. _`VDJbase`: https://www.vdjbase.org
