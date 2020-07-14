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

Ontology Data Representation
============================

The nodes in an ontology are typically either concepts (e.g., capital) or instances thereof (e.g., Paris).
These nodes have local IDs (often numbers), which are unique within an ontology. They also typically have labels,
which is the human-readable name of the node. Ontology entities in the AIRR Data Standard reflect this model,
with each AIRR field that is represented as an ontology recorded with an ontology `id` and an ontology `label`.

Within the AIRR Standards, Compact URIs (`CURIEs`_) are used to represent an ontology `id`.
CURIEs are a standardized way to abbreviate International
Resource Identifiers (IRI, [RFC3987]_), which includes URIs as a subset. They were originally conceived to
simplify the handling of attributes, e.g. in XML or SPARQL, by making
them more compact and readable. For example CURIEs are used by IEDB databases
to reduce redundancies (mainly in the leading part of IRIs).

For example, a typical CURIE would look like ``NCBITAXON:9258``. In this case,
``NCBITAXON`` is the *prefix*, a custom string that will be replaced by
a repository-defined IRI component (e.g.,
``http://purl.obolibrary.org/obo/NCBITaxon_``). Note that there is no
connection between ``NCBITAXON`` in the CURIE and ``NCBITaxon`` in the
IRI, the former one is just a placeholder.

The AIRR schema will provide a list of AIRR approved CURIE *prefixes*
along with a list of at least one IRI *prefix* (i.e., replacement
string) for each them. This list serves two purposes:

1. It provides a controlled namespace for CURIE *prefixes* used in the
   AIRR schema. For now, custom additions to or replacements of these
   *prefixes* in the schema is prohibited. This does not affect the
   ability of repositories to use such custom prefixes internally.
2. It simplifies resolution of CURIEs by non-repositories. The
   lists of IRI *prefixes* for each CURIE *prefix* should not be
   considered to be exhaustive. However, when using custom IRI
   *prefixes*, it must be ensured that they refer to the same
   ontology as the provider *prefixes*.

It should be explicitly noted that the IRI *prefix* list should not be
interpreted as any kind of recommendation for certain *providers*. It is
left up to users to decide how to resolve the resulting IRIs, e.g., via
DNS/HTTP (if possible) or by using a *provider* of their choice.

Approved Ontologies
===================

.. _ONTO_CL:

*  Cell ontology (CL_)

   *  used in:

      *  Cell subset (``cell_subset``,
         :ref:`Tissue and Cell Processing <CellProcessingFields>`)

   *  CURIE summary
   
      * CURIE Prefix: CL
      * CURIE IRI Prefix: http://purl.obolibrary.org/obo/CL\_

   *  example AIRR use
   
      * "cell_subset.id" : "CL:0000542"
      * "cell_subset.label" : "lymphocyte"

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

   *  CURIE summary
   
      * CURIE Prefix: DOID
      * CURIE IRI Prefix: http://purl.obolibrary.org/obo/DOID\_

   *  example AIRR use
   
      * "disease_diagnosis.id" : "DOID:9538"
      * "disease_diagnosis.label" : "multiple myeloma"
    
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

   *  CURIE summary

      * CURIE Prefix: NCBITAXON
      * CURIE IRI Prefixes:

         * http://purl.obolibrary.org/obo/NCBITaxon\_
         * http://purl.bioontology.org/ontology/NCBITAXON/

   *  example AIRR use

      * "species.id" : "NCBITAXON:9606"
      * "species.label" : "Homo sapiens"

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

   *  CURIE summary

      * CURIE Prefix: NCIT
      * CURIE IRI Prefix: http://purl.obolibrary.org/obo/NCIT\_, http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#

   *  example AIRR use

      * "study_type.id" : "NCIT:C15197"
      * "study_type.label" : "Case-Control Study"

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

   *  CURIE summary
   
      * CURIE Prefix: UO
      * CURIE IRI Prefix: http://purl.obolibrary.org/obo/UO\_
      
   *  example AIRR use
   
      * "age_unit.id" : "UO:0000036"
      * "age_unit.label" : "year"

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

   *  example AIRR use
   
      * "tissue.id" : "UBERON:0002371"
      * "tissue.label" : "bone marrow"

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


Sprint Reports
==============

.. toctree::
   :maxdepth: 2

   Report Sprint 11/2018 <report_sprint_2018-11>
   Report Sprint 04/2020 <report_sprint_2020-04>

.. Citations

.. [RFC3987] Internationalized Resource Identifiers (IRIs). `DOI:10.17487/RFC3987`_

.. Links

.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _`CC BY`: https://creativecommons.org/licenses/by/4.0/
.. _`CURIEs`: https://www.w3.org/TR/curie
.. _CL: http://obofoundry.org/ontology/cl.html
.. _DOID: https://disease-ontology.org
.. _NCBITAXON: https://www.ebi.ac.uk/ols/ontologies/NCBITAXON
.. _NCIT: https://www.ebi.ac.uk/ols/ontologies/ncit
.. _Uberon: https://www.ebi.ac.uk/ols/ontologies/UBERON
.. _UO: https://www.ebi.ac.uk/ols/ontologies/UO
