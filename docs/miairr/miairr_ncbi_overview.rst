.. _MiAIRR_NCBI:

=============================
MiAIRR-to-NCBI Implementation
=============================

:Authors: Christian E. Busse, Florian Rubelt and Syed Ahmad Chan Bukhari

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

   guide_miairr_ncbi
   manual_miairr_ncbi
   specification_miairr_ncbi

Introduction
============

The MiAIRR standard (minimal information about adaptive immune receptor
repertoires) is a minimal reporting standard for experiments using
sequencing-based technologies to study adaptive immune receptors (e.g. T cell
receptors or immunoglobulins). It was developed by the `AIRR Community Minimal
Standards Working Group`_ of the `Adaptive Immune Receptor Repertoire (AIRR)
Community`__ [Breden_2017]_. The current version (1.0) was ratified by the AIRR
Community and published in 2017 [Rubelt_2017]_. MiAIRR requires researchers to
report six sets of information:

1. study, subject, diagnosis & intervention
2. sample collection
3. sample processing and sequencing
4. raw sequencing data
5. data processing
6. processed sequences with a basic analysis results

However, MiAIRR only describes the mandatory data items that have to be
reported, but neither provides details how and where to deposit data nor
specifies data types and formats. Therefore this document aims to
provide both a submission manual for users as well as a detailed data
specification for developers.

.. _`AIRR Community Minimal Standards Working Group`:
   http://airr-community.org/working_groups/minimal_standards

.. __: http://airr-community.org

