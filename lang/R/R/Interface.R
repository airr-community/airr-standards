#### Rearrangement I/O ####

#' Read an AIRR Rearrangement TSV
#' 
#' \code{read_airr} reads a TSV container AIRR Rearrangement records.
#'
#' @param    file    input file path.
#' @param    base    starting index for positional fields in the input file. 
#'                   If \code{0}, then fields ending in \code{_start} and \code{_end}
#'                   are 0-based half-open intervals (python style) in the input file 
#'                   and will be converted to 1-based closed-intervals (R style). 
#'                   If \code{1}, then these fields will not be modified.
#' 
#' @return   A data.frame of the TSV file with appropriate type and position conversion
#'           for fields defined in the specification.
#'                   
#' @seealso  See \link{write_airr} for writing to AIRR Rearrangement data.
#' 
#' @examples
#' \dontrun{
#'   # Read a TSV file with default options
#'   df <- read_airr("file.tsv")
#' }
#' 
#' @export
read_airr <- function(file, base=0 ) {
    # Check arguments
    base_choices <- c(0,1)
    base <- match.arg(as.character(base), base_choices)

    # Define types
    parsers <- c("character"="c", "logical"="l", "integer"="i", "double"="d")
    header <- names(suppressMessages(readr::read_tsv(file, n_max=1)))
    schema_fields <- intersect(names(RearrangementSchema), header)
    cast <- setNames(lapply(schema_fields, function(f) parsers[RearrangementSchema[f]$type]), schema_fields)
    types <- do.call(readr::cols, cast)
    
    # Read file    
    data <- suppressMessages(readr::read_tsv(file, col_types=types, na=c("", "NA", "None")))
    
    # Adjust indexes
    if (base == 0) {
        start_positions <- grep("_start$", names(data), perl=TRUE)
        if (length(start_positions) > 0) {
            data[, start_positions] <- data[, start_positions] - 1
        }
    }

    return(data)
}


#' Write an AIRR Rearrangement TSV
#' 
#' \code{write_airr} writes an TSV container AIRR Rearrangement records.
#'
#' @param    data    data.frame of Rearrangement data.
#' @param    file    output file name.
#' @param    base    starting index for positional fields in the output file. 
#'                   If \code{0}, then fields ending in \code{_start} and \code{_end}
#'                   will be converted to 0-based half-open intervals (python style) 
#'                   in the output file. If \code{1}, then these fields will not be 
#'                   modified. Fields in the input \code{data} are assumed to be 
#'                   1-based closed-intervals (R style). 
#'
#' @return   NULL
#' 
#' @seealso  See \link{read_airr} for reading to AIRR Rearrangement files.
#' 
#' @examples
#' \dontrun{
#'   # Write data
#'   write_airr(data, "file.tsv")
#' }
#' 
#' @export
write_airr <- function(data, file, base=0) {
    ## DEBUG
    # data <- data.frame("sequence_id"=1:4, "extra"=1:4, "a"=LETTERS[1:4])

    # Check arguments
    base_choices <- c(0,1)
    base <- match.arg(as.character(base), as.character(base_choices))
    
    # Fill in missing required columns
    missing <- setdiff(RearrangementSchema@required, names(data))
    data[, missing] <- NA
    
    # order columns
    ordering <- c(intersect(names(RearrangementSchema), names(data)),
                  setdiff(names(data), names(RearrangementSchema)))
    data <- data[, ordering]
    
    # Adjust indexes
    if (base == 0) {
        start_positions <- grep("_start$", names(data), perl=TRUE)
        if (length(start_positions) > 0) {
            data[, start_positions] <- data[, start_positions] + 1
        }
    }
    
    # Write
    write_tsv(data, file, na="")
}
