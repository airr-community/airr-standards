validate_airr
-------------

**Validate AIRR data**

Description
~~~~~~~~~~~

``validate_airr`` validates compliance of the contents of a data.frame
to the AIRR data standards.

Usage
~~~~~

::

    validate_airr(data, schema = RearrangementSchema)

Arguments
~~~~~~~~~

data
    data.frame to validate.
schema
    ``Schema`` object defining the data standard.

Value
~~~~~

Returns ``TRUE`` if the input ``data`` is compliant and ``FALSE`` if
not.

Examples
~~~~~~~~

.. code:: r

    ### Not run:
    # Validate a data.frame against the Rearrangement schema
    # validate_airr(data, schema=RearrangementSchema)
