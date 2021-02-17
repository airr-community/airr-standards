#### AIRR Input, tsv format ####

#' Read an AIRR TSV
#' 
#' \code{read_airr_tsv} reads a TSV containing AIRR records.
#'
#' @param    file    input file path.
#' @param    base    starting index for positional fields in the input file. 
#'                   If \code{"1"}, then these fields will not be modified.
#'                   If \code{"0"}, then fields ending in \code{"_start"} and \code{"_end"}
#'                   are 0-based half-open intervals (python style) in the input file 
#'                   and will be converted to 1-based closed-intervals (R style).
#' @param    schema  \code{Schema} object defining the output format.
#' @param    ...     additional arguments to pass to \link[readr]{read_delim}.
#' 
#' @return   A data.frame of the TSV file with appropriate type and position conversion
#'           for fields defined in the specification.
#'                   
#' @seealso  
#' See \link{Schema} for the AIRR schema object definition.
#' See \link{write_airr} for writing AIRR data.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
#' 
#' # Load data file
#' df <- read_rearrangement(file)
#' 
#' @export
read_airr_tsv <- function(file, base=c("1", "0"), schema=RearrangementSchema, ...) {
    # Check arguments
    base <- match.arg(base)

    # Define types
    parsers <- c("character"="c", "logical"="l", "integer"="i", "double"="d")
    header <- names(suppressMessages(readr::read_tsv(file, n_max=1)))
    schema_fields <- intersect(names(schema), header)
    cast <- setNames(lapply(schema_fields, function(f) parsers[schema[f]$type]), schema_fields)
    types <- do.call(readr::cols, cast)
    
    # Read file
    data <- suppressMessages(readr::read_tsv(file, col_types=types, na=c("", "NA", "None"), ...))
    
    # Validate file
    valid_data <- validate_airr_tsv(data, schema=schema)
    
    # Adjust indexes
    if (base == "0") {
        start_positions <- grep("_start$", names(data), perl=TRUE)
        if (length(start_positions) > 0) {
            data[, start_positions] <- data[, start_positions] + 1
        }
    }

    return(data)
}

#' Validate AIRR data
#' 
#' \code{validate_airr_tsv} validates compliance of the contents of a data.frame 
#' to the AIRR data standards.
#'
#' @param    data    data.frame to validate.
#' @param    schema  \code{Schema} object defining the data standard.
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
#' validate_airr_tsv(df, schema=RearrangementSchema)
#' 
#' @export
validate_airr_tsv <- function(data, schema=RearrangementSchema){
  
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
      not_logical <- data[[log_field]] %in% c(TRUE, FALSE) == FALSE
      if (any(not_logical)) {
        warning(paste("Warning:",log_field,"is not logical for row(s):",
                      paste(which(not_logical), collapse = ", ")))            
      } else {
        NULL
      }
    }
  }
  
  valid
}

#' @details
#' \code{read_rearrangement} reads an AIRR TSV containing Rearrangement data.
#' 
#' @rdname read_airr_tsv
#' @export
read_rearrangement <- function(file, base=c("1", "0"), ...) {
  read_airr_tsv(file, base=base, schema=RearrangementSchema, ...)
}


#' @details
#' \code{read_alignment} reads an AIRR TSV containing Alignment data.
#' 
#' @rdname read_airr_tsv
#' @export
read_alignment <- function(file, base=c("1", "0"), ...) {
  read_airr_tsv(file, base=base, schema=AlignmentSchema, ...)
}


#### AIRR Input, yaml format ####

#' Read an AIRR yaml
#' 
#' \code{read_airr_yaml} reads a yaml containing AIRR records.
#'
#' @param    file    input file path in yaml format.
#' @param    schema  \code{Schema} object defining the output format.
#' 
#' @return   An object of the data contained in the input file.
#'                   
#' @seealso  
#' See \link{Schema} for the AIRR schema object definition.
#' See \link{write_airr_yaml} for writing AIRR data in yaml format.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' file <- system.file("tests/data-tests/", "good_repertoire.airr.yaml", package="airr")
#' 
#' # Load data file
#' df <- read_repertoire(file)
#' 
#' @export

read_airr_yaml <- function(file, schema=RepertoireSchema) {
  
  # if file is of type YAML, load as YAML
  data <- yaml.load_file(file)
  # could be replaced by the name of the schema
  definition_list_all <- data[[1]]
  
  valid <- validate_airr_yaml(yaml_list = definition_list_all, schema = schema)
  
  return(data)
}

#' Validate an AIRR yaml
#' 
#' \code{validate_airr_yaml} reads a yaml containing AIRR records.
#'
#' @param    yaml_list  Data object from yaml import. This data contains the AIRR records.
#' @param    schema  \code{Schema} object defining the output format.
#' @param    ...     additional arguments to pass to \link[readr]{read_delim}.
#' 
#' @return   Returns \code{TRUE} if the input \code{yaml_list} is compliant with AIRR standards and
#'           \code{FALSE} if not. 
#'                   
#' @seealso  
#' See \link{Schema} for the AIRR schema object definition.
#' See \link{write_airr} for writing AIRR data.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' file <- system.file("tests/data-tests/", "good_repertoire.airr.yaml", package="airr")
#' 
#' # Load data file
#' df <- read_repertoire(file)
#' # validate
#' df <- validate_airr_yaml(df[["Repertoire"]])
#' 
#' @export

# This is a wrapper function to allow recursive validation of the different entries in yaml file
# Directly calling validate_airr_yaml_entry does not work, because the function
# validate_airr_yaml_entry also needs to work for recursive calling of reference schemes
validate_airr_yaml <- function(yaml_list, schema = RepertoireSchema) {
  # yaml file can contain multiple entries
  entries_n <- seq_len(length(yaml_list))

  # recursively validate all entries
  valid_list <- sapply(entries_n,  function(X) validate_airr_yaml_entry(yaml_list[[X]], schema = schema))

  # data only valid if all entries valid
  return(all(valid_list))
}


# Validation function for a single entry in the yaml file
validate_airr_yaml_entry <- function(definition_list, schema=RearrangementSchema){
  
  valid <- TRUE
  
  # Check all required fields exist
  missing_fields <- setdiff(schema@required, names(definition_list))
  
  if (length(missing_fields) > 0 ) {
    valid <- FALSE
    warning(paste("Warning: File is missing AIRR mandatory field(s):",
                  paste(missing_fields, collapse = ", "), "\n"))
  }
  
  # loop through all fields in the list and check if they refer to other schemes
  for(f in names(definition_list)) {
    
    # get the reference scheme
    reference_schemes <- schema[f]$ref
    
    # simple recursive (reference scheme in 1st level)
    # in this case the type on the 1st level is NULL
    if (is.null(schema[f][["type"]])) {
      if (!is.null(reference_schemes)) {
        valid <- validate_airr_yaml_entry(definition_list[[f]], schema = reference_schemes)
      }
      # entry of array type with a list of on or several reference schemes
    } else if (schema[f][["type"]] == "array" & !is.null(reference_schemes)) {
      # this is the number of different reference schemes
      n_schemes <- length(reference_schemes)
      # this is the number of elements in the array
      n_array_entries <- length(definition_list[[f]])
      # loop over all reference schemes in list
      for (n_ref in seq_len(n_schemes)) {
          # recursively validate the entries in the array
        for (n_array in seq_len(n_array_entries)) {
          valid <- validate_airr_yaml_entry(definition_list[[f]][[n_array]], schema = reference_schemes[[n_ref]])
        }
      }
    }
  }
  # we do not cover the case when type == "object", in the case of germline for example
  
  # return to indicate whether entries are valid
  return(valid)
}

#' @details
#' \code{read_repertoire} reads a YAML file containing AIRR Repertoire data.
#' 
#' @rdname read_airr_yaml
#' @export
read_repertoire <- function(file, ...) {
  read_airr_yaml(file, schema=RepertoireSchema)
}


#### AIRR output, tsv format ####

#' Write an AIRR TSV
#' 
#' \code{write_airr_tsv} writes a TSV containing AIRR formatted records.
#'
#' @param    data    data.frame of Rearrangement data.
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
#' See \link{read_airr_tsv} for reading to AIRR files.
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
#' write_rearrangement(df, outfile)
#' 
#' @export
write_airr_tsv <- function(data, file, base=c("1", "0"), schema=RearrangementSchema, ...) {
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
    
    valid <- suppressWarnings(validate_airr_tsv(data, schema))
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
#' \code{write_rearrangement} writes a data.frame containing AIRR Rearrangement data to TSV.
#' 
#' @rdname write_airr_tsv
#' @export
write_rearrangement <- function(data, file, base=c("1", "0"), ...) {
    write_airr_tsv(data, file, base=base, schema=RearrangementSchema, ...)
}


#' @details
#' \code{write_alignment} writes a data.frame containing AIRR Alignment data to TSV.
#' 
#' @rdname write_airr_tsv
#' @export
write_alignment <- function(data, file, base=c("1", "0"), ...) {
    write_airr_tsv(data, file, base=base, schema=AlignmentSchema, ...)
}

#### AIRR output, yaml format ####

#' Write an AIRR yaml
#' 
#' \code{write_airr_yaml} writes a yaml containing AIRR formatted records.
#'
#' @param    data    object containing Repertoire data.
#' @param    file    output file name.
#' @param    schema  \code{Schema} object defining the output format.
#' @param    ...     additional arguments to pass to \link[readr]{write_delim}.
#'
#' @return   NULL
#' 
#' @seealso
#' See \link{Schema} for the AIRR schema object definition.
#' See \link{read_airr} for reading to AIRR files.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' system.file("tests/data-tests/", "good_repertoire.airr.yaml", package="airr")
#' 
#' # Load data file
#' df <- read_repertoire(file)
#' 
#' # Write a Rearrangement data file
#' outfile <- file.path(tempdir(), "output.yaml")
#' write_repertoire(df, outfile)
#' 
#' @export
write_airr_yaml <- function(data, file, schema=RepertoireSchema, ...) {

  # run a validation
  definition_list_all <- data[[1]]
  
  valid <- validate_airr_yaml(yaml_list = definition_list_all, schema = schema)
  
  # what kind of other tests do we need to implement here?
  # where does the data come from?

  # Write
  yaml::write_yaml(data, file)
}


#' @details
#' \code{write_repertoire} writes a object containing AIRR Repertoire data to yaml.
#' 
#' @rdname write_airr_yaml
#' @export
write_repertoire <- function(data, file, ...) {
  write_airr_yaml(data, file, schema=RepertoireSchema, ...)
}
