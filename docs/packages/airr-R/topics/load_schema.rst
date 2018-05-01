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

-  ``"Rearrangement"``
-  ``"Alignment"``
-  ``"Study"``
-  ``"Subject"``
-  ``"Diagnosis"``
-  ``"Sample"``
-  ``"CellProcessing"``
-  ``"NucleicAcidProcessing"``
-  ``"RawSequenceData"``
-  ``"SoftwareProcessing"``

Examples
~~~~~~~~

.. code:: r

    # Load the rearrangement definition
    schema <- load_schema("Rearrangement")

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the return object.
