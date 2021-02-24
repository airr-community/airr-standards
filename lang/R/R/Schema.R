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



# Function to extract entries from individual fields

extract_field_content <- function(properties, field) {
    
    types <- c("string"="character", "boolean"="logical", "integer"="integer", "number"="double", "array"="array", "object"="object")
    
    # if there is a simple reference to another AIRR schema elements, call the reference entries
    # example: disease_diagnosis entry in Diagnosis schema 
    if(!is.null(properties[[field]]$`$ref`)) {
        # name of the AIRR scheme element to refer to
        ref_element <- properties[[field]]$`$ref`
        # remove #/
        ref_element <- substr(ref_element, 3, nchar(ref_element))
        ref_schema <- load_schema(ref_element)
        # overwrite the property of the field with the Schema it is referencing to
        properties[[field]][["ref"]] <- ref_schema
    }
    
    # if there is an array type format that has ref as entries
    # example: diagnosis entry in Subject schema
    items <- unlist(properties[[field]][["items"]])
    if(!is.null(items)) {
        # check if these are references to other schemes
        if(all(grepl("ref", names(items)))) {
            ref_schemes <- items
            ref_element <- substr(ref_schemes, 3, nchar(ref_schemes))
            # store as a list of schemes
            ref_scheme_list <- sapply(ref_element, load_schema)
            properties[[field]][["ref"]] <- ref_scheme_list
        }
    }
    
    # if there is an object type, the properties may cover several reference schemes 
    # example: germline entry in Subject schema
    if(!is.null(properties[[field]][["type"]]) && 
       properties[[field]][["type"]] == "object") {
        # this should be normally defined in airr-schema.yaml as a reference scheme with optional properties
        # as a workaround we create a helper Schema without required entries
        required_helper <- character(0)
        info_helper <- list(0)
        optional_helper <- names(properties[[field]][["properties"]])
        properties_helper <- properties[[field]][["properties"]]
        
        for (f in optional_helper) {
            # if there is a reference to another AIRR schema elements, call the reference entries
            properties_helper <- extract_field_content(properties_helper, f)
        }
        
        helper_schema <- new("Schema", 
                   required=required_helper, 
                   optional=optional_helper, 
                   properties=properties_helper, 
                   info=info_helper)

        properties[[field]][["ref"]] <- helper_schema
    }
    
    x <- properties[[field]][["type"]]
    y <- properties[[field]][["description"]]
    
    # make sure that NULL types also remain NULL
    if (!is.null(x)) {properties[[field]][["type"]] <- unname(types[x])}
    properties[[field]][["description"]] <- stri_trim(y) 
    
    return(properties)
}


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
#' # Load the Repertoire definition
#' schema <- load_schema("Repertoire")
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
    
    for (f in fields) {
        # if there is a reference to another AIRR schema elements, call the reference entries
        properties <- extract_field_content(properties, f)
    }
    
    # for ontology, required in NULL and this is not type character
    # this leads to a problem returning "none" in the validation function.
    # to be taken care of when array type recursion implemented
    if(is.null(required)) {required <- character(0)}
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

#' @details   \code{RepertoireSchema}: AIRR Repertoire \code{Schema}.
#' @rdname    Schema-class
#' @export
RepertoireSchema <- load_schema("Repertoire")
