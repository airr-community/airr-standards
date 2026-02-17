load_schema
-----------

**Load a schema definition**

Description
~~~~~~~~~~~

``load_schema`` loads an AIRR object definition from the internal
definition set.

Usage
~~~~~

::

   load_schema(definition)

Arguments
~~~~~~~~~

definition
   name of the schema definition.

Value
~~~~~

A `Schema <Schema-class.html>`__ object for the ``definition``.

Details
~~~~~~~

Valid definitions include:

- ``"Rearrangement"``
- ``"Alignment"``
- ``"Repertoire"``
- ``"Study"``
- ``"Subject"``
- ``"Diagnosis"``
- ``"Sample"``
- ``"SampleProcessing"``
- ``"DataProcessing"``
- ``"GermlineSet"``
- ``"GenotypeSet"``

Examples
~~~~~~~~

.. code:: r

   # Load the Rearrangement definition
   schema <- load_schema("Rearrangement")

   # Load the Repertoire definition
   schema <- load_schema("Repertoire")

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the return object.
