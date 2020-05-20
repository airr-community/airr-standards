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


Sprint Reports
==============

.. toctree::
   :maxdepth: 2

   Report Sprint 11/2018 <report_sprint_2018-11>
   Report Sprint 04/2020 <report_sprint_2020-04>


Approved Ontologies
===================

.. _ONTO_CL:

*  Cell ontology (CL_)

   *  used in:

      *  Cell subset (``cell_subset``,
         :ref:`Tissue and Cell Processing <CellProcessingFields>`)

   *  default root node

      *  label: ``lymphocyte``
      *  local id: ``CL_0000542``
      *  path: ``

   *  license: `CC BY`_
   *  latest release (as of 2020-05-20): 2020-03-02
   *  repo: https://github.com/obophenotype/cell-ontology
   *  maintainer: Alexander Diehl, Buffalo, NY, US
      (addiehl@buffalo.edu)

.. _ONTO_DOID:

*  Human disease ontology (DOID_)

   *  used in:

      *  Diagnosis (``disease_diagnosis``,
         :ref:`Diagnosis <DiagnosisFields>`)

   *  default root node

      *  label: ``disease``
      *  local ID: ``DOID:4``
      *  path: ``disease``

   *  license: CC0_
   *  latest release (as of 2020-05-20): 2020-04-20
   *  repo: https://github.com/DiseaseOntology/HumanDiseaseOntology
   *  maintainer: Lynn Schriml, U Maryland, MD, US
      (lynn.schriml@gmail.com)
   *  notes: Features ICD cross-reference

.. _ONTO_NCBITAXON:

*  NCBI organismal taxonomy (NCBITAXON_)

   *  used in:

      *  Species (``species``, :ref:`Subject <SubjectFields>`)
      *  Cell species (``cell_species``,
         :ref:`Tissue and Cell Processing <CellProcessingFields>`)

   *  default root node

      *  label: ``Gnathostomata``
      *  local ID: ``7776``
      *  path:
         ``cellular organisms/Eukaryota/Opisthokonta/Metazoa/Eumetazoa/Bilateria/Deuterostomia/Chordata/Craniata/Vertebrata/Gnathostomata``

   *  license: UMLS
   *  latest release (as of 2020-05-20): 2020-04-18
   *  repo: https://github.com/obophenotype/ncbitaxon
   *  maintainer: NCBI (info@ncbi.nlm.nih.gov)

.. _ONTO_NCIT:

*  NCI thesaurus (NCIT_)

   *  used in:

      *  Study type (``study_type``, :ref:`Study <StudyFields>`)

   *  default root node

      *  label: ``Study``
      *  local ID: ``C63536``
      *  path: ``Activity/Clinical or Research Activity/
         Research Activity/Study``

   *  license: Public domain, credit of NCI is requested
   *  repo: https://github.com/NCI-Thesaurus/thesaurus-obo-edition
   *  latest release (as of 2020-05-20): 2020-05-04
   *  maintainer: NCI (ncicbiitappssupport@mail.nih.gov)

.. _ONTO_UO:

*  Units of measurement ontology (UO_)

   *  used in:

      *  Age unit (``age_unit``, :ref:`Subject <SubjectFields>`)

   *  default root node

      *  label: ``time unit``
      *  local ID: ``UO_0000003``
      *  path: ``unit/time unit``

   *  license: `CC BY`_ (per Github repo)
   *  repo: https://github.com/bio-ontology-research-group/unit-ontology
   *  latest release (as of 2020-05-20): 2020-05-18
   *  maintainer: unknown

.. _ONTO_UBERON:

*  Uber-anatomy ontology (Uberon_)

   *  used in:

      *  Tissue (``tissue``, :ref:`Sample <SampleFields>`)

   *  default root node

      *  label: ``multicellular anatomical structure``
      *  local ID: ``UBERON:0010000``
      *  path:
         ``/BFO_0000002/BFO_0000004/anatomical entity/material anatomical entity/anatomical structure/multicellular anatomical structure``

   *  license: `CC BY`_
   *  repo: https://github.com/obophenotype/uberon
   *  latest release (as of 2020-05-20): 2019-11-22
   *  maintainer: Chris Mungall, LBL, CA, US
      (cjmungall@lbl.gov)

.. Links

.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _`CC BY`: https://creativecommons.org/licenses/by/4.0/
.. _CL: http://obofoundry.org/ontology/cl.html
.. _DOID: https://disease-ontology.org
.. _NCBITAXON: https://www.ebi.ac.uk/ols/ontologies/NCBITAXON
.. _NCIT: https://www.ebi.ac.uk/ols/ontologies/ncit
.. _Uberon: https://www.ebi.ac.uk/ols/ontologies/UBERON
.. _UO: https://www.ebi.ac.uk/ols/ontologies/UO
