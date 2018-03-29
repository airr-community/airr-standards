# Load schema from yaml file
definitions <- yaml::yaml.load_file("data-raw/definitions.yaml")
cast <- c("string"="c", "boolean"="l", "integer"="i", "number"="d")

# Define Alignment
AlignmentSchema <- definitions[["Alignment"]]
AlignmentSchema[["discriminator"]] <- AlignmentSchema[["type"]] <- NULL
alignment_fields <- names(AlignmentSchema[["properties"]])
AlignmentSchema[["optional"]] <- alignment_fields[!(alignment_fields %in% AlignmentSchema[["required"]])]
for (field in alignment_fields) {
    type <- AlignmentSchema[["properties"]][[field]][["type"]]
    AlignmentSchema[["properties"]][[field]][["cast"]] <- unname(cast[type])
}

# Define Rearrangement
RearrangementSchema <- definitions[["Rearrangement"]]
RearrangementSchema[["discriminator"]] <- RearrangementSchema[["type"]] <- NULL
rearrangement_fields <- names(RearrangementSchema[["properties"]])
RearrangementSchema[["optional"]] <- rearrangement_fields[!(rearrangement_fields %in% RearrangementSchema[["required"]])]
for (field in rearrangement_fields) {
    type <- RearrangementSchema[["properties"]][[field]][["type"]]
    RearrangementSchema[["properties"]][[field]][["cast"]] <- unname(cast[type])
}

# Save schema
devtools::use_data(AlignmentSchema, overwrite=TRUE)
devtools::use_data(RearrangementSchema, overwrite=TRUE)
