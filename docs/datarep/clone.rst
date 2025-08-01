.. _CloneSchema:

Clone Schema
============================================

A ``Clone`` object groups a set of ``Rearrangements`` or ``Cells`` that are
inferred to be related by common descent from a single naive ancestor. The
member ``Rearrangements`` and ``Cells`` are referenced from ``Clone`` as an
array of ``Nodes`` and can include inferred ancestors that were not directly
observed. All members of a ``Clone`` must be from either a single 
``RepertoireGroup`` or from a single ``Repertoire`` if a ``RepertoireGroup``
was not created.

A ``Node`` links members of a ``Clone`` to their original metadata and 
annotations.

File Format Specification
-------------------------

Files are YAML/JSON with an AIRR Data File structure. Files should be
encoded as UTF-8. Identifiers are case-sensitive. Files should have the
extension ``.yaml``, ``.yml``, or ``.json``.

File Structure
~~~~~~~~~~~~~~

+ The `DataFile` is a dictionary (key/value pair) structure with the keys ``Clone`` and ``Node``.

+ The file can (optionally) contain an ``Info`` object, at the beginning of the file, based upon the ``Info`` schema in the OpenAPI V2 specification. If provided, ``version`` in ``Info`` should reference the version of the AIRR schema for the file.

+ The file should correspond to a list of ``Clone`` objects, using ``Clone`` as the key to the list.

+ The file should correspond to a list of ``Node`` objects, using ``Node`` as the key to the list.

+ Each ``Clone`` object should contain a top-level key/value pair for ``clone_id`` that uniquely identifies the clone and a top-level key/value pair for *either* ``repertoire_group_id`` *or* ``repertoire_id`` that identifies the source of the clone's members.

+ Each ``Node`` object should contain top-level key/value pairs for ``node_id`` (uniquely identifies the node) and ``repertoire_id`` (identifies the source repertoire).

+ Some fields require the use of a particular ontology or controlled vocabulary.

+ The structure is the same regardless of whether the data is stored in a file or a data repository.
.. _CloneFields:

Clone Fields
------------------------------

:download:`Download as TSV <../_downloads/Clone.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Clone_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _NodeFields:

Node Fields
------------------------------

:download:`Download as TSV <../_downloads/Node.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Node_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}
