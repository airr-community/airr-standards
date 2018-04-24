Schema-class
------------

**S4 class defining an AIRR standard schema**

Description
~~~~~~~~~~~

``Schema`` defines a common data structure for AIRR standards.

Usage
~~~~~

::

    "names"(x)

::

    "["(x, i)

::

    "$"(x, name)

Arguments
~~~~~~~~~

x
    ``Schema`` object.
i
    field name.
name
    field name.

Slots
~~~~~

``required``
    ``character`` vector of required fields.
``optional``
    ``character`` vector of non-required fields.
``properties``
    ``list`` of field definitions.

See also
~~~~~~~~

See `load_schema <load_schema.md>`__ loading a ``Schema`` from
definitions file.
