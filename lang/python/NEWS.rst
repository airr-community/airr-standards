Version 1.4.0:  In development
--------------------------------------------------------------------------------

1. Updated pandas requirement to 0.24.0 or higher.
2. Added support for missing integer values (``NaN``) in ``load_rearrangement``
   by casting to the pandas ``Int64`` data type.
3. Added support for arrays of objects
4. Added support for GermlineSet and GenotypeSet and associated objects
5. Added support for the AIRR Data File, which is a combined data format to hold
   AIRR object of multiple types. It is backwards compatible with Repertoire metadata.
6. Deprecated ``load_repertoire``. Use ``load_airr_data`` instead.
7. Deprecated ``write_repertoire``. Use ``write_airr_data`` instead.
8. Deprecated ``validate_repertoire``. Use ``validate_airr_data`` instead.
9. Fixed a bug in the ``validate`` subcommand of ``airr-tools`` causing
   validation errors to only be reporting for the first invalid file when
   multiple files were specified on the command line.

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