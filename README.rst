=============================
AIRR Community Data Standards
=============================

Introduction
============

One of the core initiatives of the Adaptive Immune Receptor Repertoire
(AIRR) Community [Breden_2017]_ has been to develop standards regarding
the content and format of metadata associated with AIRR sequencing
datasets. The primary aim of this effort is to make published AIRR
datasets `FAIR`_ (findable, accessible, interoperable, reusable). This
work has been a joint effort between the AIRR Community's `Minimal
Standards`_ and `Data Representation`_ Working Groups. 

.. _`FAIR`: https://www.force11.org/group/fairgroup/fairprinciples
.. _`Minimal Standards`: https://www.antibodysociety.org/airrc/working_groups/minimal_standards
.. _`Data Representation`: https://www.antibodysociety.org/database-representation-working-group


The MiAIRR Data Standard
========================

In order to support FAIR-ness, reproducibility, quality control, and
data deposition in a common repository, the AIRR Community has agreed to
six high-level data sets that will guide the publication, curation and
sharing of AIRR-seq data and metadata:

-  study and subject

-  sample collection

-  sample processing and sequencing

-  raw sequence reads

-  processing of sequence data

-  processed AIRR sequences

These data sets and their associated individual items are referred to as
**MiAIRR**, the Minimum information about an Adaptive Immune Receptor
Repertoire sequencing experiment. The MiAIRR data standard has recently
been published together with a first implementation using the NCBI
repository structure [Rubelt_2017]_. For further information, including
a submission guide and a detailed specification, see `here`__.

.. __: https://docs.airr-community.org/en/latest/miairr/overview.html


AIRR Standardized Data Representation
=====================================

The standardarized data representation was first published in 2018
[Vander_Heiden_2018]_, a current version of the schema can be found
`here`__.

.. __: https://github.com/airr-community/airr-standards/blob/master/specs/airr-schema.yaml


Implementations
===============

-  `NCBI-based`_
-  `AIRR Common Repository`_ - *in development*

.. _`NCBI-based`: https://docs.airr-community.org/en/latest/miairr/miairr_ncbi_overview.html
.. _`AIRR Common Repository`: https://www.antibodysociety.org/airrc/working_groups/repository


Contributions
=============

The AIRR Community is an open initiative and we welcome all
contributions. Please review our `development process`_ before
contributing changes.

.. _`development process`: https://github.com/airr-community/airr-standards/tree/master/CONTRIBUTING.rst


Contact and Build Status
========================

Please report problems, bugs, comments or enhancement requests using
the `issue tracker`_.

.. _`issue tracker`: https://github.com/airr-community/airr-standards/issues
.. https://waffle.io/airr-community/airr-standards

.. image:: https://travis-ci.org/airr-community/airr-standards.svg?branch=master
   :target: https://travis-ci.org/airr-community/airr-standards


References
==========

.. [Vander_Heiden_2018] Vander Heiden JA *et al*. AIRR Community
   Standardized Representations for Annotated Immune Repertoires. Front
   Immunol 9:2206 (2018) `[PMID: 30323809]`_ `[DOI: 10.3389/fimmu.2018.02206]`_ `[PubMed Central: PMC6173121]`_
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
   (2015-2019) `[DOI: 10.5281/zenodo.1185414]`_
.. _`[DOI: 10.5281/zenodo.1185414]`: https://doi.org/10.5281/zenodo.1185414


License
=======

(c) 2015 - 2019 by Syed Ahmad Chan Bukhari, Jean-Philippe Bürckert,
Christian E. Busse, Scott Christley, Brian Corrie, Lindsay G. Cowell,
Uri Hershberg, Steven H. Kleinstein, Susanna Marquez, Frederick A. Matsen IV,
Uri Laserson, Marie-Paule Lefranc, Eline T. Luning Prak, Florian Rubelt,
Jason Vander Heiden, Corey T. Watson

.. image:: https://i.creativecommons.org/l/by/4.0/80x15.png
   :target: https://creativecommons.org/licenses/by/4.0/

This work is licensed under a `Creative Commons Attribution 4.0
International License`_.

.. _`Creative Commons Attribution 4.0 International License`: http://creativecommons.org/licenses/by/4.0/
