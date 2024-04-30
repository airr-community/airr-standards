.. image:: https://github.com/airr-community/airr-standards/actions/workflows/schema-test.yaml/badge.svg?branch=release-1.5
   :target: https://github.com/airr-community/airr-standards/actions/workflows/schema-test.yaml
.. image:: https://github.com/airr-community/airr-standards/actions/workflows/py-unittest.yaml/badge.svg?branch=release-1.5
   :target: https://github.com/airr-community/airr-standards/actions/workflows/py-unittest.yaml
.. image:: https://github.com/airr-community/airr-standards/actions/workflows/r-check.yaml/badge.svg?branch=release-1.5
   :target: https://github.com/airr-community/airr-standards/actions/workflows/r-check.yaml

=============================
AIRR Community Data Standards
=============================

Introduction
============

One of the core initiatives of the `Adaptive Immune Receptor Repertoire
(AIRR) Community`_ [Breden_2017]_ is to develop and maintain standards
regarding the content, format and exchange of data and metadata from
AIRR sequencing (AIRR-seq) experiments, thereby contributing to the
global endeavor to make scientific data `FAIR`_ (findable, accessible,
interoperable, reusable). The current Standards developed from three
initially separate initatives (Minimal Information, Data Representation,
API), which converged over time. The further development of the
Standards is currently carried out by the AIRR Community's `Standards
Working Group`_ (WG), which was the result of the fusion of the "Data
Representation", "Minimal Standards" and parts of the `Common
Repository`_ WGs.


MiAIRR Minimal Information Standard
===================================

The Minimal information about an Adaptive Immune Receptor Repertoire
(**MiAIRR**) data standard defines around 60 metadata fields which
should be provided to facilitate evaluation and re-use a the data set.
These fields are grouped according to the various stage of the typical
workflow (e.g., study, subject, sample, experimental processing, data
processing, data annotation). MiAIRR was originally published in 2017
[Rubelt_2017]_ and has since been intergrated into the `AIRR Data
Schema`_, which has now become the authorative reference for MiAIRR.
For further information see the `MiAIRR section`_ of the `AIRR Standards
documentation`_.


AIRR Standardized Data Representation
=====================================

The standardarized data representation was first published in 2018
[Vander_Heiden_2018]_, the current version of the schema can be found
in this repository as `OpenAPI v2`_ and `OpenAPI v3`_ definitions. The
two versions are functionally identical, but users should be aware that
support for OpenAPI v2 will be discontinued in the intermediate future.


AIRR Data Commons API
=====================

The `AIRR Data Commons`_ (ADC) `API`_ [Christley_2020]_ provides
programmatic access to query and download AIRR-seq data from ADC
repositories.


Implementations
===============

The AIRR Standards are supported by the following services:

*  `AIRR Data Commons`_
*  `CEDAR-AIRR`_


Releases and Issues
===================

Official releases can be found in the `release`_ section of the
repository. There releases are also permanently archived on Zenodo,
where they can be referenced to via the archive's DOI [Zenodo_1185414]_.


Contributions
=============

The AIRR Community is an open initiative and we welcome all
contributions. Please review our `development process`_ before
contributing changes.


References
==========

.. [Breden_2017] Breden F *et al*. Reproducibility and Reuse of
   Adaptive Immune Receptor Repertoire Data. Front Immunol 8:1418
   (2017) `[PMID:29163494]`_ `[DOI:10.3389/fimmu.2017.01418]`_
.. [Christley_2020] Christley S *et al*. The ADC API: A Web API for the
   Programmatic Query of the AIRR Data Commons. Front Big Data (2020)
   `[PMID:33693395]`_ `[DOI:10.3389/fdata.2020.00022]`_
.. [Lees_2020] Lees W *et al*. OGRDB: a reference database of inferred
   immune receptor genes. Nucleic Acids Res 48:D964 (2020) 
   `[PMID:31566225]`_ `[DOI:10.1093/nar/gkz822]`_
.. [Rubelt_2017] Rubelt F *et al*. AIRR Community Recommendations for
   Sharing Immune Repertoire Sequencing Data. Nat Immunol 18:1274
   (2017) `[PMID:29144493]`_ `[DOI:10.1038/ni.3873]`_
.. [Vander_Heiden_2018] Vander Heiden JA *et al*. AIRR Community
   Standardized Representations for Annotated Immune Repertoires. Front
   Immunol 9:2206 (2018) `[PMID:30323809]`_
   `[DOI:10.3389/fimmu.2018.02206]`_
.. [Zenodo_1185414] Release archive of the AIRR Standards repository.
   (2018-2022) `[DOI:10.5281/zenodo.1185414]`_


Copyright & License
===================

Copyright 2015 - 2023 by the AIRR Community and `contributors`_. This
work is licensed under a `Creative Commons Attribution 4.0
International License`_.


.. === External links and references ===

.. _`[PMID:29144493]`: https://www.ncbi.nlm.nih.gov/pubmed/29144493
.. _`[PMID:29163494]`: https://www.ncbi.nlm.nih.gov/pubmed/29163494
.. _`[PMID:30323809]`: https://www.ncbi.nlm.nih.gov/pubmed/30323809
.. _`[PMID:31566225]`: https://www.ncbi.nlm.nih.gov/pubmed/31566225
.. _`[PMID:33693395]`: https://www.ncbi.nlm.nih.gov/pubmed/33693395
.. _`[DOI:10.1038/ni.3873]`: https://doi.org/10.1038/ni.3873
.. _`[DOI:10.3389/fdata.2020.00022]`: https://doi.org/10.3389/fdata.2020.00022
.. _`[DOI:10.3389/fimmu.2017.01418]`: https://doi.org/10.3389/fimmu.2017.01418
.. _`[DOI:10.3389/fimmu.2018.02206]`: https://doi.org/10.3389/fimmu.2018.02206
.. _`[DOI:10.5281/zenodo.1185414]`: https://doi.org/10.5281/zenodo.1185414
.. _`[DOI:10.1093/nar/gkz822]`: https://doi.org/10.1093/nar/gkz822

.. _`Adaptive Immune Receptor Repertoire (AIRR) Community`: https://www.antibodysociety.org/the-airr-community/
.. _`AIRR Data Commons`: https://docs.airr-community.org/en/stable/api/adc.html
.. _`AIRR Data Schema`: https://docs.airr-community.org/en/stable/datarep/overview.html#airr-data-model
.. _`AIRR Standards documentation`: https://docs.airr-community.org/en/stable/
.. _`API`: https://docs.airr-community.org/en/stable/api/adc_api.html
.. _`CEDAR-AIRR`: https://cedar.metadatacenter.org/instances/create/https://repo.metadatacenter.org/templates/ea716306-5263-4f7a-9155-b7958f566933
.. _`Common Repository`: https://www.antibodysociety.org/the-airr-community/airr-working-groups/repository/
.. _`contributors`: https://github.com/airr-community/airr-standards/blob/master/CONTRIBUTORS.rst
.. _`Creative Commons Attribution 4.0 International License`: http://creativecommons.org/licenses/by/4.0/
.. _`development process`: https://github.com/airr-community/airr-standards/tree/master/CONTRIBUTING.rst
.. _`FAIR`: https://www.go-fair.org/fair-principles/
.. _`issue tracker`: https://github.com/airr-community/airr-standards/issues
.. _`MiAIRR section`: https://docs.airr-community.org/en/stable/miairr/introduction_miairr.html
.. _`OpenAPI v2`: https://github.com/airr-community/airr-standards/blob/master/specs/airr-schema.yaml
.. _`OpenAPI v3`: https://github.com/airr-community/airr-standards/blob/master/specs/airr-schema-openapi3.yaml
.. _`release`: https://github.com/airr-community/airr-standards/releases
.. _`Standards Working Group`: https://www.antibodysociety.org/the-airr-community/airr-working-groups/standards/
