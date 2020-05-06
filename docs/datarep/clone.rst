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

.. list-table::
    :widths: 20, 10, 10, 60
    :header-rows: 1

    * - Name
      - Type
      - MiAIRR
      - Description
    {%- for field in Clone_schema %}
    * - ``{{ field.name }}``
      - {{ field.type }}
      - ``{{ field.miairr }}``
      - {{ field.description | trim }}
    {%- endfor %}

.. _TreeFields:

Tree Fields
------------------------------

.. list-table::
    :widths: 20, 10, 10, 60
    :header-rows: 1

    * - Name
      - Type
      - MiAIRR
      - Description
    {%- for field in Tree_schema %}
    * - ``{{ field.name }}``
      - {{ field.type }}
      - ``{{ field.miairr }}``
      - {{ field.description | trim }}
    {%- endfor %}

.. _NodeFields:

Node Fields
------------------------------

.. list-table::
    :widths: 20, 10, 10, 60
    :header-rows: 1

    * - Name
      - Type
      - MiAIRR
      - Description
    {%- for field in Node_schema %}
    * - ``{{ field.name }}``
      - {{ field.type }}
      - ``{{ field.miairr }}``
      - {{ field.description | trim }}
    {%- endfor %}
