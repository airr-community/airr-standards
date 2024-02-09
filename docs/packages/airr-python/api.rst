.. _PythonAPI:

API Reference
================================================================================

Rearrangement Interface
--------------------------------------------------------------------------------

.. autofunction:: airr.read_rearrangement

.. autofunction:: airr.create_rearrangement

.. autofunction:: airr.derive_rearrangement

.. autofunction:: airr.load_rearrangement

.. autofunction:: airr.dump_rearrangement

.. autofunction:: airr.merge_rearrangement

.. autofunction:: airr.validate_rearrangement


AIRR Data Model Interface
--------------------------------------------------------------------------------

.. autofunction:: airr.read_airr

.. autofunction:: airr.write_airr

.. autofunction:: airr.validate_airr


Classes
--------------------------------------------------------------------------------

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
--------------------------------------------------------------------------------

.. autodata:: airr.schema.InfoSchema
    :annotation: Schema object for the Info definition

.. autodata:: airr.schema.DataFileSchema
    :annotation: Schema object for the DataFile definition

.. autodata:: airr.schema.AlignmentSchema
    :annotation: Schema object for the Alignment definition

.. autodata:: airr.schema.RearrangementSchema
    :annotation: Schema object for the Rearrangement definition

.. autodata:: airr.schema.RepertoireSchema
    :annotation: Schema object for the Repertoire definition

.. autodata:: airr.schema.GermlineSetSchema
    :annotation: Schema object for the Repertoire definition

.. autodata:: airr.schema.GenotypeSetSchema
    :annotation: Schema object for the Repertoire definition


Deprecated
--------------------------------------------------------------------------------

.. autofunction:: airr.load_repertoire

.. autofunction:: airr.write_repertoire

.. autofunction:: airr.validate_repertoire

.. autofunction:: airr.repertoire_template