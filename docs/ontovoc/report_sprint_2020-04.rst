===============================
OntoVoc Report - Sprint 04/2020
===============================

Objectives
==========

The objectives of this second sprint in April 2020 were to:

1. revisit general policies around ontologies used in the AIRR schema

2. identify two new ontologies for several fields of the AIRR schema

3. solve technical questions regarding IDs and providers


General Policies
================

The OntoVoc team revisited the criteria for ontologies used in the AIRR
schema that it :ref:`defined in the 11/2018 sprint <ONTO_CRIT_11-2018>`.
While they are still considered to be valid, the team felt that a more
detailed guidance could be useful in the process of selecting ontologies
for new fields. It therefore evaluated the `OBO Foundry Principles`_,
which partially re-iterate some of the existing criteria (e.g.,
:ref:`Openness <ONTO_CRIT_6>` and :ref:`Maintenance<ONTO_CRIT_5>`),
but also provide additional recommendations, e.g., the presence of
textual definitions, clear scope and a common format, which were
considered to be valuable additions to the existing guidelines. The team
therefore decided to endorse the OBO Foundry Principles, as RECOMMENDED
(but NOT REQUIRED) criteria. It should be noted, that this does not make
any statement regarding the use of OBO vs. non-OBO ontologies.


Decisions on Pending Items of Sprint 11/2018
============================================

A number of decisions on draft and legacy ontologies as well as root
nodes was not officially passed during the last sprint. The team thus
revisited and confirmed the following decisions:

*  Use of NCIT for ``study_type``, top node ``Study`` (``NCIT:C63536``).
*  Use of UO for ``age_unit``, top node ``time unit`` (``UO:0000003``).
*  Use of ```Gnathostomata`` (``NCBITAXON:7776``) as top node for
   ``NCBITAXON`` when used for fields encoding a host species.
*  Use of ``lymphocyte`` (``CL:0000542``) as top node for ``CL`` when
   used for ``cell_subset``.


New Ontologies
==============

Mouse strain
------------

Background
~~~~~~~~~~

Mouse strain names follow a very `elaborate nomenclature`__ that is
capable of describing the genetic background, breeding history and
introduced mutation in a detailed manner. However, this nomenclature
is rarely used correctly (if at all), which creates uncertainty about
the identity of strains used in experimental studies. Therefore an
ontology or vocabulary compliant to this nomenclature would be of
tremendous help for consistent annotation.

.. __: http://www.informatics.jax.org/mgihome/nomen/strains.shtml

An ontology for the ``strain_name`` field was already on the list for
the last sprint, however it was not possible to identify a single
ontology that would contain comprehensive information about strains
from multiple species. This situation created a problem that could not
be resolved then. In the mean time, the concept of "extensions" has
been introduced to the AIRR schema, which create an additional layer of
fields (and associated ontologies) on top of a core schema. As these
extensions can be made conditional on the value of fields within the
core schema, it has now become possible to have multiple extensions
defining the ``strain_name`` field, but for differnt species and
therefore with distinct species-specific ontologies.
   
Having addressed this issue, the other key problem that remains is the
absence of an actual ontology for mouse strains, while a
`rat strain ontology`_ exists. Therefore in a first step it is necessary
to identify resources that you at least serve as a provider for
vocabularies. The two potential candidates that were identified are:

*  MGI: The Mouse Genome Informatics database hosted at JAX aims to be
   comprehensive in regard to all mouse strains that have been published
   in the literature.
*  IEDB: The Immune Epitope Database already ran in to problem of the
   missing mouse ontology and therefore decided to build up their own
   reference focused on immunologically relevant strains, as part of
   their Ontie database.

Once it is clear which of the resources could be used, it will be
necessary to approach the current maintainers regarding their
willingness to convert the data into an actual ontology (the RS could
serve as a template for this). As this will take longer than just a
couple of weeks, the second step is out-of-scope for this sprint.


Evaluation
~~~~~~~~~~

*  MGI: The database can be downloaded as a dump, however the licensing
   conditions are unclear. It contains a total of 60k entries of which
   3.2k inbred and 13.8k are congenic strains. The majority of the
   remaining entries are coisogenic strains, most of them from large-
   scale gene KO projects.
*  IEDB: Database dumps can also be downloaded and are freely available
   under CC-BY 4.0. It covers over a thousand mouse strains and contains
   addtional information on the genetic background of a strain.


Next steps
~~~~~~~~~~

*  Get in touch with JAX (pending)


Geolocation
-----------
 
There are several (planed) extension to the AIRR metadata standard that
will provide geospatial metadata. Country-level information is typically
assumed to be privacy-preserving and easy to operationalize. Therefore,
while clearly only capturing some aspects of genetic ancestry, it might
serve as a proxy for concepts of "race" and "ethnicity" that are rather
ill-defined.

Potential candidate vocabularies/ontologies:

*  `ISO3166-1 alpha-2`_: Two-letter code, some ambiguity but well known
   from ccTLDs.
*  `ISO3166-1 alpha-3`_: Three-letter code, less ambiguity than alpha-2.
*  UN Stats Division code (currently `M49`_): Numerical code, not
   human-readable, maps to ISO3166-1 alpha-3.
*  Gazetter (`GAZ`_)

   *  Contains 2nd (state) and 3rd (county) level information.
   *  Not linked to any actual coordinates
   *  ISO3166-1 annotation is incomplete and lacks e.g. for Germany and
      Switzerland.
   *  Does not support German Umlauts. Äbsölütely inacceptable, as these
      are not just diacritial marks (i.e. "Münster" and "Munster" are
      two different cities).

*  `HANCESTRO`_:

   *  Seems to be complete, but does not provide ISO3166 codes.
   *  Ontology could also be used for other fields relating to genetic
      ancestery.
   *  Links to DBpedia, currently unclear whether it is also populated
      from there
   *  `country` node has pan-240 leaves (surplus seems due to oversea
      territories), cross-referencing to GAZ (s/a)

*  Various pathogen-related repositories:

   *  VectorBase (`VBGEO`_): see link and choose "GADM/VBGEO PlaceNames”
   *  Viral Pathogen Resource (`ViPR`_):

      *  Uses v1.3 of the `GSCID/BRC Project and Sample Application
         Standard`_.
      *  `GSCID/BRC Core Sample`_ defines four fields for "Collection
         Location":

         *  "Latitude" (``CS11``) and "Longitude" (``CS12``) in `ISO
            6709`_ format
         *  "Location" (``CS13``), using GAZ as controlled vocabulary
         *  "Country" (``CS14``) as by ISO3166-1 (alpha-2).

   *  Influenza Research Database (`IRD`_): Flu-focused version of ViPR,
      also uses GSCID/BRC Project and Sample Application Standard v1.3.
   *  Pathosystems Resource Integration Center (`Patric`_): Focused on
      bacterial infectious diseases. Uses an "Isolation Country" field
      in their "Genome" table, format seems to be full text.

Rejected candidates:

*  HL7: own ontology deprecated, now recommends ISO 3166-1 alpha-3 set.
*  NCIT: Incomplete, only contains pan-90 entities
*  SNOMED: Licensing issues
*  GADM data: Good quality and resolution, but not an ontology in
   itself. Also not under a free license, does not allow redistribution
   or commercial use.


Evaluation
~~~~~~~~~~

Given the number of options, there is no obvious candidate to pick.
Therefore the team decided to define clear use cases and then evaluate
each options against them. However, due to time limitation, we did not
really get into this, will have to follow up in the next sprint. The
use cases so far were:

*  Annotate country of birth / of sampling [REQUIRED]
*  Encode higher resolution than country level if legally permitted and
   scientifically meaningful [RECOMMENDED].
*  Linking to geo-spatial coordinates [OPTIONAL]


Technical Questions
===================

Background and Problem
----------------------

Some nomenclature first: The nodes in an ontology graph are typically
either *concepts* (e.g., captial) or *instances* thereof (e.g., Paris).
These nodes have *local IDs* (often numbers), which are unique within
an ontology. They also typically have *labels*, which is the human-
readable name of the node. Nodes can have additional *attributes* (e.g.,
"population count") and are connected to other nodes by *relations*
(e.g. "is-a", "superset-of"), which create the edges of the graph.

The complete ontology is usually represented in an XML or OWL file.
However, we are looking for a *provider*, i.e. a service that
facilitates queries of an ontology via web and/or an API-based
interface. Upon querying with a unique ID, is it expected that a
*provider* will be able to return the record of a node, with should
contain all attributes and relations. Furthermore a *provider* might
allow set- and graph-based queries (e.g., is A a complete subset of B;
what is the last common ancestor of A and B). Finally a *provider* can
offer lookup services, i.e., identify the corresponding *concept* or
*instance* in another onotology. Until now we have mainly looked at
three providers: `Ontobee`_, `OLS`_ and `BioPortal`_. While they all
provide similar basic services, it should be noted that some biomedical
databases and repositories are, by convention, restricted to use certain
*providers*.

As stated above, each node has a *local ID*. To avoid conflicts between
the *local IDs* of multiple ontologies, *providers* and ontology
collections (e.g., OBO Foundry) use a `namespace`_, i.e., some
abbreviation for the ontology that is prefixed to the *local ID*.
However, as there no common standard how to create these prefixes, this
system is only unambiguous and collision-safe within a single
*provider*. To resolve this issue, ontologies often use International
Resource Identifiers (IRI, [RFC3987]_). While IRIs look like HTTP URLs,
they should primarily be considered as permanent and globally unique
identifiers, which might resolve to the node's record via DNS/HTTP, but
this is optional. In addition, potential intermediate URLs generated in
the DNS/HTTP resolving process must be considered internal and therefore
should not be used by third parties. Finally, it needs be noted that
IRIs should to be considered case-sensitive, especially when used as
identifiers (per [RFC3987]_, Section 5.3.2.1, which only excludes
the schema and host (authority) component for case-sensitivity).

While many ontologies already define an entities IRI on the level of the
ontology, there are some that do not. For such ontologies, IRIs are then
assigned by the provider. The most notable example for this are the UMLS
ontologies like the NCBI Taxonomy. This leads to the situation that a
single node in an ontology, stored by two providers can have different
IRIs. Therefore, a concept from NCBI Taxonomy, e.g., the duck-billed
platypus (``label:`` *Ornithorhynchus anatinus*, local ID: 9258) has
the IRI ``http://purl.obolibrary.org/obo/NCBITaxon_9258`` in Ontobee and
the IRI ``http://purl.bioontology.org/ontology/NCBITAXON/9258`` in
BioPortal. In addition, other providers might choose to use one of these
IRIs too, altough it will never resolve to their system via DNS/HTTP
(e.g., OLS uses the Ontobee IRIs).

For the AIRR Community, this creates the challenge that we want to be
able to have unambigous indentifiers, without requiring any specific
provider.


Proposed solution
-----------------

Compact URIs (`CURIEs`_) are a standardized way to abbreviate IRIs,
which includes URIs as a subset. They were originally conceived to
simplify the handling of attributes, e.g. in XML or SPARQL, by making
them more compact and readable. CURIEs are e.g. used by IEDB databases
to reduce redundancies (mainly in the leading part of IRIs).

A typical CURIE would, e.g., look like ``NCBITAXON:9258``. In this case,
``NCBITAXON`` is the *prefix*, a custom string that will be replaced by
a repository-defined IRI component (e.g.,
``http://purl.obolibrary.org/obo/NCBITaxon_``). Note that there is no
connection between ``NCBITAXON`` in the CURIE and ``NCBITaxon`` in the
IRI, the former one is just a placeholder.

This resolves the issue of different *providers* usings different IRIs
with distinct formating rules (as described above). As the choice of the
*provider* is independent for each ontologt, it allows greater
flexibility for the repositories, as they do not need a single
*provider* that needs be able to resolve all terms. Similarly, different
repositories can use the same ontology, but use a different *providers*.
Note that his would not require changes to the data, as this now only
contains CURIEs, not the (provider-specific) IRIs.

The AIRR schema will provide a list of AIRR approved CURIE *prefixes*
along with a list of at least one IRI *prefix* (i.e., replacement
string) for each them. This list serves two purposes:

1. It provides a controlled namespace for CURIE *prefixes* used in the
   AIRR schema. For now, custom additions to or replacements of these
   *prefixes* in the schema is prohibited. This does not affect the
   ability of repositories to use such custom prefixes internally.
2. It simplifies resolution for of CURIEs by non-repositories. The
   lists of IRI *prefixes* for each CURIE *prefix* should not be
   considered to be exhaustive. However, when using custom IRI
   *prefixes*, it must be ensured that they refer to the same
   ontology as the provides *prefixes*.

It should be explicitly noted that the IRI *prefix* list should not be
interpreted as any kind of recommendation for certain *providers*. It is
left up to users to decide how to resolve the resulting IRIs, e.g., via
DNS/HTTP (if possible) or by using a *provider* of their choice.


Modifications to the AIRR schema
================================

All changes to the AIRR schema that would be based on the sprint can
currently be reviewed on Github in Pull Request `#385`_. These changes
are supposed to be included into the next major release.


Clarifications
==============

*  Root nodes are specific to individual fields, not to an ontology.
   Therefore, NCBITAXON will use a root node of "Gnathostomata" for the
   annotations of the host species, but this would not be useful, e.g.,
   if it would be used to annotate pathogenic organisms, which will
   require a top node at the apex of the hierarchy.
*  The ``labels`` (previous: ``values``) that are provided in the schema
   for ontology-based fields, should be considered an addition for
   convenience and not as being authoritative. Repositories can choose
   to link synonyms to given concepts (e.g., "human" for
   "*Homo sapiens*") to simply search queries. Repositories further can
   provide such a synonym in the ``label`` field upon exporting data.
   However, repositories importing data should verify the correctness of
   ``labels`` that do not match the one provided by the ontology.
   Importing repositories must not be expected to allow for queries of
   ``labels`` other than those present in the ontology.


Annotation guidance
===================

*Note that this section is only a parking lot, the respective text will be moved into the AIRR Docs in the final version.*

*  Cells that come from Ficoll gradients should not be annotated as
   ``PBMCs`` as this is a sister node of ``lymphocyte``. For the
   other sampling related fields, in nearly all cases venous blood
   (``UBERON:0013756``) will be the correct ``tissue`` and it should
   be used in the case of ``sample_type``:``eripheral venous puncture``.
   However, if the mode of sampling is not specified, ``blood``
   (``UBERON:0000178``) should be used instead. Also see
   https://github.com/airr-community/airr-standards/issues/242


.. == Citations ==

.. [RFC3987] Internationalized Resource Identifiers (IRIs).
   `DOI:10.17487/RFC3987`_
   
.. == Link references ==

.. _`OBO Foundry Principles`: https://en.wikipedia.org/wiki/OBO_Foundry#Principles
.. _`rat strain ontology`: https://www.ebi.ac.uk/ols/ontologies/rs
.. _`ISO3166-1 alpha-2`: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
.. _`ISO3166-1 alpha-3`: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
.. _`M49`: https://unstats.un.org/unsd/methodology/m49
.. _`GAZ`: https://www.ebi.ac.uk/ols/ontologies/gaz
.. _`HANCESTRO`: https://www.ebi.ac.uk/ols/ontologies/hancestro
.. _`VBGEO`: https://www.vectorbase.org/ontology-browser
.. _`Ontobee`: http://www.ontobee.org/
.. _`OLS`: https://www.ebi.ac.uk/ols/index
.. _`BioPortal`: https://bioportal.bioontology.org
.. _`namespace`: https://en.wikipedia.org/wiki/Namespace
.. _`DOI:10.17487/RFC3987`: https://doi.org/10.17487/RFC3987
.. _`CURIEs`: https://www.w3.org/TR/curie
.. _`#385`: https://github.com/airr-community/airr-standards/pull/385
.. _`ViPR`: https://www.viprbrc.org
.. _`GSCID/BRC Project and Sample Application Standard`: https://www.niaid.nih.gov/research/human-pathogen-and-vector-sequencing-metadata-standards
.. _`GSCID/BRC Core Sample`: https://github.com/GSCID-BRC-Metadata-Standard-WG/GSCID-BRC-Project-and-Sample-Application-Standard/blob/master/NIAID%20GSC%20BRC_Core%20Metadata%20Standard_v1.3_Core_Sample_final.docx
.. _`ISO 6709`: https://en.wikipedia.org/wiki/ISO_6709
.. _`IRD`: https://www.fludb.org
.. _`Patric`: https://patricbrc.org
