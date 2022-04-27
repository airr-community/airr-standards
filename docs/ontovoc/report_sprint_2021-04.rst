===============================
OntoVoc Report - Sprint 04/2021
===============================

Objectives
==========

The objectives of this third sprint in April 2021 were to:

*  Revisit General Policies
*  CURIE for PIDs 
*  Assess whether the use of multiple ontologies for single fields
   should be allowed
*  Use of IDs and labels
*  Provide guidance on ``cell_population`` annotation


General Policies
================

The OntoVoc team revisited the criteria for ontologies used in the AIRR
schema that it :ref:`defined in the 11/2018 sprint <ONTO_CRIT_2018>` and
that were expanded in the 04/2020 sprint to include the
`OBO Foundry Principles`_.


CURIEs for PIDs
===============

This is not directly related to ontologies, but as it does touch upon
the use of CURIEs in the AIRR Schema, it does fall into the scope of
OntoVoc. Main question is whether and how we can use, e.g., ORCIDs
in Repos (see `#476`_). The top-level conclusion on this topic is that
CURIE can be used by repositories for non-ontology PIDs, but that
the exact specification should be addresses by ComRepo WG. However,
it should be noted that there are two functions a CURIE can serve:

*  A CURIE can be used to create a unique ID. In this case the prefix
   serves as/provides a namespace.
*  An expanded CURIE (i.e. URI) can be used to retrieve data, i.e.,
   using it as a PID in the strict sense.

As there is no standard what type of information is provided by an URI
(in the second case) there should be hints in the schema, e.g., on
human vs. machine-readable data.


Use of multiple ontologies for a single field
=============================================

While it sometime would be preferable to have multiple ontologies
available for a given field, the group came to the conclusing that this
is would more likely than not reduce the interoperability of the data:

*  Overlaps between two accepted ontologies would be problematic as this
   creates an ambiguity about which term to use. This ambiguity
   jeopardizes the linkage possibilities that ontologies should provide.
*  Although OLS has a term-mapping service, this does not ensure that
   the same term in two different ontologies represents the same
   concept. Also the logical structure between ontologies might differ,
   complicating things even further.
*  There might however be very special and restricted use cases in which
   ontologies are orthogonal to each other and therefore the union of
   both could be used. This would in addition require a common structure
   that should exists for OBO ontologies. However, until there is a
   clear use case for this that cannot be solved in any other way, we
   will not allow multiple ontologies per term.


Use of IDs and labels
=====================

It should be reiterated that:

*  The ``id`` is the authorative and required part of the information,
   the ``label`` is at the discretion of the repository and is
   provided to the user as complementrary information (so that the user
   does not need to resolve the ``id``).
*  Repositories MUST support searches for the official label term, they
   SHOULD support ontology synonyms and they MAY support their own
   synonyms (termed “alias”).
*  Data returned by a repository MUST provide the official term as 
   ``label``  and MAY provide or not provide a set of synonyms/aliases
   in the novel ``synonyms`` array.
*  The behavior of a ``synonyms`` field can be altered by the user
   query.
*  Some PID types might not have a meaningful label. Therefore ``label``
   MAY be NULL.


Provide guidance on ``cell_population`` annotation
==================================================

Added to documentation


.. == Citations ==

.. == Link references ==

.. _`OBO Foundry Principles`: https://en.wikipedia.org/wiki/OBO_Foundry#Principles
.. _`CURIEs`: https://www.w3.org/TR/curie
.. _`#476`: https://github.com/airr-community/airr-standards/issues/476
