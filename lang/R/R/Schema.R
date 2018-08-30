#### Classes ####

#' S4 class defining an AIRR standard schema
#' 
#' \code{Schema} defines a common data structure for AIRR Data Representation 
#' standards.
#' 
#' @slot    required    \code{character} vector of required fields.
#' @slot    optional    \code{character} vector of non-required fields.
#' @slot    properties  \code{list} of field definitions.
#' @slot    info        \code{list} schema information.
#'                  
#' @details
#' The following predefined Schema objects are defined:
#'
#' @format
#' A \code{Schema} object.
#' 
#' @seealso
#' See \link{load_schema} for loading a \code{Schema} from the definition set.
#' See \link{read_airr}, \link{write_airr} and \link{validate_airr} schema operators.
#'
#' @name         Schema-class
#' @rdname       Schema-class
#' @aliases      Schema
#' @exportClass  Schema
setClass("Schema", 
         slots=c(required="character",
                 optional="character",
                 properties="list",
                 info="list"))


#### Methods #####

#' @param    x    \code{Schema} object.
#' 
#' @rdname   Schema-class
#' @aliases  Schema-method
#' @export
setMethod("names",
          signature(x="Schema"),
          function (x) { names(x@properties) })

#' @param    i    field name.
#' 
#' @rdname   Schema-class
#' @aliases  Schema-method
#' @export
setMethod("[",
          signature(x="Schema", i="character"),
          function (x, i) { x@properties[[i]] })

#' @param    name  field name.
#' 
#' @rdname   Schema-class
#' @aliases  Schema-method
#' @export
setMethod("$",
          signature(x="Schema"),
          function (x, name) { x@properties[[name]] })


#### Schema I/O ####

#' Load a schema definition
#' 
#' \code{load_schema} loads an AIRR object definition from the internal
#' definition set.
#'
#' @param    definition   name of the schema definition.
#' 
#' @return   A \link{Schema} object for the \code{definition}.
#' 
#' @details
#' Valid definitions include:
#' \itemize{
#'   \item   \code{"Rearrangement"}
#'   \item   \code{"Alignment"}
#'   \item   \code{"Study"}
#'   \item   \code{"Subject"}
#'   \item   \code{"Diagnosis"}
#'   \item   \code{"Sample"}
#'   \item   \code{"CellProcessing"}
#'   \item   \code{"NucleicAcidProcessing"}
#'   \item   \code{"RawSequenceData"}
#'   \item   \code{"SoftwareProcessing"}
#' }
#'    
#' @seealso  See \link{Schema} for the return object.
#' 
#' @examples
#' # Load the Rearrangement definition
#' schema <- load_schema("Rearrangement")
#' 
#' # Load the Alignment definition
#' schema <- load_schema("Alignment")
#' 
#' @export
load_schema <- function(definition) {
    # Load schema from yaml file
    spec_file <- system.file("extdata", "airr-schema.yaml", package="airr")
    spec_list <- yaml.load_file(spec_file)
    
    # Load definition
    definition_list <- spec_list[[definition]]
    definition_list[["discriminator"]] <- definition_list[["type"]] <- NULL

    # schema info
    info <- spec_list[["Info"]]

    # Define member attributes
    fields <- names(definition_list[["properties"]])
    properties <- definition_list[["properties"]]

    required <- definition_list[["required"]]
    optional <- setdiff(fields, required)
    
    # Rename type and clean description
    types <- c("string"="character", "boolean"="logical", "integer"="integer", "number"="double")
    for (f in fields) {
        x <- properties[[f]][["type"]]
        y <- properties[[f]][["description"]]
        properties[[f]][["type"]] <- unname(types[x])
        properties[[f]][["description"]] <- stri_trim(y)
    }
    
    return(new("Schema", required=required, optional=optional, properties=properties, info=info))
}


#### Data ####

#' Example AIRR data
#'
#' Example data files compliant with the the AIRR Data Representation standards.
#'
#' @format
#' \code{extdata/rearrangement-example.tsv.gz}: Rearrangement TSV file.
#' 
#' @examples
#' # Get path to the rearrangement-example file
#' file <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
#' 
#' # Load data file
#' df <- read_rearrangement(file)
#' 
#' @name ExampleData
NULL

#' @details   \code{AlignmentSchema}: AIRR Alignment \code{Schema}.
#' @rdname    Schema-class
#' @export
AlignmentSchema <- load_schema("Alignment")

#' @details   \code{RearrangementSchema}: AIRR Rearrangement \code{Schema}.
#' @rdname    Schema-class
#' @export
RearrangementSchema <- load_schema("Rearrangement")
