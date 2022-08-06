read_airr
---------

**Read an AIRR Data Model file in YAML or JSON format**

Description
~~~~~~~~~~~

``read_airr`` loads a YAML or JSON file containing AIRR Data Model
records.

Usage
~~~~~

::

   read_airr(file, format = c("auto", "yaml", "json"), validate = TRUE)

Arguments
~~~~~~~~~

file
   path to the input file.
format
   format of the input file. Must be one of ``"auto"``, ``"yaml"``, or
   ``"json"``. If ``"auto"`` (default), the format will be detected from
   the ``file`` extension.
validate
   run schema validation if ``TRUE``.

Value
~~~~~

A named nested ``list`` contained in the AIRR Data Model with the
top-level names reflecting the individual AIRR objects.

Examples
~~~~~~~~

.. code:: r

   # Get path to the Reportoire and GermlineSet example files
   f1 <- system.file("extdata", "repertoire-example.yaml", package="airr")
   f2 <- system.file("extdata", "germline-example.json", package="airr")

   # Load data files
   repertoire <- read_airr(f1)
   germline <- read_airr(f2)

*Warning*:Warning: GermlineSet object is missing AIRR mandatory
field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions *Warning*:Warning:
GermlineSet object is missing AIRR mandatory field(s): germline_set_id,
author, lab_name, lab_address, release_version, release_description,
release_date, germline_set_name, germline_set_ref, species, locus,
allele_descriptions *Warning*:Warning: GermlineSet object is missing
AIRR mandatory field(s): germline_set_id, author, lab_name, lab_address,
release_version, release_description, release_date, germline_set_name,
germline_set_ref, species, locus, allele_descriptions

See also
~~~~~~~~

See `Schema <Schema-class.html>`__ for the AIRR schema definition objects.
See `write_airr <write_airr.html>`__ for writing AIRR Data Model records
in YAML or JSON format.
