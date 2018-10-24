================================================================
Sample Scientific Query Scenarios for AIRR Common Repository API
================================================================

Introduction
============

The AIRR Common Repository Working Group (`CRWG`_) has defined a
number of sample scientific query scenarios to guide the design of the
common repository API. The `Design Decisions`_ document lists the
major design choices for the API, and the `API`_ is currently defined
using the `OpenAPI V2.0 Specification`_. This document describes the
query examples with associated JSON definitions that can be submitted
to an AIRR repository.

There are two main query endpoints in the API: /repertoire for
querying MiAIRR-compliant study metadata and /rearrangement for
querying rearrangement annotations. Most scientific queries will
involve both endpoints. The basic workflow involves first
querying /repertoire to get the list of repertoires that meet the
search criteria on study, subject, and sample metadata. Secondly, the
identifiers from the repertoires in the first query are passed to
the /rearrangement endpoint along with any search criteria on the
rearrangement annotations. The resultant rearrangements can be
downloaded as JSON or in `AIRR TSV format`_.

.. _`CRWG`: https://www.antibodysociety.org/airrc/working_groups/repository/
.. _`Design Decisions`: https://github.com/airr-community/common-repo-wg/blob/master/decisions.md
.. _`API`: https://github.com/airr-community/airr-standards/blob/master/specs/common_repository_api.yaml
.. _`OpenAPI V2.0 Specification`: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md
.. _`AIRR TSV format`: http://docs.airr-community.org/en/latest/datarep/overview.html

Query Example 1 (Bjoern)
========================

What human full length TCR-beta sequences have CDR3 region: “CASSYIKLN”? 

- `query1_repertoire.json`_ is the JSON query definition for /repertoire endpoint.

- `query1_rearrangement.json`_ is the JSON query definition for /rearrangement endpoint.

.. _`query1_repertoire.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query1_repertoire.json
.. _`query1_rearrangement.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query1_rearrangement.json

Query Example 2 (Lindsay)
=========================

What human full length IgH sequences have been found in patients with an autoimmune diagnosis.

- `query2_repertoire.json`_ is the JSON query definition for /repertoire endpoint.

- `query2_rearrangement.json`_ is the JSON query definition for /rearrangement endpoint.

.. _`query2_repertoire.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query2_repertoire.json
.. _`query2_rearrangement.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query2_rearrangement.json

Query Example 3 (Corey)
=======================

What is the antibody IG heavy chain V usage in people who have diabetes?

- `query3_repertoire.json`_ is the JSON query definition for /repertoire endpoint.

- `query3_rearrangement.json`_ is the JSON query definition for /rearrangement endpoint.

.. _`query3_repertoire.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query3_repertoire.json
.. _`query3_rearrangement.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query3_rearrangement.json

Query Example 4 (Felix)
=======================

Give me all the anti-HIV antibody sequences that use IGHV1-69 in HIV infected individuals?

- `query4_repertoire.json`_ is the JSON query definition for /repertoire endpoint.

- `query4_rearrangement.json`_ is the JSON query definition for /rearrangement endpoint.

.. _`query4_repertoire.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query4_repertoire.json
.. _`query4_rearrangement.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query4_rearrangement.json

Query Example 5 (Lindsay)
=========================

Repertoires from cancer patients where we have pre- and post-immunotherapy peripheral blood (or tumor biopsy).

- `query5_repertoire.json`_ is the JSON query definition for /repertoire endpoint.

- `query5_rearrangement.json`_ is the JSON query definition for /rearrangement endpoint.

.. _`query5_repertoire.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query5_repertoire.json
.. _`query5_rearrangement.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query5_rearrangement.json

Query Example 6 (Uri)
=====================

Return TCRs that score highly on a position weight matrix from subjects with a particular HLA allele that have been infected with TB.

- `query6_repertoire.json`_ is the JSON query definition for /repertoire endpoint.

- `query6_rearrangement.json`_ is the JSON query definition for /rearrangement endpoint.

.. _`query6_repertoire.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query6_repertoire.json
.. _`query6_rearrangement.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query6_rearrangement.json

Query Example 7 (iReceptor Gateway v2.0 Repertoire)
=====================

Search MiAIRR meta-data at the study/sample/subject level to return a set of repertoires of interest. 

- `query7_repertoire_female_cancer.json`_ is an example JSON query definition that returns all of the repertoires that are from female patients with a sample disease state containing the string "cancer". Features of this query are that it uses a substring "contains" query and lists all of the fields that the current iReceptor Gateway displays by default for each repertoire. It also ask for a **summary statistic** return value that is currently not supported in the API, the "repertoire rearrangement count". This value represent the total number of rearrangements for the repertoire. 

- `query7_repertiore_all.json`_ is an example JSON query definition that returns all of the repertiores that satisfy the search criteria when all of the iReceptor Gateway search fields have a value in them.

.. _`query7_repertoire_female_cancer.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query7_repertoire_female_cancer.json
.. _`query7_repertiore_all.json`: https://github.com/airr-community/airr-standards/blob/master/lang/python/examples/query7_repertiore_all.json
