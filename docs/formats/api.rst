.. _API:

Python API
===============================

Inferface
-------------------------------

.. automodule:: airr
    :members:

Classes
-------------------------------

.. autoclass:: airr.io.RearrangementReader
    :members:
    :special-members:
    :exclude-members: fields, external_fields, __weakref__

.. autoclass:: airr.io.RearrangementWriter
    :members:
    :special-members:
    :exclude-members: fields, external_fields, __weakref__

.. autoclass:: airr.schema.Schema
    :members:

Schema
-------------------------------

.. autodata:: airr.schema.RearrangementSchema
    :annotation: Schema object for the Rearrangement definition

.. autodata:: airr.schema.AlignmentSchema
    :annotation: Schema object for the Alignment definition