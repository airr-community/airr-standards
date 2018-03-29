#' airr
#' 
#' AIRR API Package
#' 
#' @name        airr
#' 
#' @importFrom  readr  read_tsv write_tsv cols
#' @importFrom  stats  setNames
NULL


#### Data ####

#' Alignment Schema
#'
#' AIRR Alignment object schema
#'
#' @format   A list with the following items:
#'   \itemize{
#'     \item  \code{required}:    A vector of mandatory fields.
#'     \item  \code{properties}:  Definitions for each field.
#'     \item  \code{optional}:    A vector of non-required fields.
#' }
#' 
#' @seealso \link{read_airr} and \link{write_airr}.
"AlignmentSchema"

#' Rearrangment Schema
#'
#' AIRR Rearrangement object schema
#'
#' @format   A list with the following items:
#'   \itemize{
#'     \item  \code{required}:    A vector of mandatory fields.
#'     \item  \code{properties}:  Definitions for each field.
#'     \item  \code{optional}:    A vector of non-required fields.
#' }
#' 
#' @seealso \link{read_airr} and \link{write_airr}.
"RearrangementSchema"
