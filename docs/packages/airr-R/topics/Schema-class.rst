Schema-class
------------

**S4 class defining an AIRR standard schema**

Description
~~~~~~~~~~~

``Schema`` defines a common data structure for AIRR Data Representation
standards.

Usage
~~~~~

::

   "names"(x)

::

   "["(x, i)

::

   "$"(x, name)

::

   InfoSchema

::

   DataFileSchema

::

   RearrangementSchema

::

   RepertoireSchema

::

   GermlineSetSchema

::

   GenotypeSetSchema

::

   AIRRSchema

Arguments
~~~~~~~~~

x
   ``Schema`` object.
i
   field name.
name
   field name.

Format
~~~~~~

A ``Schema`` object.

An object of class ``Schema`` of length 1.

An object of class ``Schema`` of length 1.

An object of class ``Schema`` of length 1.

An object of class ``Schema`` of length 1.

An object of class ``Schema`` of length 1.

An object of class ``Schema`` of length 1.

An object of class ``Schema`` of length 1.

An object of class ``list`` of length 26.

Details
~~~~~~~

The following predefined Schema objects are defined:

``InfoSchema``: AIRR Info ``Schema``.

``DataFileSchema``: AIRR DataFile ``Schema``.

``RearrangementSchema``: AIRR Rearrangement ``Schema``.

``RepertoireSchema``: AIRR Repertoire ``Schema``.

``GermlineSetSchema``: AIRR GermlineSet ``Schema``.

``GenotypeSetSchema``: AIRR GenotypeSet ``Schema``.

``AIRRSchema``: named list containing all non-experimental AIRR
``Schema`` objects.

Slots
~~~~~

``definition``
   name of the schema definition.
``required``
   ``character`` vector of required fields.
``optional``
   ``character`` vector of non-required fields.
``properties``
   ``list`` of field definitions.
``info``
   ``list`` schema information.

See also
~~~~~~~~

See `load_schema <load_schema.html>`__ for loading a ``Schema`` from the
definition set.
