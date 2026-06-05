R Library Release Notes
=======================

Version 2.0.0: June 5, 2026
---------------------------

Deprecation and Removal:

- Completely removed ``read_alignment``, ``write_alignment``, and
  ``AlignmentSchema``. Removed “Alignment” from the valid definitions
  list and ``AIRRSchema``.

Tabular Data and Parsing:

- Updated ``read_tabular`` to initially treat logical columns as
  character data to prevent silent ``NA`` conversions during parsing,
  then explicitly casting valid logical character values.
- Updated ``validate_tabular`` to support character strings representing
  logical values (e.g., “TRUE”, “T”, “False”, “F”) when validating
  logical fields.

Validation:

- Enhanced ``validate_entry`` to support comprehensive validation of
  arrays without reference schemas, including item type checking
  (string, integer, number, boolean) and enum constraints.
- Added rigorous type and enum validation for individual fields within
  ``validate_entry``, providing explicit warnings for unrecognized
  types.
- Added an ontology validation check in ``validate_entry`` to ensure
  that an ontology field is structured as a list before performing
  recursive validation.

Data Model and Schema:

- Updated ``AIRRSchema`` to replace the ``Acknowledgement`` schema with
  the new ``Contributor`` schema.
- Added a safety check in ``extract_field_content`` to handle fields
  with null properties safely.
- 

Version 1.6.1: February 12, 2026
--------------------------------

- Sync version with release of python airr package.

Version 1.6.0: July 7, 2025
---------------------------

- Updated schema set.

Version 1.5.0: August 29, 2023
------------------------------

- Updated schema set and examples to v1.5.

Version 1.4.1: August 27, 2022
------------------------------

Significant internal refactoring to improve schema generalizability,
harmonize behavior between the python and R libraries, and prepare for
AIRR Standards v2.0.

Rearrangement:

- Added the ``aux_types`` argument to ``read_tabular``,
  ``read_rearrangement``, and ``read_alignment`` to allow explicit
  declaration of the type for fields that are not defined in the schema.
- Renamed ``read_airr``, ``write_airr``, and ``validate_airr`` to
  ``read_tabular``, ``validate_tabular``, and ``validate_tabular``,
  respectively.

Data Model and Schema:

- Defined new ``read_airr``, ``write_airr``, and ``validate_airr``
  functions that support AIRR Data Model files that store arrays of
  objects in JSON or YAML.
- Added support for the AIRR Model Data File and associated schema
  (DataFile, Info). The Data File data format holds AIRR object of
  multiple types and is backwards compatible with Repertoire metadata.
- Added support for the new germline and genotyping schema (GermlineSet,
  GenotypeSet) and associated schema.

Version 1.3.0: May 26, 2020
---------------------------

- Updated schema set to v1.3.
- Added ``info`` slot to ``Schema`` object containing general schema
  information.

Version 1.2.0: August 17, 2018
------------------------------

- Updated schema set to v1.2.
- Changed defaults to ``base="1"`` for read and write functions.
- Updated example TSV file with coordinate changes, addition of
  ``germline_alignment`` data and simplification of ``sequence_id``
  values.

Version 1.1.0: May 1, 2018
--------------------------

Initial release.
