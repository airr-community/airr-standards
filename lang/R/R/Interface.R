#### Read TSV ####

#' Read AIRR tabular data
#' 
#' \code{read_tabular} reads a tab-delimited (TSV) file containing tabular AIRR records.
#'
#' @param    file        input file path.
#' @param    base        starting index for positional fields in the input file.
#'                       If \code{"1"}, then these fields will not be modified.
#'                       If \code{"0"}, then fields ending in \code{"_start"} and \code{"_end"}
#'                       are 0-based half-open intervals (python style) in the input file
#'                       and will be converted to 1-based closed-intervals (R style).
#' @param    schema      \code{Schema} object defining the output format.
#' @param    aux_types   named vector or list giving the type for fields that are not
#'                       defined in \code{schema}. The field name is the name, the value
#'                       the type, denoted by one of \code{"c"} (character), \code{"l"} (logical),
#'                       \code{"i"} (integer), \code{"d"} (double), or \code{"n"} (numeric).
#' @param    ...         additional arguments to pass to \link[readr]{read_delim}.
#'
#' @return   A \code{data.frame} of the TSV file with appropriate type and position conversion
#'           for fields defined in the specification.
#'
#' @seealso
#' See \link{Schema} for the AIRR schema object definition.
#' See \link{write_tabular} for writing AIRR data.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
#'
#' # Load data file
#' df <- read_rearrangement(file)
#'
#' @export
read_tabular <- function(file, schema, base=c("1", "0"), aux_types=NULL,...) {
    # Check arguments
    base <- match.arg(base)

    # Define types
    parsers <- c("character"="c", "logical"="l", "integer"="i", "double"="d", "numeric"="n")
    header <- names(suppressMessages(readr::read_tsv(file, n_max=1)))
    schema_fields <- intersect(names(schema), header)
    cast <- setNames(lapply(schema_fields, function(f) parsers[schema[f]$type]), schema_fields)
    cast <- c(cast, list(.default = col_character()))

    if(!is.null(aux_types)){
        aux_types <- aux_types[names(aux_types) %in% header]
        aux_cols <- setNames(lapply(aux_types, function(f) parsers[f]), names(aux_types))
        cast <- c(cast, aux_cols)
    }

    types <- do.call(readr::cols, cast)

    # Read file
    data <- suppressMessages(readr::read_tsv(file, col_types=types, na=c("", "NA", "None"), ...))
    
    # Validate file
    valid_data <- validate_tabular(data, schema=schema)
    
    # Adjust indexes
    if (base == "0") {
        start_positions <- grep("_start$", names(data), perl=TRUE)
        if (length(start_positions) > 0) {
            data[, start_positions] <- data[, start_positions] + 1
        }
    }

    return(data)
}


#' @details
#' \code{read_rearrangement} reads an AIRR TSV containing Rearrangement data.
#' 
#' @rdname read_tabular
#' @export
read_rearrangement <- function(file, base=c("1", "0"), ...) {
  read_tabular(file, base=base, schema=RearrangementSchema, ...)
}


#### Read YAML/JSON ####

#' Read an AIRR Data Model file in YAML or JSON format
#' 
#' \code{read_airr} loads a YAML or JSON file containing AIRR Data Model records.
#'
#' @param    file      path to the input file.
#' @param    format    format of the input file. Must be one of \code{"auto"}, \code{"yaml"}, or 
#'                     \code{"json"}. If \code{"auto"} (default), the format will be 
#'                     detected from the \code{file} extension.
#' @param    validate  run schema validation if \code{TRUE}.
#' @param    model     if \code{TRUE} validate only AIRR DataFile defined objects. If \code{FALSE} 
#'                     attempt validation of all objects in \code{data}.
#'                     Ignored if \code{validate=FALSE}
#' 
#' @return   A named nested \code{list} contained in the AIRR Data Model with the top-level
#'           names reflecting the individual AIRR objects.
#'                   
#' @seealso  
#' See \link{Schema} for the AIRR schema definition objects.
#' See \link{write_airr} for writing AIRR Data Model records in YAML or JSON format.
#' 
#' @examples
#' # Get path to the Reportoire and GermlineSet example files
#' f1 <- system.file("extdata", "repertoire-example.yaml", package="airr")
#' f2 <- system.file("extdata", "germline-example.json", package="airr")
#' 
#' # Load data files
#' repertoire <- read_airr(f1)
#' germline <- read_airr(f2)
#' 
#' @export
read_airr <- function(file, format=c("auto", "yaml", "json"), validate=TRUE, model=TRUE) {
    # Check arguments
    format <- match.arg(format)
    
    # Autodetect format
    if (format == "auto") { format <- tolower(tools::file_ext(file)) }
    
    # Load data
    if (format == "yaml") {
        records <- read_airr_yaml(file, validate=validate, model=model)
    } else if (format == "json") {
        records <- read_airr_json(file, validate=validate, model=model)
    } else {
        stop("Unrecognized file extension ", format, "; must be either .json or .yaml.")
    }
    
    # Return
    return(records)
}

# Read an AIRR YAML file
# 
# \code{read_airr_yaml} loads a YAML file containing AIRR Data Model records.
#
# @param    file      path to the YAML input file.
# @param    validate  run schema validation if \code{TRUE}.
# @param    model     if \code{TRUE} validate only AIRR DataFile defined objects. If \code{FALSE} 
#                     attempt validation of all objects in \code{data}.
#                     Ignored if \code{validate=FALSE}
#                      
# @return   A named nested \code{list} contained in the AIRR Data Model with the top-level
#           names reflecting the individual AIRR objects.
#                   
# @seealso  
# See \link{Schema} for the AIRR schema definition objects.
# See \link{write_airr_yaml} for writing AIRR data in YAML format.
# 
# @examples
# # Get path to the repertoire-example file
# file <- system.file("extdata", "repertoire-example.yaml", package="airr")
# 
# # Load data file
# repr <- read_airr_yaml(file)
read_airr_yaml <- function(file, validate=TRUE, model=TRUE) {
  
  # YAML format
  data <- yaml::read_yaml(file)

  # Validation. Warnings are thrown for fields for AIRR compliance failures
  if (validate) {
      valid <- validate_airr(data, model=model)
  }
  
  return(data)
}


# Read an AIRR JSON file
# 
# \code{read_airr_json} loads a JSON file containing AIRR Data Model records.
#
# @param    file      path to the JSON input file.
# @param    validate  run schema validation if \code{TRUE}.
# @param    model     if \code{TRUE} validate only AIRR DataFile defined objects. If \code{FALSE} 
#                     attempt validation of all objects in \code{data}.
#                     Ignored if \code{validate=FALSE}
#
# @return   A named nested \code{list} contained in the AIRR Data Model with the top-level
#           names reflecting the individual AIRR objects.
#                   
# @seealso  
# See \link{Schema} for the AIRR schema object definition.
# See \link{write_airr_json} for writing AIRR data in JSON format.
# 
# @examples
# # Get path to the rearrangement-example file
# file <- system.file("extdata", "germline-example.json", package="airr")
# 
# # Load data file
# repr <- read_airr_json(file)
read_airr_json <- function(file, validate=TRUE, model=TRUE) {
  
  # Read JSON format
  data <- jsonlite::fromJSON(file, 
                             simplifyVector=TRUE,
                             simplifyMatrix=FALSE,
                             simplifyDataFrame=FALSE,
                             flatten=FALSE)
  
  # Validation. Warnings are thrown for fields for AIRR compliance failures
  if (validate) {
      valid <- validate_airr(data, model=model)
  }
  
  return(data)
}

#### Write TSV ####

#' Write an AIRR tabular data
#' 
#' \code{write_tabular} writes a TSV containing AIRR tabular records.
#'
#' @param    data    \code{data.frame} of Rearrangement data.
#' @param    file    output file name.
#' @param    base    starting index for positional fields in the output file.
#'                   Fields in the input \code{data} are assumed to be 1-based
#'                   closed-intervals (R style).
#'                   If \code{"1"}, then these fields will not be modified.
#'                   If \code{"0"}, then fields ending in \code{_start} and \code{_end}
#'                   will be converted to 0-based half-open intervals (python style)
#'                   in the output file.
#' @param    schema  \code{Schema} object defining the output format.
#' @param    ...     additional arguments to pass to \link[readr]{write_delim}.
#'
#' @return   NULL
#'
#' @seealso
#' See \link{Schema} for the AIRR schema object definition.
#' See \link{read_tabular} for reading to AIRR files.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
#'
#' # Load data file
#' df <- read_rearrangement(file)
#'
#' # Write a Rearrangement data file
#' outfile <- file.path(tempdir(), "output.tsv")
#' write_tabular(df, outfile, schema=RearrangementSchema)
#'
#' @export
write_tabular <- function(data, file, schema, base=c("1", "0"),  ...) {
    ## DEBUG
    # data <- data.frame("sequence_id"=1:4, "extra"=1:4, "a"=LETTERS[1:4])

    data_name <- deparse(substitute(data))
    schema_name <- deparse(substitute(schema))

    # Check arguments
    base <- match.arg(base)

    # Fill in missing required columns
    missing <- setdiff(schema@required, names(data))
    if (length(missing) > 0 ) {
        data[, missing] <- NA
    }

    # order columns
    ordering <- c(intersect(names(schema), names(data)),
                  setdiff(names(data), names(schema)))
    data <- data[, ordering]

    # Adjust indexes
    if (base == "0") {
        start_positions <- grep("_start$", names(data), perl=TRUE)
        if (length(start_positions) > 0) {
            data[, start_positions] <- data[, start_positions] - 1
        }
    }
    valid <- suppressWarnings(validate_tabular(data, schema))
    if (!valid) {
        w <- names(warnings())
        w <- gsub("Warning: *", "" ,w)
        err_msg <- paste0(data_name, " is not a valid ", schema_name, "\n")
        err_msg <- paste(err_msg, paste(w, collapse = "\n"))
        warning(err_msg)
    }


    # write logical fields as T/F
    logical_fields <- names(which(sapply(schema@properties,
                                         '[[', "type") == "logical"))
    logical_fields <- intersect(colnames(data), logical_fields)
    if (length(logical_fields) > 0 ) {
        for (log_field in logical_fields) {
            logical_values <- data[[log_field]] %in% c(TRUE, FALSE)
            data[[log_field]] <- as.character(data[[log_field]])
            if (length(logical_values) > 0 ) {
                data[[log_field]][logical_values] <- c("T", "F")[match(data[[log_field]][logical_values],
                                                            c("TRUE", "FALSE"))]
            }
        }
    }

    # Write
    write_tsv(data, file, na="", ...)
}


#' @details
#' \code{write_rearrangement} writes a \code{data.frame} containing AIRR Rearrangement data to TSV.
#' 
#' @rdname write_tabular
#' @export
write_rearrangement <- function(data, file, base=c("1", "0"), ...) {
    write_tabular(data, file, base=base, schema=RearrangementSchema, ...)
}


#### Write YAML/JSON ####

#' Write AIRR Data Model records to YAML or JSON files
#' 
#' \code{write_airr} writes a YAML or JSON file containing AIRR Data Model records.
#'
#' @param    data      \code{list} containing AIRR Model Records.
#' @param    file      output file name.
#' @param    format    format of the output file. Must be one of \code{"auto"}, \code{"yaml"}, or 
#'                     \code{"json"}. If \code{"auto"} (default), the format will be 
#'                     detected from the \code{file} extension.
#' @param    validate  run schema validation prior to write if \code{TRUE}.
#' @param    model     if \code{TRUE} validate and write only AIRR DataFile defined objects. 
#'                     If \code{FALSE} attempt validation and write of all objects in \code{data}.
#' 
#' @seealso
#' See \link{Schema} for the AIRR schema definition objects.
#' See \link{read_airr} for reading to AIRR Data Model files.
#' 
#' @examples
#' # Get path to the repertoire-example file
#' file <- system.file("extdata", "repertoire-example.yaml", package="airr")
#' 
#' # Load data file
#' repertoire <- read_airr(file)
#' 
#' # Write a Rearrangement data file
#' outfile <- file.path(tempdir(), "output.yaml")
#' write_airr(repertoire, outfile)
#' 
#' @export
write_airr <- function(data, file, format=c("auto", "yaml", "json"), validate=TRUE, model=TRUE) {
    # Check arguments
    format <- match.arg(format)
    
    # Autodetect format
    if (format == "auto") { format <- tolower(tools::file_ext(file)) }
    
    # Write data
    if (format == "yaml") {
        write_airr_yaml(data, file, validate=validate, model=model)
    } else if (format == "json") {
        write_airr_json(data, file, validate=validate, model=model)
    } else {
        stop("Unrecognized file extension ", format, "; must be either .json or .yaml.")
    }
}


# Write an AIRR yaml
# 
# \code{write_airr_yaml} writes a yaml containing AIRR formatted records.
#
# @param    data      object containing Repertoire data.
# @param    file      output file name.
# @param    validate  run schema validation prior to write if \code{TRUE}.
# @param    model     if \code{TRUE} validate only AIRR DataFile defined objects. If \code{FALSE} 
#                     attempt validation of all objects in \code{data}.
# 
# @seealso
# See \link{Schema} for the AIRR schema object definition.
# See \link{read_airr_yaml} for reading to AIRR files.
# 
# @examples
# # Get path to the rearrangement-example file
# file <- system.file("extdata", "repertoire-example.yaml", package="airr")
# 
# # Load data file
# repr <- read_airr(file)
# 
# # Write a Rearrangement data file
# outfile <- file.path(tempdir(), "output.yaml")
# write_airr_yaml(repr, outfile)
write_airr_yaml <- function(data, file, validate=TRUE, model=TRUE) {
    # Validate prior to write
    if (validate) {
        valid <- validate_airr(data, model=model)
    }
    
    # Subset to AIRR DataFile records
    if (model) {
        data <- data[names(data) %in% names(DataFileSchema@properties)]
    }
    
    # Write
    yaml::write_yaml(data, file)
}

# Write an AIRR json
# 
# \code{write_airr_json} writes a yaml containing AIRR formatted records.
#
# @param    data    object containing Repertoire data.
# @param    file    output file name.
# @param    validate  run schema validation prior to write if \code{TRUE}.
#
# @return   NULL
# 
# @seealso
# See \link{Schema} for the AIRR schema object definition.
# See \link{read_airr_json} for reading to AIRR files.
# 
# @examples
# # Get path to the rearrangement-example file
# file <- system.file("extdata", "germline-example.json", package="airr")
# 
# # Load data file
# repr <- read_airr(germline)
# 
# # Write a Rearrangement data file
# outfile <- file.path(tempdir(), "output.json")
# write_airr_json(repr, outfile)
write_airr_json <- function(data, file, validate=TRUE, model=TRUE) {
    # Validate prior to write
    if (validate) {
        valid <- validate_airr(data, model=model)
    }
  
    # Subset to AIRR DataFile records
    if (model) {
        data <- data[names(data) %in% names(DataFileSchema@properties)]
    }
    
    # Write
    json <- jsonlite::toJSON(data, auto_unbox=TRUE, null="null", na="null")
    write(json, file)
}


#### Validation ####

#' Validate tabular AIRR data
#' 
#' \code{validate_tabular} validates compliance of the contents of a \code{data.frame} 
#' to the AIRR standards.
#'
#' @param    data    \code{data.frame} of tabular data to validate.
#' @param    schema  \code{Schema} object defining the data standard of the table.
#'
#' @return   Returns \code{TRUE} if the input \code{data} is compliant and
#'           \code{FALSE} if not.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
#'
#' # Load data file
#' df <- read_rearrangement(file)
#'
#' # Validate a data.frame against the Rearrangement schema
#' validate_rearrangement(df)
#' 
#' @export
validate_tabular <- function(data, schema) {
    # Initialize return value
    valid <- TRUE
    
    # Check all required fields exist
    missing_fields <- setdiff(schema@required, names(data))
    
    if (length(missing_fields) > 0 ) {
        valid <- FALSE
        warning(paste("Warning: File is missing AIRR mandatory field(s):",
                      paste(missing_fields, collapse = ", ")))
    }
    
    # Validate sequence_id: 
    # - uniqueness
    # - not empty
    if ("sequence_id" %in% colnames(data)) {
        dup_ids <- duplicated(data[['sequence_id']])
        if (any(dup_ids)) {
            valid <- FALSE
            warning(paste("Warning: sequence_id(s) are not unique:",
                          paste(data[['sequence_id']][dup_ids], collapse = ", ")))
        }
        empty_rows <- which(data[['sequence_id']] %in% c("None", "", NA))
        if (length(empty_rows) > 0 ) {
            # TODO
            # valid <- FALSE
            warning(paste("Warning: sequence_id is empty for row(s):",
                          paste(empty_rows, collapse = ", ")))           
        }
    }
    
    # check logical fields
    logical_fields <- names(which(sapply(schema@properties, 
                                         '[[', "type") == "logical"))
    logical_fields <- intersect(colnames(data), logical_fields)
    if (length(logical_fields) > 0 ) {
        for (log_field in logical_fields) {
            not_logical <- data[[log_field]] %in% c(TRUE, FALSE, NA) == FALSE
            if (any(not_logical)) {
                warning(paste("Warning:",log_field,"is not logical for row(s):",
                              paste(which(not_logical), collapse = ", ")))            
            } else {
                NULL
            }
        }
    }
    
    return(valid)
}

#' @details
#' \code{validate_rearrangement} validates the standards compliance of AIRR Rearrangement 
#' data stored in a \code{data.frame}
#' 
#' @rdname validate_tabular
#' @export
validate_rearrangement <- function(data) {
    validate_tabular(data, schema=RearrangementSchema)
}


#' Validate an AIRR Data Model nested list representation
#' 
#' \code{validate_airr} validates the fields in a named nested list representation of the 
#' AIRR Data Model. Typically, generating by reading of JSON or YAML formatted AIRR files.
#'
#' @param    data     \code{list} containing records of an AIRR Data Model objected imported from 
#'                    a YAML or JSON representation.
#' @param    model    if \code{TRUE} validate only AIRR DataFile defined objects. If \code{FALSE} 
#'                    attempt validation of all objects in \code{data}.
#' @param    each     if \code{TRUE} return a logical vector with results for each object in \code{data}
#'                    instead of a single \code{TRUE} or \code{FALSE} value.
#' 
#' @return   Returns \code{TRUE} if the input \code{data} is compliant with AIRR standards and
#'           \code{FALSE} if not. If \code{each=TRUE} is set, then a vector with results for each
#'           each object in \code{data} is returned instead.
#'                   
#' @seealso  
#' See \link{Schema} for the AIRR schema definitions.
#' See \link{read_airr} for loading AIRR Data Models from a file.
#' See \link{write_airr} for writing AIRR Data Models to a file.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' f1 <- system.file("extdata", "repertoire-example.yaml", package="airr")
#' f2 <- system.file("extdata", "germline-example.json", package="airr")
#' 
#' # Load data file
#' repertoire <- read_airr(f1)
#' germline <- read_airr(f2)
#' 
#' # Validate a single record
#' validate_airr(repertoire)
#' 
#' # Return validation for individual objects
#' validate_airr(germline, each=TRUE)
#' 
#' @export
validate_airr <- function(data, model=TRUE, each=FALSE) {
    # This is a wrapper function to allow recursive validation of the different entries in yaml file
    # Directly calling validate_entry does not work, because the function
    # validate_entry also needs to work for recursive calling of reference schemes
    
    # Iterate through objects in input data
    valid_sum <- logical()
    for (n in names(data)) {
        if (n %in% c('Info', 'DataFile')) { next }
        entry <- data[[n]]
        if (is.null(entry)) { next }

        # Check for non-DataFile objects
        if (model && !(n %in% names(DataFileSchema@properties))) { 
            warning('Skipping validation of non-DataFile object: ', n)
            next 
        }
        
        # Load schema
        if (n %in% names(AIRRSchema)) { 
            schema <- AIRRSchema[[n]] 
        } else { 
            schema <- tryCatch(load_schema(n), error=function(e) NULL)
        }
        
        # Fail invalid schema
        if (is.null(schema)) {
            warning('Unrecognized schema: ', n)
            valid <- FALSE
        } else {
            # Recursively validate all entries
            valid <- sapply(entry, validate_entry, schema=schema)
        }
        
        # Store check result
        valid_sum <- append(setNames(all(valid), n), valid_sum)
    }
    
    # Data only valid if all entries valid
    if (!each) { valid_sum <- all(valid_sum) }
    
    return(valid_sum)
}


# Validation function for a single entry in the yaml file
#
# @param    entry    AIRR data in a nested list structure
# @param    schema             Schema definition object
# @returns  TRUE or FALSE
validate_entry <- function(entry, schema) {
    schema_name <- schema@definition
    valid <- TRUE

    # Check all required fields exist
    missing_fields <- setdiff(schema@required, names(entry))
    
    if (length(missing_fields) > 0 ) {
        valid <- FALSE
        warning(paste("Warning:", schema_name, "object is missing AIRR mandatory field(s):",
                      paste(missing_fields, collapse = ", "), "\n"))
    }
    
    # loop through all fields in the list and check if they refer to other schemes
    for(f in names(entry)) {
        # get the reference scheme
        reference_schemes <- schema[f]$ref
        
        # simple recursive (reference scheme in 1st level)
        # in this case the type on the 1st level is NULL
        if (is.na(schema[f][["type"]]) || is.null(schema[f][["type"]])) {
            if (!is.null(reference_schemes)) {
                # check whether an ontology is a list, before recursing into it.
                if (reference_schemes@definition == "Ontology" & class(entry[[f]]) != "list") {
                    valid <- FALSE
                    warning(paste("Warning: Property", paste(schema_name, ".", f, sep=""),
                                "should be an ontology but is of class", class(entry[[f]]), "\n"))
                } else {
                    v <- validate_entry(entry[[f]], schema=reference_schemes)
                    if (!v) { valid <- FALSE }
                }
            }
        # entry of array type with a list of on or several reference schemes
        } else if (schema[f][["type"]] == "array" & !is.null(reference_schemes)) {
            # this is the number of different reference schemes
            n_schemes <- length(reference_schemes)
            # this is the number of elements in the array
            n_array_entries <- length(entry[[f]])
            # loop over all reference schemes in list
            for (n_ref in seq_len(n_schemes)) {
                # recursively validate the entries in the array
                for (n_array in seq_len(n_array_entries)) {
                    v <- validate_entry(entry[[f]][[n_array]], schema = reference_schemes[[n_ref]])
                    if (!v) { valid <- FALSE }
                }
            }
        # check if the entry type is correct
        } else if (class(entry[[f]]) != schema[f][["type"]]) {
            # one reason for non-identical types can be that the entry is nullable
            nullable <- schema[f][["x-airr"]][["nullable"]]
            # if not specified, it should be nullable
            if (is.null(nullable)) { nullable <- TRUE }
            if (!(nullable & is.null(entry[[f]]))) {
                # another reason for types not matching is the array format
                # we test whether the entries are lists
                if (!(schema[f][["type"]] == "array" & is.vector(entry[[f]]))) {
                    # another reason for types not matching is the numeric arguments being read as integers
                    # we test whether the entries are numeric
                    if (!(schema[f][["type"]] == "numeric" & is.numeric(entry[[f]]))) {
                        valid <- FALSE
                        warning(paste("Warning:", schema_name, "entry does not have the required type",
                                      schema[f][["type"]], ":", f, "\n"))
                    }  
                }
            }
        }
    }
    
    # return to indicate whether entries are valid
    return(valid)
}
