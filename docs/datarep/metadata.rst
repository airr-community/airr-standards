.. _MetadataRepresentations:

Metadata Schema
=============================

AIRR datasets come with detailed metadata about the projects, samples, and
experimental details. These data generally correspond to the set of information
specified in the MiAIRR minimal reporting standards as described here and
published here.


Encoding
-----------------------------

Metadata files are YAML/JSON with a structure defined below. Files should be
encoded as UTF-8. Identifiers are case-sensitive. Files should have the
extension ``.yaml``, ``.yml``, or ``.json``.


Structure
-----------------------------

The MiAIRR metadata is hierarchical, and includes information about the study,
the subjects, the collected samples and how they are processed, details of the
sequencing protocol, and information about the data analysis. However, to
simplify processing of metadata, all information is stored in a denormalized
fashion. In particular, metadata in the file is organized as a list of YAML/JSON
objects containing key/value pairs encoding all of the MiAIRR data. This
information is denormalized so that if, for example, there are two blood samples
from the same subject, all the subject metadata will be replicated into the
object describing the results from each blood sample. (Put another way, metadata
is denormalized/replicated into the lowest level of the hierarchy.) Each YAML
object will contain a unique identifier ``repertoire_id``. This identifier can
be used to connect to data objects (e.g., ``rearrangements``).


Metadata objects, ``repertoire_id``, and ``rearrangement_set_id``
-----------------------------

Each metadata object/"blob" that has a ``repertoire_id`` is generally meant to
correspond to a physical sequencing library from with data can be generated.
However, this semantic notion is not rigorously required as different
experiments will have different organizations.

However, in some cases, it might make sense to allow for an arbitrary grouping
of AIRR data. For example, the results of a search query through a large set of
TCR sequences may warrant being grouped in a persistent way. Or because a single
dataset might be analyzed in multiple ways and the resulting ``rearrangement``
objects must be distinguished. In such situations, we have defined the
``rearrangement_set_id`` that can be used as the lowest-level identifier of
metadata blobs.

We expect that for most users in most situation, a ``repertoire_id`` and
``rearrangement_set_id`` will be semantically equivalent and only the former
should be used.


Schema
-----------------------------

+ The metadata file should correspond to a list of metadata objects.

+ Each metadata object should contain a top-level key/value pair for
  ``repertoire_id`` and optionally for ``rearrangement_set_id``.

+ The remaining top level keys should coorespond to the top-level MiAIRR
  categories, including ``study``, ``subject``, ``sample``. Each of these keys
  will contain a sub-object with specified keys and identifiers.

+ The full valid set of keys for each subobject corresponds to the CRWG API
  specification found here.

+ Some fields (as specified in the API spec) require the use of a particular
  ontology.


Joining to data
-----------------------------

The AIRR Python and R clients provide tools for reading and validating AIRR
metadata. In particular, metadata objects should be joined to AIRR data through
the ``repertoire_id`` fields. This means that AIRR data (e.g., rearrangement or
alignment data) should contain a ``repertoire_id`` column that is a foreign key
into the metadata YAML file.


References
-----------------------------

The metadata API defines the set of fields in the metadata. INCLUDE LINK.

An example metadata file is included in the repository as ``florian.airr.yaml``.
