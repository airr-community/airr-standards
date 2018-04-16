.. _PythonAPI:

Python API
-------------------------------

Inferface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: airr.read_rearrangement

.. autofunction:: airr.create_rearrangement

.. autofunction:: airr.derive_rearrangement

.. autofunction:: airr.load_rearrangement

.. autofunction:: airr.write_rearrangement

.. autofunction:: airr.merge_rearrangement

.. autofunction:: airr.validate_rearrangement

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