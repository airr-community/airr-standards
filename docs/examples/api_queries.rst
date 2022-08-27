.. _DataCommonsQueries:

================================================================
Scientific Query Scenarios for AIRR Data Commons API
================================================================

The AIRR Common Repository Working Group (`CRWG`_) has defined a
number of sample scientific query scenarios to guide the design of the
ADC API. The `Design Decisions`_ document lists the
major design choices for the API, and the :ref:`API <DataCommonsAPI>` is currently defined
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
downloaded as JSON or in the :ref:`AIRR TSV format <RearrangementSchema>`.

.. _`CRWG`: https://www.antibodysociety.org/airrc/working_groups/repository/
.. _`Design Decisions`: https://github.com/airr-community/common-repo-wg/blob/master/decisions.md
.. _`OpenAPI V2.0 Specification`: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md

Query Example
---------------

What human full length TCR-beta sequences have junction amino acid sequence: “CASSYIKLN”?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The :download:`JSON query definition <queries/query1_repertoire.json>` for /repertoire endpoint. The ontology
  identifier ``9606`` requests human and ``TRB`` is the locus of interest.

.. literalinclude:: queries/query1_repertoire.json
  :language: JSON

- That query does not request full length sequences. We can enhance the :download:`query <queries/query1-1_repertoire.json>` by adding a clause for
  the ``sample.complete_sequences`` field.
  
.. literalinclude:: queries/query1-1_repertoire.json
  :language: JSON

- The :download:`JSON query definition <queries/query1_rearrangement.json>` for /rearrangement endpoint.
  The repertoire identifiers (``repertoire_id``) in the query are just examples, you would replace them with the actual identifiers
  returned from the above repertoire query. The query performs an exact match of the junction amino acid sequence.

.. literalinclude:: queries/query1_rearrangement.json
  :language: JSON

..
    Query Example 2
    ---------------

    What human full length IgH sequences have been found in patients with an autoimmune diagnosis.

    - TO BE WRITTEN

    Query Example 3
    ---------------

    What is the antibody IG heavy chain V usage in people who have diabetes?

    - TO BE WRITTEN

    Query Example 4
    ---------------

    Give me all the anti-HIV antibody sequences that use IGHV1-69 in HIV infected individuals?

    - TO BE WRITTEN

    Query Example 5
    ---------------

    Repertoires from cancer patients where we have pre- and post-immunotherapy peripheral blood (or tumor biopsy).

    - TO BE WRITTEN

    Query Example 6
    ---------------

    Return TCRs that score highly on a position weight matrix from subjects with a particular HLA allele that have been infected with TB.

    - TO BE WRITTEN

    Query Example 7
    ---------------

    Repertoires from female patients with cancer.

    - TO BE WRITTEN
