#### Data ####

#' Alignment Schema
#'
#' AIRR Alignment object schema
#'
#' @format   A \link{Schema} object.
"AlignmentSchema"

#' Rearrangment Schema
#'
#' AIRR Rearrangement object schema
#'
#' @format   A \link{Schema} object.
#' 
#' @seealso See \link{read_airr} and \link{write_airr} for reading and writing.
"RearrangementSchema"


#### Classes ####

#' S4 class defining an AIRR standard schema
#' 
#' \code{Schema} defines a common data structure for AIRR standards.
#' 
#' @slot    required           \code{character} vector of required fields.
#' @slot    optional            \code{character} vector of non-required fields.
#' @slot    properties          \code{list} of field definitions.
#'                          
#' @seealso      See \link{load_schema} loading a \code{Schema} from definitions file.
#'
#' @name         Schema-class
#' @rdname       Schema-class
#' @aliases      Schema
#' @exportClass  Schema
setClass("Schema", 
         slots=c(required="character",
                 optional="character",
                 properties="list"))


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


#### Schema Functions ####

#' Read an AIRR Rearrangement TSV
#' 
#' \code{read_airr} reads a TSV container AIRR Rearrangement records.
#'
#' @param    file        input file path.
#' @param    positions   if \code{TRUE} modify positional fields to 1-based indexes.
#' 
#' @return   A data.frame of the TSV file with appropriate type and position conversion
#'           for fields defined in the specification.
#'                   
#' @seealso  See \link{write_airr} for writing to AIRR Rearrangement data.
#' 
#' @examples
#' # Load the rearrangement definition
#' schema <- load_schema("Rearrangement")
#' 
#' @export
load_schema <- function(definition) {
   # Load schema from yaml file
   spec_file <- system.file("extdata", "definitions.yaml", package="airr")
   spec_list <- yaml::yaml.load_file(spec_file)
   
   # Load definition
   definition_list <- spec_list[[definition]]
   definition_list[["discriminator"]] <- definition_list[["type"]] <- NULL
   
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
   
   return(new("Schema", required=required, optional=optional, properties=properties))
}