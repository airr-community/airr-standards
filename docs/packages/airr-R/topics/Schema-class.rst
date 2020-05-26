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

   AlignmentSchema

::

   RearrangementSchema

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

Details
~~~~~~~

The following predefined Schema objects are defined:

``AlignmentSchema``: AIRR Alignment ``Schema``.

``RearrangementSchema``: AIRR Rearrangement ``Schema``.

Slots
~~~~~

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
definition set. See `read_airr <read_airr.html>`__,
`write_airr <write_airr.html>`__ and `validate_airr <validate_airr.html>`__
schema operators.
