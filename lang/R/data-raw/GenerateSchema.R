# Load
AlignmentSchema <- airr::load_schema("Alignment")
RearrangementSchema <- airr::load_schema("Rearrangement")

# Save
devtools::use_data(AlignmentSchema, overwrite=TRUE)
devtools::use_data(RearrangementSchema, overwrite=TRUE)
