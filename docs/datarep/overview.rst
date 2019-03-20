.. _DataRepresentations:

AIRR Data Representations
=============================

AIRR Data Representations are versioned specifications that consist of
a file format and a well-defined schema. The schema is provided in a
machine-readable YAML document that follows the OpenAPI v2.0
specification. The schema defines the data model, field names, data
types, and encodings for AIRR standard objects. Strict typing enables
interoperability and data sharing between different AIRR-seq analysis
tools and repositories, and some fields use a controlled vocabulary or
an ontology for value restriction. Specification extensions are
utilized to define AIRR-specific attributes.

Schema Definitions
-----------------------------

.. toctree::
   :maxdepth: 2

   Repertoire Schema <metadata>
   Rearrangement Schema <rearrangements>
   Alignment Schema (Experimental) <alignments>
