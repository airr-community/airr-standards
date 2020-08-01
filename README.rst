=============================
AIRR Community Data Standards
=============================

Introduction
============

One of the core initiatives of the `Adaptive Immune Receptor Repertoire
(AIRR) Community`__ [Breden_2017]_ has been to develop standards regarding
the content and format of metadata associated with AIRR sequencing
datasets. The primary aim of this effort is to make published AIRR
datasets `FAIR`_ (findable, accessible, interoperable, reusable). This
work has been a joint effort between the AIRR Community's `Minimal
Standards`_ and `Data Representation`_ Working Groups. 

.. __: https://www.antibodysociety.org/the-airr-community/
.. _`FAIR`: https://www.go-fair.org/fair-principles/
.. _`Minimal Standards`: https://www.antibodysociety.org/the-airr-community/airr-working-groups/minimal_standards/
.. _`Data Representation`: https://www.antibodysociety.org/the-airr-community/airr-working-groups/data_representation/


The MiAIRR Data Standard
========================

In order to support FAIR-ness, reproducibility, quality control, and
data deposition in a common repository, the AIRR Community has agreed to
six high-level data sets that will guide the publication, curation and
sharing of AIRR-seq data and metadata:

*  study and subject
*  sample collection
*  sample processing and sequencing
*  raw sequence reads
*  processing of sequence data
*  processed AIRR sequences

These data sets and their associated individual items are referred to as
**MiAIRR**, the Minimum information about an Adaptive Immune Receptor
Repertoire sequencing experiment. The MiAIRR data standard has recently
been published together with a first implementation using the NCBI
repository structure [Rubelt_2017]_. For further information, including
a submission guide and a detailed specification, see the
`respective section`_ of the `AIRR Standards documentation`_.

.. _`respective section`: https://docs.airr-community.org/en/stable/miairr/introduction_miairr.html
.. _`AIRR Standards documentation`: https://docs.airr-community.org/en/stable/


AIRR Standardized Data Representation
=====================================

The standardarized data representation was first published in 2018
[Vander_Heiden_2018]_, a current version of the schema can be found
`here`__.

.. __: https://github.com/airr-community/airr-standards/blob/master/specs/airr-schema.yaml


AIRR Data Commons API
=====================

The `AIRR Data Commons`_ (ADC) `API`_ was published in 2020
[Christley_2020]_.

.. _`AIRR Data Commons`: https://docs.airr-community.org/en/stable/api/adc.html
.. _`API`: https://docs.airr-community.org/en/stable/api/adc_api.html


Implementations
===============

*  `NCBI-based`_
*  `AIRR Common Repository`_ - *in development*

.. _`NCBI-based`: https://docs.airr-community.org/en/stable/miairr/miairr_ncbi_overview.html
.. _`AIRR Common Repository`: https://www.antibodysociety.org/the-airr-community/airr-working-groups/repository/


Contributions
=============

The AIRR Community is an open initiative and we welcome all
contributions. Please review our `development process`_ before
contributing changes.

.. _`development process`: https://github.com/airr-community/airr-standards/tree/master/CONTRIBUTING.rst


Build Status, Issues and Archive
================================

.. image:: https://travis-ci.org/airr-community/airr-standards.svg?branch=master
   :target: https://travis-ci.org/airr-community/airr-standards

Please report problems, bugs, comments or enhancement requests using
the `issue tracker`_. Official releases are archived and DOI referenced
via Zenodo [Zenodo_1185414]_.

.. _`issue tracker`: https://github.com/airr-community/airr-standards/issues


References
==========

.. [Christley_2020] Christley S *et al*. The ADC API: A Web API for the
   Programmatic Query of the AIRR Data Commons. Front Big Data (2020)
   `[DOI: 10.3389/fdata.2020.00022]`_
.. _`[DOI: 10.3389/fdata.2020.00022]`: https://doi.org/10.3389/fdata.2020.00022

.. [Vander_Heiden_2018] Vander Heiden JA *et al*. AIRR Community
   Standardized Representations for Annotated Immune Repertoires. Front
   Immunol 9:2206 (2018) `[PMID: 30323809]`_
   `[DOI: 10.3389/fimmu.2018.02206]`_ `[PubMed Central: PMC6173121]`_
.. _`[PMID: 30323809]`: https://www.ncbi.nlm.nih.gov/pubmed/30323809
.. _`[DOI: 10.3389/fimmu.2018.02206]`: https://doi.org/10.3389/fimmu.2018.02206
.. _`[PubMed Central: PMC6173121]`: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6173121

.. [Rubelt_2017] Rubelt F *et al*. AIRR Community Recommendations for
   Sharing Immune Repertoire Sequencing Data. Nat Immunol 18:1274
   (2017) `[PMID: 29144493]`_ `[DOI: 10.1038/ni.3873]`_ `[PubMed Central: PMC5790180]`_
.. _`[PMID: 29144493]`: https://www.ncbi.nlm.nih.gov/pubmed/29144493
.. _`[DOI: 10.1038/ni.3873]`: https://doi.org/10.1038/ni.3873
.. _`[PubMed Central: PMC5790180]`: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5790180

.. [Breden_2017] Breden F *et al*. Reproducibility and Reuse of
   Adaptive Immune Receptor Repertoire Data. Front Immunol 8:1418
   (2017) `[PMID: 29163494]`_ `[DOI: 10.3389/fimmu.2017.01418]`_ `[PubMed Central: PMC5671925]`_
.. _`[PMID: 29163494]`: https://www.ncbi.nlm.nih.gov/pubmed/29163494
.. _`[DOI: 10.3389/fimmu.2017.01418]`: https://doi.org/10.3389/fimmu.2017.01418
.. _`[PubMed Central: PMC5671925]`: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5671925

.. [Zenodo_1185414] Release archive of the AIRR Standards repository.
   (2015-2020) `[DOI: 10.5281/zenodo.1185414]`_
.. _`[DOI: 10.5281/zenodo.1185414]`: https://doi.org/10.5281/zenodo.1185414


License
=======

(c) 2015 - 2020 by Francisco Arcila, Syed Ahmad Chan Bukhari,
Jean-Philippe Bürckert, Christian E. Busse, Scott Christley, Brian
Corrie, Lindsay G. Cowell, Srilakshmy L. Harikrishnan, Uri Hershberg,
Steven H. Kleinstein, Susanna Marquez, Frederick A. Matsen IV,
Uri Laserson, Marie-Paule Lefranc, Eline T. Luning Prak, Florian Rubelt,
Jason Vander Heiden, Corey T. Watson

.. image:: https://i.creativecommons.org/l/by/4.0/80x15.png
   :target: https://creativecommons.org/licenses/by/4.0/

This work is licensed under a `Creative Commons Attribution 4.0
International License`_.

.. _`Creative Commons Attribution 4.0 International License`: http://creativecommons.org/licenses/by/4.0/
