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


.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/watch?v=Db5WqHUgpOI" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

References
==========

.. [Rubelt_2017] Rubelt F *et al*. AIRR Community Recommendations for
   Sharing Immune Repertoire Sequencing Data. Nat Immunol 18:1274
   (2017) `DOI: 10.1038/ni.3873`_
.. _`DOI: 10.1038/ni.3873`: https://doi.org/10.1038/ni.3873

.. [Breden_2017] Breden F *et al*. Reproducibility and Reuse of
   Adaptive Immune Receptor Repertoire Data. Front Immunol 8:1418
   (2017) `DOI: 10.3389/fimmu.2017.01418`_
.. _`DOI: 10.3389/fimmu.2017.01418`: https://doi.org/10.3389/fimmu.2017.01418

.. [Zenodo_1185414] Release archive of the AIRR Standards repository.
   (2015-2018) `DOI: 10.5281/zenodo.1185414`_
.. _`DOI: 10.5281/zenodo.1185414`: https://doi.org/10.5281/zenodo.1185414
