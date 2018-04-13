.. _PythonAPI:

Python API
-------------------------------

Inferface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: airr.read

.. autofunction:: airr.create

.. autofunction:: airr.derive

.. autofunction:: airr.load

.. autofunction:: airr.write

.. autofunction:: airr.merge

.. autofunction:: airr.validate

Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autodata:: airr.schema.RearrangementSchema
    :annotation: Schema object for the Rearrangement definition

.. autodata:: airr.schema.AlignmentSchema
    :annotation: Schema object for the Alignment definition