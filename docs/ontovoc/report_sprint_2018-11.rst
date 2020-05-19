===============================
OntoVoc Report - Sprint 11/2018
===============================

Objectives
==========

The objectives of this first sprint in November 2018 were to:

1. define criteria for suitable ontologies

2. identify ontologies for five fields/keywords of the MiAIRR data
   standard and

3. assess technical aspects of ontology integration into databases


General Considerations
======================

The Team initially discussed an approach where only vocabularies (i.e.
lists of terms) and not ontologies (i.e. many terms connected by
predicates) would have been defined. These vocabularies would have been
derived from ontologies, but this process would not necessarily have
been reversible. The notion at this time point was, that such an
approach would allow to solve a number of problems like combining
multiple sources and removing duplicated leaves. However, after some
discussions this approach was effectively abandoned for a number of
reasons:

-  It would discard the UID for an entity. As the UID (in contrast to
   the name string) is guaranteed to be stable and unique, it
   facilitates updates, linking and information representation, all of
   which would otherwise be lost.
-  In general, it will be more sustainable to work with the maintainers
   of an existing ontology to include entities/terms, than just dumping
   their terms into a list and adding new ones.
-  Well-designed ontologies will not contain duplicated entities,
   although they might appear to do so in a simple browsers (i.e. this
   is an artifact of representation). Ontologies that actually do
   contain duplicates are excluded by criterium `(2)`_.


Criteria for Ontologies
=======================

Criteria
--------

Ontologies used within AIRR standards

.. _ONTO_CRIT_1:

1. MUST [1]_ cover the majority of the required terms, but complete
   coverage is OPTIONAL

.. _ONTO_CRIT_2:

2. MUST have a structure that is scientifically correct and logically
   coherent

.. _ONTO_CRIT_3:

3. MUST NOT feature complexity that makes it hard to use for queries
   and data representation

.. _ONTO_CRIT_4:

4. SHOULD already be widely adopted

.. _ONTO_CRIT_5:

5. MUST be actively maintained

.. _ONTO_CRIT_6:

6. MUST be available under a free license

Comments on criteria:

-  ad `(1)`_: For most fields it will be difficult to find complete and
   accurate ontologies. Therefore picking the best available ontology
   and working with its maintainers to include missing terms is expected
   to be the most sustainable approach.
-  ad `(5)`_: This requirement follows from `(1)`_, as there needs to be
   a way for term requests.
-  ad `(6)`_: A number of ontologies need to be licensed from their
   respective copyright holders. This results in potential barriers for
   implementation and distribution of such ontologies. Therefore only
   ontologies available under a free license are considered suitable for
   AIRR-compliant databases. The list of suitable licenses is not final,
   but includes: CC0_ and `CC BY`_.

.. _`(1)`: ONTO_CRIT_1_
.. _`(2)`: ONTO_CRIT_2_
.. _`(5)`: ONTO_CRIT_5_
.. _`(6)`: ONTO_CRIT_6_


Selected Ontologies
===================

(designations are MiAIRR field names and ``DataRep keywords``)

Completed
---------

-  Species (``organism``)

   -  NCBITAXON_
   -  license: UMLS [2]_
   -  latest release: 2018-07-06
   -  maintainer: NCBI (info@ncbi.nlm.nih.gov)

-  Diagnosis (``disease_diagnosis``)

   -  DOID_
   -  root node

      -  name: ``disease``
      -  ID: ``DOID:4``
      -  path: ``/disease``

   -  License: `CC BY`_
   -  latest release: 2018-03-02
   -  maintainer: Lynn Schriml, U Maryland, MD, US
      (lynn.schriml@gmail.com)
   -  notes: Features ICD cross-reference

-  Cell subset (``cell_subset``)

   -  CellOntology_
   -  license: `CC BY`_
   -  latest release: 2018-07-11
   -  maintainer: Alexander Diehl, Buffalo, NY, US
      (addiehl@buffalo.edu)

-  Tissue (``tissue``)

   -  Uberon_
   -  root node

      -  name: ``multicellular anatomical structure``
      -  ID: ``UBERON:0010000``
      -  path: ``/BFO_0000002/BFO_0000004/anatomical entity/material
         anatomical entity/anatomical structure/multicellular anatomical
         structure``

   -  License: `CC BY`_
   -  latest release: 2018-10-15
   -  Maintainer: Chris Mungall, LBL, CA, US
      (cjmungall@lbl.gov)

Under evaluation
----------------

-  Strain name (``strain_name``)

   -  Suggested ontologies:

      -  JAX
      -  IEDB

   -  Issues:
   
      -  Nomenclature
      -  one ontology is not enough	


Technical aspects
=================

-  Repositories:

   -  UID assigned by ontologies are guaranteed to be unique and 
      permanent [3]_.
   -  A repository MAY use internal identifiers that are distinct from
      UIDs. However, to be AIRR-compliant it MUST be able to map UIDs to
      its identifiers.
   -  Points of “AIRR compliance” would typically be:

      -  When data is extracted from the repository through a Query API
         (CRWG)
      -  When data is extracted from the repository into a file format
         (DataRep)

-  Integration of ontologies into repositories:

   -  There are two main ontology providers offering a REST API and all
      the ontologies listed above:

      -  NCBO Bioportal [https://bioportal.bioontology.org]
      -  OLS ontology [https://www.ebi.ac.uk/ols/ontologies]

   -  NCBO can apparently be slow and sometimes not that stable, while
      OLS seems to be more stable and potentially has a better long-term
      support.
   -  Remote ontology services tend to be slow and create external
      dependencies. On the other hand, while local hosting of an
      ontology is possible (and partially supported by NCBO and OLS), it
      requires non-negligible resources. The Team's current assumption
      is that queries to remote ontology services can be substantially
      accelerated if only the relevant section of a respective ontology
      is queried. Therefore a local service would not be necessary.
   -  Repositories should store both the IDs and the values in their
      database. This way, they do not have to query the ontology in a
      scenario where human-readable output is required. In the case of
      changes, most ontologies try to follow the practice of not
      changing a term value but instead create a new term with the new
      value and a new ID, and deprecating the old term. Therefore term
      deprecation needs to be handled by the repository.
   -  Like for the databases, also the API should be able to handle both
      IDs and values as query input and return both during a query.
   -  The user interface (UI) should offer an ontology-backed
      autocomplete. NCBO provides some JavaScript code to use. The UI
      must not offer deprecated terms. To allow entry of terms not
      present in the ontology, data can be prefixed with some text that
      will allow the data validation to proceed (e.g., if an entry
      starts with "other -" the UI will not autocomplete/validate).
      Later, i.e. when the term has been created, the data will be
      updated.

-  Note that the complete IEDB can be `downloaded as SQL dump`__, it is
   licensed under `CC BY`_. At a first glance, the main overlap seems to
   be with ``organism``, ``strain_name`` and to a smaller extent
   ``disease_diagnosis``. However, sample information like ``cell_subset``
   and ``tissue`` seems to be largely absent from IEDB, so it could
   currently not be the one-stop solution for AIRR.

__ https://www.iedb.org/database_export_v3.php


Footnotes
=========

.. [1] See the "Glossary" section on how to interpret term written in
   all-caps.
.. [2] Will require further review the `UMLS Metathesaurus License
   <https://uts.nlm.nih.gov/license.html>`_ is not a free license,
   however it needs to be clarified how much of it relates to the work
   (i.e. the taxonomy itself) and how much to the service.
.. [3] This has more recently (early 2020) been called in question and
   will be revisited during the next sprint. Note that the uncertainty
   revolves around the question what exactly constitues a UID, rather
   than the question whether a UID is permanent and unique.
   
Appendix
========
   
Glossary
--------

-  MUST / REQUIRED: Indicates that an element or action is necessary to
   conform to the standard.

-  SHOULD / RECOMMENDED: Indicates that an element or action is
   considered to be best practice by AIRR, but not necessary to conform
   to the standard.

-  MAY / OPTIONAL: Indicates that it is at the discretion of the user
   to use an element or perform an action.

-  MUST NOT / FORBIDDEN: Indicates that an element or action will be in
   conflict with the standard.

.. Links

.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _`CC BY`: https://creativecommons.org/licenses/by/4.0/
.. _NCBITAXON: https://bioportal.bioontology.org/ontologies/NCBITAXON
.. _DOID: https://bioportal.bioontology.org/ontologies/DOID
.. _CellOntology: https://bioportal.bioontology.org/ontologies/CL
.. _Uberon: https://bioportal.bioontology.org/ontologies/UBERON

