Version 1.5.0:  August 31, 2023
--------------------------------------------------------------------------------

1. Updated schema set and examples to v1.5.
2. Officially dropped support for Python 2.
3. Added check for valid enum values to schema validation routines.
4. Set enum values to first defined value during template generation routines.
5. Removed mock dependency installation in ReadTheDocs environments from setup.
6. Improved package import time.


Version 1.4.1:  August 27, 2022
--------------------------------------------------------------------------------

General:

1. Updated pandas requirement to 0.24.0 or higher.
2. Added support for missing integer values (``NaN``) in ``load_rearrangement``
   by casting to the pandas ``Int64`` data type.
3. Added gzip support to ``read_rearrangement``.
4. Significant internal refactoring to improve schema generalizability,
   harmonize behavior between the python and R libraries, and prepare for
   AIRR Standards v2.0.
5. Fixed a bug in the ``validate`` subcommand of ``airr-tools`` causing
   validation errors to only be reporting for the first invalid file when
   multiple files were specified on the command line.

Data Model and Schema:

1. Added support for arrays of objects in a single JSON or YAML file.
2. Added support for the AIRR Data File and associated schema
   (DataFile, Info). The Data File data format holds AIRR object of
   multiple types and is backwards compatible with Repertoire metadata.
3. Added support for the new germline and genotyping schema
   (GermlineSet, GenotypeSet) and associated schema.
4. Renamed ``schema.CachedSchema`` to ``schema.AIRRSchema``.
5. Removed ``specs/blank.airr.yaml``.

Deprecations:

1. Deprecated ``load_repertoire``. Use ``read_airr`` instead.
2. Deprecated ``write_repertoire``. Use ``write_airr`` instead.
3. Deprecated ``validate_repertoire``. Use ``validate_airr`` instead.
4. Deprecated ``repertoire_template``. Use ``schema.RepertoireSchema.template`` instead.
5. Deprecated the commandline tool ``airr-tools validate repertoire``.
   Use ``airr-tools validate airr`` instead.


Version 1.3.1:  October 13, 2020
--------------------------------------------------------------------------------

1. Refactored ``merge_rearrangement`` to allow for larger number of files.
2. Improved error handling in format validation operations.


Version 1.3.0:  May 30, 2020
--------------------------------------------------------------------------------

1. Updated schema set to v1.3.
2. Added ``load_repertoire``, ``write_repertoire``, and ``validate_repertoire``
   to ``airr.interface`` to read, write and validate Repertoire metadata,
   respectively.
3. Added ``repertoire_template`` to ``airr.interface`` which will return a
   complete repertoire object where all fields have ``null`` values.
4. Added ``validate_object`` to ``airr.schema`` that will validate a single
   repertoire object against the schema.
5. Extended the ``airr-tools`` commandline program to validate both rearrangement
   and repertoire files.


Version 1.2.1:  October 5, 2018
--------------------------------------------------------------------------------

1. Fixed a bug in the python reference library causing start coordinate values
   to be empty in some cases when writing data.


Version 1.2.0:  August 17, 2018
--------------------------------------------------------------------------------

1. Updated schema set to v1.2.
2. Several improvements to the ``validate_rearrangement`` function.
3. Changed behavior of all `airr.interface` functions to accept a file path
   (string) to a single Rearrangement TSV, instead of requiring a file handle
   as input.
4. Added ``base`` argument to ``RearrangementReader`` and ``RearrangementWriter``
   to support optional conversion of 1-based closed intervals in the TSV to
   python-style 0-based half-open intervals. Defaults to conversion.
5. Added the custom exception ``ValidationError`` for handling validation checks.
6. Added the ``validate`` argument to ``RearrangementReader`` which will raise
   a ``ValidationError`` exception when reading files with missing required
   fields or invalid values for known field types.
7. Added ``validate`` argument to all type conversion methods in ``Schema``,
   which will now raise a ``ValidationError`` exception for value that cannot be
   converted when set to ``True``. When set ``False`` (default), the previous
   behavior of assigning ``None`` as the converted value is retained.
8. Added ``validate_header`` and ``validate_row`` methods to ``Schema`` and
   removed validations methods from ``RearrangementReader``.
9. Removed automatic closure of file handle upon reaching the iterator end in
   ``RearrangementReader``.


Version 1.1.0:  May 1, 2018
--------------------------------------------------------------------------------

Initial release.