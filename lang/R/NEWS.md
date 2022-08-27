Version 1.4.0:  August 27, 2022
-------------------------------------------------------------------------------

Significant internal refactoring to improve schema generalizability,
harmonize behavior between the python and R libraries, and prepare for
AIRR Standards v2.0.
   
Rearrangement:

+ Added the `aux_types` argument to `read_tabular`, `read_rearrangement`, and 
  `read_alignment` to allow explicit declaration of the type for fields that 
  are not defined in the schema.
+ Renamed `read_airr`, `write_airr`, and `validate_airr` to `read_tabular`,
  `validate_tabular`, and `validate_tabular`, respectively.

Data Model and Schema:

+ Defined new `read_airr`, `write_airr`, and `validate_airr` functions that
  support AIRR Data Model files that store arrays of objects in JSON or YAML.
+ Added support for the AIRR Model Data File and associated schema
  (DataFile, Info). The Data File data format holds AIRR object of
  multiple types and is backwards compatible with Repertoire metadata.
+ Added support for the new germline and genotyping schema
  (GermlineSet, GenotypeSet) and associated schema.


Version 1.3.0:  May 26, 2020
-------------------------------------------------------------------------------
    
+ Updated schema set to v1.3.
+ Added `info` slot to `Schema` object containing general schema information.
  
Version 1.2.0:  August 17, 2018
-------------------------------------------------------------------------------
    
+ Updated schema set to v1.2.
+ Changed defaults to `base="1"` for read and write functions.
+ Updated example TSV file with coordinate changes, addition of 
  `germline_alignment` data and simplification of `sequence_id` values.

Version 1.1.0:  May 1, 2018
-------------------------------------------------------------------------------
    
Initial release.
