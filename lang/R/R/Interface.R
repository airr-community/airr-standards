#### Rearrangement I/O ####

#' Read an AIRR TSV
#' 
#' \code{read_airr} reads a TSV containing AIRR records.
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
read_airr <- function(file, base=c("1", "0"), schema=RearrangementSchema, ...) {
    # Check arguments
    base <- match.arg(base)
    
    # Define types
    parsers <- c("character"="c", "logical"="l", "integer"="i", "double"="d", "array"="a")

    # later, since first the recursive schema calling has to be fixed
    cast <- setNames(lapply(schema_fields, function(f) parsers[schema[f]$type]), schema_fields)
    
    # if file is of type TSV, load as TSV
    header <- names(suppressMessages(readr::read_tsv(file, n_max=1)))
    schema_fields <- intersect(names(schema), header)
    cast <- setNames(lapply(schema_fields, function(f) parsers[schema[f]$type]), schema_fields)
    types <- do.call(readr::cols, cast)
    
    # Read file
    data <- suppressMessages(readr::read_tsv(file, col_types=types, na=c("", "NA", "None"), ...))
    
    
    
    # Validate file
    valid_data <- validate_airr(data, schema=schema)
    
    # Adjust indexes
    if (base == "0") {
        start_positions <- grep("_start$", names(data), perl=TRUE)
        if (length(start_positions) > 0) {
            data[, start_positions] <- data[, start_positions] + 1
        }
    }

    return(data)
}


#### Rearrangement I/O ####

validate_airr_yaml_1 <- function(n_entry, schema, definition_list) {

  fields <- names(definition_list[[n_entry]])
  schema_fields <- intersect(names(schema), fields)
  
  # Validate file
  validate_airr_yaml_2(definition_list[[n_entry]], schema=schema)
}

#' Read an AIRR TSV
#' 
#' \code{read_airr} reads a TSV containing AIRR records.
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

read_airr_yaml <- function(file, schema=RepertoireSchema, ...) {
  
  # if file is of type YAML, load as YAML
  data <- yaml.load_file(file)
  # could be replaced by the name of the schema
  definition_list_all <- data[[1]]
  
  entries <- seq_len(length(definition_list_all))
  sapply(entries, validate_airr_yaml_1, schema = schema, definition_list = definition_list_all)
  
  return(data)
}


# make it recursive, since one repertoire file may contain several repertoire_ids
validate_airr_yaml_2 <- function(definition_list, schema=RearrangementSchema){
  
  valid <- TRUE
  
  # Check all required fields exist
  missing_fields <- setdiff(schema@required, names(definition_list))
  
  if (length(missing_fields) > 0 ) {
    valid <- FALSE
    warning(paste("Warning: File is missing AIRR mandatory field(s):",
                  paste(missing_fields, collapse = ", ")))
  }
  
  
  # check the fields with reference
  for(f in names(definition_list)) {
    # get the reference scheme
    reference_scheme <- schema[f]$ref
    if(!is.null(reference_scheme)) {
        #recursively validate the entries
        validate_airr_yaml_2(definition_list[[f]], schema = reference_scheme)
    }
  }
}


#' Validate AIRR data
#' 
#' \code{validate_airr} validates compliance of the contents of a data.frame 
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
#' validate_airr(df, schema=RearrangementSchema)
#' 
#' @export
validate_airr <- function(data, schema=RearrangementSchema){
    
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
#' @rdname read_airr
#' @export
read_rearrangement <- function(file, base=c("1", "0"), ...) {
    read_airr(file, base=base, schema=RearrangementSchema, ...)
}


#' @details
#' \code{read_alignment} reads an AIRR TSV containing Alignment data.
#' 
#' @rdname read_airr
#' @export
read_alignment <- function(file, base=c("1", "0"), ...) {
    read_airr(file, base=base, schema=AlignmentSchema, ...)
}

#' @details
#' \code{read_repertoire} reads a YAML file containing AIRR Repertoire data.
#' 
#' @rdname read_airr
#' @export
read_repertoire <- function(file, base=c("1", "0"), ...) {
  read_airr_yaml(file, base=base, schema=RepertoireSchema, ...)
}


#' Write an AIRR TSV
#' 
#' \code{write_airr} writes a TSV containing AIRR formatted records.
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
#' See \link{read_airr} for reading to AIRR files.
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
write_airr <- function(data, file, base=c("1", "0"), schema=RearrangementSchema, ...) {
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
    
    valid <- suppressWarnings(validate_airr(data, schema))
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
#' @rdname write_airr
#' @export
write_rearrangement <- function(data, file, base=c("1", "0"), ...) {
    write_airr(data, file, base=base, schema=RearrangementSchema, ...)
}


#' @details
#' \code{write_alignment} writes a data.frame containing AIRR Alignment data to TSV.
#' 
#' @rdname write_airr
#' @export
write_alignment <- function(data, file, base=c("1", "0"), ...) {
    write_airr(data, file, base=base, schema=AlignmentSchema, ...)
}
