.. _CloneSchema:

Clone and Lineage Tree Schema (Experimental)
============================================

A unique inferred clone object that has been constructed within a
single data processing for a single repertoire and a subset of its
sequences and/or rearrangements.

A clone object may have one or more inferred lineage trees. Each tree
is represented by a Newick string for its edges and a dictionary of
node objects.

File Format Specification
-------------------------

The file format has not been specified yet.

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

.. _TreeFields:

Tree Fields
------------------------------

:download:`Download as TSV <../_downloads/Clone.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Tree_schema %}
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
