.. _OntoVoc:

=====================================
AIRR Ontologies and Vocabularies Team
=====================================

Summary
=======

The "Ontologies and Vocabularies Team" was formed as a joint interest
group of the Common Repository (ComRepo) and the Minimal Standards
(MiniStd) working groups of the AIRR Community. The long-term aim of
the Team is to define standard vocabularies and ontologies to be used
by AIRR-compliant databases.

Approved Ontologies
===================

-  Species (``organism``, :ref:`Subject <SubjectFields>`) (``cell_species``, :ref:`Tissue and Cell Processing <CellProcessingFields>`)

   -  NCBITAXON_
   -  license: UMLS
   -  latest release: 2018-07-06
   -  maintainer: NCBI (info@ncbi.nlm.nih.gov)

-  Diagnosis (``disease_diagnosis``, :ref:`Diagnosis <DiagnosisFields>`)

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

-  Cell subset (``cell_subset``, :ref:`Tissue and Cell Processing <CellProcessingFields>`)

   -  CellOntology_
   -  license: `CC BY`_
   -  latest release: 2018-07-11
   -  maintainer: Alexander Diehl, Buffalo, NY, US
      (addiehl@buffalo.edu)

-  Tissue (``tissue``, :ref:`Sample <SampleFields>`)

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

Topics
======

.. toctree::
   :maxdepth: 2

   Report Sprint 11/2018 <report_sprint_2018-11>

.. Links

.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _`CC BY`: https://creativecommons.org/licenses/by/4.0/
.. _NCBITAXON: https://bioportal.bioontology.org/ontologies/NCBITAXON
.. _DOID: https://bioportal.bioontology.org/ontologies/DOID
.. _CellOntology: https://bioportal.bioontology.org/ontologies/CL
.. _Uberon: https://bioportal.bioontology.org/ontologies/UBERON
