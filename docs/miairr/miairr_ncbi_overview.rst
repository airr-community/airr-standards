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
reported, but neither provides details how and where to deposit data nor
specifies data types and formats. Therefore this document aims to
provide both a submission manual for users as well as a detailed data
specification for developers.

.. __: http://airr-community.org

