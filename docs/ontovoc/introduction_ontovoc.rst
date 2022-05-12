.. _OntoVoc:

=======================================
AIRR Ontologies and Vocabularies Sub-WG
=======================================

Summary
=======

The "Ontologies and Vocabularies Team" was initial formed as a joint
interest group of the Common Repository (ComRepo) and the Minimal
Standards (MiniStd) working groups (WG) of the AIRR Community. When the
two WG merged into the current Standards WG in Decemmber 2020, OntoVoc
became a Sub-WG of it. The long-term aim of the Sub-WG is to define
standard vocabularies and ontologies to be used by AIRR-compliant
repositories.


Ontology Data Representation
============================

The nodes in an ontology are typically either concepts (e.g., capital)
or instances thereof (e.g., Paris). These nodes have *local IDs* (often
numbers), which are unique within an ontology. They also typically have
*labels*, which is the human-readable name of the node. Ontology
entities in the AIRR Data Standard reflect this model, with each AIRR
field that is represented as an ontology recorded with a global
*ontology ID* (``id``) and the corresponding *label* (``label``).

Within the AIRR Standards, Compact URIs (`CURIEs`_) are used to
represent *ontology IDs* or *persistent IDs*. CURIEs are a standardized
way to abbreviate International Resource Identifiers (IRI, [RFC3987]_),
which include URIs and URLs as subsets. They were originally conceived
to simplify the handling of attributes, e.g., in XML or SPARQL, by
making them more compact and readable. CURIEs are also used by IEDB
databases to reduce redundancies (mainly in the leading part of IRIs).

For example, a typical CURIE would look like ``NCBITAXON:9258``. In this
case, ``NCBITAXON`` is the *prefix*, a custom string that will be
replaced by a repository-defined IRI component (e.g.,
``http://purl.obolibrary.org/obo/NCBITaxon_``). Note that there is no
connection between ``NCBITAXON`` in the CURIE and ``NCBITaxon`` in the
IRI, the former one is just a placeholder. Although common, it is not
always the case that a resolved CURIE (the IRI *prefix* plus the
*local ID*) can be used as a URL directly to look up the CURIE using a
web browser.

The AIRR Schema provides a ``CURIEMap``, a list of AIRR approved CURIE
*prefixes* along with a ``map`` of at least one ``iri_prefix`` (i.e.,
a replacement string to construct the complete IRI) for each *prefix*.
As the ``iri_prefix`` might differ between *provider*-specific
implementations of an ontology (e.g., NCBI Taxonomy), the ``CURIEMap``
supports multiple ``iri_prefix`` entries for a given *prefix*. Finally,
the ``CURIEMap`` should also provide a default ``map`` and ``provider``
for each *prefix*. Complementary to this, the ``InformationProvider``
list describes the mechanism to computationally look up a resolved IRI
(e.g., the ``iri_prefix`` and the *local ID*) by specifying how to make
a request to the *provider* as well as describing the format in which
the request response will be provided.

The ``CURIEMap`` serves several purposes:

1. It provides a controlled namespace for CURIE *prefixes* used in the
   AIRR Schema. For now, custom additions to or replacements of these
   *prefixes* in the schema are prohibited. This does not affect the
   ability of repositories to use such custom prefixes internally.
2. It simplifies resolution of CURIEs. The ``iri_prefix`` lists for each
   *prefix* should not be considered to be exhaustive. However, when
   using a custom ``iri_prefix``, it must be ensured that the expanded
   IRI still refers to the same concept/instance as when using the
   default ``iri_prefix``.
3. It simplifies computation using CURIES. It is possible to use the
   ``provider`` for a *prefix* as a mechanism to look up a CURIE from a
   *provider* with a defined response (See below)

It should be explicitly noted that the ``CURIEMap`` should not be
interpreted as any kind of recommendation for certain *providers*. It is
left up to users to decide how to resolve the resulting IRIs, e.g., via
DNS/HTTP (if possible) or by using a *provider* of their choice.


.. _ONTO_CRIT_CURRENT:

General Policies
================

Criteria
--------

Ontologies used within AIRR standards

.. _ONTO_CRIT_CURRENT_1:

1. MUST [1]_ cover the majority of the required terms, but complete
   coverage is OPTIONAL

.. _ONTO_CRIT_CURRENT_2:

2. MUST have a structure that is scientifically correct and logically
   coherent

.. _ONTO_CRIT_CURRENT_3:

3. MUST NOT feature complexity that makes it hard to use for queries
   and data representation

.. _ONTO_CRIT_CURRENT_4:

4. SHOULD already be widely adopted

.. _ONTO_CRIT_CURRENT_5:

5. MUST be actively maintained

.. _ONTO_CRIT_CURRENT_6:

6. MUST be available under a free license

.. _ONTO_CRIT_CURRENT_7:

7. SHOULD comply to the `OBO Foundry Principles`_. This does not imply
   a preference.


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
-  ad `(7)`_: This is an endorsement of the OBO Foundry *Principles*,
   not of the OBO Foundry *Ontologies* in general. Hence, also non-OBO
   have an equal standing if they comply to the Principles.

.. _`(1)`: ONTO_CRIT_CURRENT_1_
.. _`(2)`: ONTO_CRIT_CURRENT_2_
.. _`(5)`: ONTO_CRIT_CURRENT_5_
.. _`(6)`: ONTO_CRIT_CURRENT_6_
.. _`(7)`: ONTO_CRIT_CURRENT_7_



Approved Ontologies
===================

.. _ONTO_CL:

*  Cell ontology (CL_)

   *  used in:

      *  Cell subset (``cell_subset``,
         :ref:`Tissue and Cell Processing <CellProcessingFields>`)

   *  CURIE summary
   
      * CURIE Prefix: ``CL``
      * CURIE IRI Prefix: ``http://purl.obolibrary.org/obo/CL_``

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
   
      * CURIE Prefix: ``DOID``
      * CURIE IRI Prefix: ``http://purl.obolibrary.org/obo/DOID_``

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

      * CURIE Prefix: ``NCBITAXON``
      * CURIE IRI Prefixes:
        ``http://purl.obolibrary.org/obo/NCBITaxon_``,
        ``http://purl.bioontology.org/ontology/NCBITAXON/``

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

      * CURIE Prefix: ``NCIT``
      * CURIE IRI Prefixes:
        ``http://purl.obolibrary.org/obo/NCIT_``,
        ``http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#``

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
   
      * CURIE Prefix: ``UO``
      * CURIE IRI Prefix: ``http://purl.obolibrary.org/obo/UO_``
      
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

   *  CURIE summary

      * CURIE Prefix: ``UBERON``
      * CURIE IRI Prefix: ``http://purl.obolibrary.org/obo/UBERON_``

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


.. _ONTO_COMPUTING:

Computing with Ontologies
=========================

One of the key goals of using ontologies is to enable analysis tools
to perform computation using the information in those ontologies. The
AIRR Schema's ``CURIEMap`` lists one or more *providers* for each CURIE
*prefix* that can be used programmatically by analysis tools. Although
the AIRR Schema lists multiple providers for each ontology, this section
focuses on the use of the `EBI OLS`_ *provider's* `OLS Web API`_
interface for querying ontologies.

If we consider the ``DOID`` *prefix* from the ``CURIEMap``, the section
below defines the use of the Human Disease Ontology (DOID_) within the
AIRR Standard:

.. code-block::

  DOID:
    type: ontology
    default:
      map: OBO
      provider: OLS
    map:
      OBO:
        iri_prefix: "http://purl.obolibrary.org/obo/DOID_"

We see that the default ``map`` for DOID is ``OBO`` map, and the OBO
map's ``iri_prefix`` is ``http://purl.obolibrary.org/obo/DOID_``. Thus
the mapping of the CURIE ``DOID:9538`` (the CURIE for disease "multiple
myeloma") will yield the resolved string
``http://purl.obolibrary.org/obo/DOID_9538``. By the strictest of
defintions, this is a valid IRI and should only be considered an
identifier, but in this case this IRI is also a URL and can be used to
look up the CURIE.

If we consider the default DOID ``provider`` in the ``CURIEMap``, we see
that it is ``OLS``. Then, in the ``InformationProvider`` object of the
AIRR Schema, under ``provider`` we see:

.. code-block::

  InformationProvider:
    provider:
      OLS:
        request:
          url: "https://www.ebi.ac.uk/ols/api/ontologies/{ontology_id}/terms?iri={iri}"
          response: application/json

And later we see that the ``parameters`` for ``OLS`` are:

.. code-block::

  parameter:
    CL:
      Ontobee:
        ontology_id: CL
      OLS:
        ontology_id: cl
    DOID:
      Ontobee:
        ontology_id: DOID
      OLS:
        ontology_id: doid

The above tells us that we can use the OLS ``provider`` to look up
ontology terms. The ``{iri}`` component of the ``url`` string tells us
that we need to use the resolved IRI and the ``{ontology_id}`` component
tells us that we need to replace the ``ontology_id`` parameter in the
URL with the DOID OLS parameter in the specification, which is the
string ``doid``. Thus the fully resolved URL to query for the CURIE
``DOID:9538`` would be:

.. code-block::

  https://www.ebi.ac.uk/ols/api/ontologies/doid/terms?iri=http://purl.obolibrary.org/obo/DOID_9538

Again, referring to the OLS ``provider`` we see that we can expect an
``application/json`` response to the above query, and indeed  the
response we receive from the above starts with a JSON object as follows.

.. code-block::

 {
  "_embedded" : {
    "terms" : [ {
      "iri" : "http://purl.obolibrary.org/obo/DOID_9538",
      "label" : "multiple myeloma",
      "description" : [ "A myeloid neoplasm that is located_in the plasma cells in bone marrow." ],
      "annotation" : {
        "comment" : [ "OMIM mapping confirmed by DO. [SN]." ],
        "database_cross_reference" : [ "ICD10CM:C90.0", "MESH:D009101", "ICD9CM:203.0", "GARD:7108", "NCI:C3242", "OMIM:254500", "ORDO:29073", "EFO:0001378", "SNOMEDCT_US_2020_09_01:94705007", "UMLS_CUI:C0026764" ],
        "has_obo_namespace" : [ "disease_ontology" ],
        "id" : [ "DOID:9538" ]
      },
      "synonyms" : [ "plasma cell myeloma" ],
      "ontology_name" : "doid",
      "ontology_prefix" : "DOID",
      "ontology_iri" : "http://purl.obolibrary.org/obo/doid.owl",
      "is_obsolete" : false,
      "term_replaced_by" : null,
      "is_defining_ontology" : true,
      "has_children" : true,
      "is_root" : false,
      "short_form" : "DOID_9538",
      "obo_id" : "DOID:9538",
      [Content edited because of length]

In this repsonse, you can see that the Ontology object that we requested
has a ``label`` field that contains the value ``multiple myeloma`` and
that the ``id`` field has a value of ``DOID:9538``.

It is beyond the scope of this document to describe in detail the JSON
structure of each of the providers, but this information can be
discovered through the ``provider`` web sites. It should be noted that
all Ontology objects in the AIRR specification have the OLS as a
``provider`` and therefore the method above can be used for any of the
ontologies in the AIRR specification. Please see the `OLS Web API`_
documentation for details of the JSON response for the OLS ``provider``.


Sprint Reports
==============

.. toctree::
   :maxdepth: 2

   Report Sprint 11/2018 <report_sprint_2018-11>
   Report Sprint 04/2020 <report_sprint_2020-04>
   Report Sprint 04/2021 <report_sprint_2021-04>

.. == Citations ==

.. [RFC3987] Internationalized Resource Identifiers (IRIs). `DOI:10.17487/RFC3987`_

.. == Link references ==
.. _`OBO Foundry Principles`: https://en.wikipedia.org/wiki/OBO_Foundry#Principles
.. _CC0: https://creativecommons.org/publicdomain/zero/1.0/
.. _`CC BY`: https://creativecommons.org/licenses/by/4.0/
.. _`CURIEs`: https://www.w3.org/TR/curie
.. _CL: http://obofoundry.org/ontology/cl.html
.. _DOID: https://disease-ontology.org
.. _NCBITAXON: https://www.ebi.ac.uk/ols/ontologies/NCBITAXON
.. _NCIT: https://www.ebi.ac.uk/ols/ontologies/ncit
.. _Uberon: https://www.ebi.ac.uk/ols/ontologies/UBERON
.. _UO: https://www.ebi.ac.uk/ols/ontologies/UO
.. _`EBI OLS`: https://www.ebi.ac.uk/ols
.. _`OLS Web API`: https://www.ebi.ac.uk/ols/docs/api
