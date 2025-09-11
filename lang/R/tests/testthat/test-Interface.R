#### Setup ####

# Installed package context
parent_path <- ".."

# Local script context
# library(testthat)
# library(airr)
# parent_path <- "tests"

# Rearrangement test files
good_rearrangement_file <- file.path(parent_path, "data-tests", "good_rearrangement.tsv")
bad_rearrangement_file <- file.path(parent_path, "data-tests", "bad_rearrangement.tsv")

# Repertoire test files
good_repertoire_file <- file.path(parent_path, "data-tests", "good_repertoire.yaml")
bad_repertoire_file <- file.path(parent_path, "data-tests", "bad_repertoire.yaml")
warn_repertoire_file <- file.path(parent_path, "data-tests", "warn_repertoire.json")

# Germline test files
good_germline_set_file <- file.path(parent_path, "data-tests", "good_germline_set.json")
bad_germline_set_file <- file.path(parent_path, "data-tests", "bad_germline_set.json")
good_genotype_set_file <- file.path(parent_path, "data-tests", "good_genotype_set.json")
bad_genotype_set_file <- file.path(parent_path, "data-tests", "bad_genotype_set.json")

# Clone test files
good_clone_file <- file.path(parent_path, "data-tests", "good_clone.tsv")
bad_clone_file <- file.path(parent_path, "data-tests", "bad_clone.tsv")

# Combined test files
good_combined_yaml <- file.path(parent_path, "data-tests", "good_combined_airr.yaml")
good_combined_json <- file.path(parent_path, "data-tests", "good_combined_airr.json")
good_combined_names <- c("Repertoire", "GermlineSet", "GenotypeSet")

# Expected warnings for bad_rearrangement_file
# expected_w <- c(
#     "Warning: File is missing AIRR mandatory field(s): sequence",
#     "Warning: sequence_id(s) are not unique: IVKNQEJ01AJ44V, IVKNQEJ01AJ44V",
#     "Warning: sequence_id is empty for row(s): 7",
#     "Warning: productive is not logical for row(s): 1"
# )
expected_w <- c(
    "Warning: File is missing AIRR mandatory field(s): sequence",
    "Warning: sequence_id(s) are not unique: IVKNQEJ01AJ44V, IVKNQEJ01AJ44V",
    "Warning: sequence_id is empty for row(s): 7"
)



#### Rearrangement ####

context("Rearrangement I/O - good data")

test_that("read_rearrangement loads a data.frame", {
    tbl_1 <- read_rearrangement(good_rearrangement_file)
    expect_true(is.data.frame(tbl_1))
})

test_that("read_tabular loads a data.frame", {
    expect_error(read_tabular(good_rearrangement_file))
    tbl_1 <- read_tabular(good_rearrangement_file, schema=RearrangementSchema)
    expect_true(is.data.frame(tbl_1))
})

test_that("read_tabular applies base", {
    tbl_0 <- read_tabular(good_rearrangement_file, base="0", schema=RearrangementSchema)
    tbl_1 <- read_tabular(good_rearrangement_file, base="1", schema=RearrangementSchema)
    expect_true(is.data.frame(tbl_0))
    expect_true(validate_tabular(tbl_0, schema = RearrangementSchema))
    start_positions <- grep("_start$", names(tbl_0), perl=TRUE)
    expect_equivalent(tbl_0[, start_positions] - 1, tbl_1[, start_positions])
})

test_that("read_tabular reads zipped tsv", {
  # Create test data gzip
  tmp_file <- tempfile(fileext = ".tsv.gz")

  x <- readr::read_tsv(good_rearrangement_file)
  readr::write_tsv(x, file=tmp_file)

  tbl_1 <- read_tabular(tmp_file, schema=RearrangementSchema)
  expect_true(is.data.frame(tbl_1))

  # bzip2
  tmp_file <- tempfile(fileext=".tsv.bz2")
  readr::write_tsv(x, file=tmp_file)

  tbl_1 <- read_tabular(tmp_file, schema=RearrangementSchema)
  expect_true(is.data.frame(tbl_1))
})

test_that("Columns are of expected type", {
    # Create test data
    tmp_file <- tempfile(fileext = ".tsv")

    tbl_0 <- read_tabular(good_rearrangement_file, schema=RearrangementSchema)

    # Create non-schema  columns
    extra_cols <- data.frame(
        extra.int = c(1:nrow(tbl_0)),
        extra.numeric = rnorm(nrow(tbl_0)),
        extra.double = rnorm(nrow(tbl_0)),
        extra.character = stringi::stri_rand_strings(nrow(tbl_0), 6)
    )
    extra_cols_na <- data.frame(
        extra.int = NA,
        extra.numeric = NA,
        extra.double = NA,
        extra.character = NA
    )

    # Get the number of replications to create a data.frame with NAs to make
    # guessing of column type fail (all NAs)
    num_rep <- ceiling(1000/nrow(tbl_0)) + 1
    tbl_1 <- do.call(
        "rbind",
        replicate(num_rep,
                  cbind(tbl_0, extra_cols_na),
                  simplify = FALSE))
    # Make all sequence_id unique
    tbl_1$sequence_id <- c(1:nrow(tbl_1))

    tbl_0 <- cbind(tbl_0, extra_cols)
    tbl_0 <- rbind(tbl_1, tbl_0)
    write_tabular(tbl_0, tmp_file, schema=RearrangementSchema)

    # Read with col_character() as default
    expect_is(tbl_0 <- read_tabular(tmp_file, schema=RearrangementSchema), "data.frame")
    expect_is(tbl_0$extra.int, "character")
    expect_is(tbl_0$extra.numeric, "character")
    expect_is(tbl_0$extra.character, "character")

    expect_is(read_tabular(
        good_rearrangement_file, schema=RearrangementSchema,
        aux_types =
            c(extra.int = "integer",
              extra.double = "double",
              extra.numeric = "numeric",
              extra.character = "character")), "data.frame")

    expect_is(tbl_0 <- read_tabular(
        tmp_file, "1", schema = RearrangementSchema,
        aux_types =
            c(extra.int = "integer",
              extra.double = "double",
              extra.numeric = "numeric",
              extra.character = "character")), "data.frame")
    expect_is(tbl_0$extra.int, "integer")
    expect_is(tbl_0$extra.double, "numeric")
    expect_is(tbl_0$extra.numeric, "numeric")
    expect_is(tbl_0$extra.character, "character")
})


test_that("write_tabular writes a file with logicals encoded T/F", {
    tbl <- read_tabular(good_rearrangement_file, schema=RearrangementSchema)
    out_file <- file.path(tempdir(), "test_out.tsv")
    write_tabular(tbl, out_file, schema = RearrangementSchema)
    expect_true(file.exists(out_file))
    reload_tbl <- read.delim(out_file, colClasses="character")
    expect_true(all(reload_tbl[['rev_comp']] == "T"))
    expect_equal(reload_tbl[['productive']],
                 c("T","T","F","T","T","F","F","F","T"))
})

context("Rearrangement I/O - bad data")

test_that("read_tabular with bad data", {
    # Expect valid==FALSE
    bad_data <- suppressWarnings(read_tabular(bad_rearrangement_file, base="1", schema=RearrangementSchema))
    expect_false(suppressWarnings(validate_tabular(bad_data, schema=RearrangementSchema)))
    # Check error messages
    w <- capture_warnings(validate_tabular(bad_data, schema=RearrangementSchema))
    expect_equal(w, expected_w)
})

test_that("write_tabular writes a bad file, with warnings, with logicals T/T", {
    bad_data <- suppressWarnings(read_tabular(bad_rearrangement_file, base="1", schema=RearrangementSchema))
    out_file <- file.path(tempdir(), "test_out.tsv")
    expect_warning(write_tabular(bad_data, out_file, schema = RearrangementSchema))
    expect_true(file.exists(out_file))
    reload_tbl <- read.delim(out_file, colClasses="character")
    expect_equal(reload_tbl[['rev_comp']],
                c("T","T","T","","T","T","T","T","T","T","T"))
    expect_equal(reload_tbl[['productive']],
                 c("","T","F","T","T","F","F","F","T","T","T"))
})

#### Repertoire ####

context("Repertoire I/O - good data")

test_that("read_airr loads a Repertoire", {
    rep_1 <- read_airr(good_repertoire_file)
    expect_true(is.list(rep_1))
})

test_that("read_airr with format=yaml loads a Repertoire", {
    rep_1 <- read_airr(good_repertoire_file, format="yaml")
    expect_true(is.list(rep_1))
})

test_that("write_airr writes a yaml Repertoire", {
    geno <- read_airr(good_repertoire_file, validate=T)
    
    tmp_file <- tempfile(fileext=".yaml")
    write_airr(geno, tmp_file, validate=T, model=F)
    geno_tmp <- read_airr(tmp_file, validate=T, model=F)
    expect_identical(geno, geno_tmp)
})

test_that("write_airr writes a json Repertoire", {
    geno <- read_airr(good_repertoire_file, validate=T)
    
    tmp_file <- tempfile(fileext=".json")
    write_airr(geno, tmp_file, validate=T, model=F)
    geno_tmp <- read_airr(tmp_file, validate=T, model=F)
    expect_identical(geno, geno_tmp)
})

context("Repertoire I/O - bad data")

test_that("validate_airr with bad data returns an error", {
    bad_data <- expect_warning(read_airr(bad_repertoire_file))
    expect_false(suppressWarnings(validate_airr(bad_data)))
})

#### GermlineSet ####

context("GermlineSet I/O - good data")

test_that("read_airr loads a GermlineSet", {
  rep_1 <- read_airr(good_germline_set_file, validate=T)
  expect_true(is.list(rep_1))
})

context("GermlineSet I/O - bad data")

test_that("validate_airr with bad data returns an error", {
  bad_data <- read_airr(bad_germline_set_file, validate=F)
  expect_false(expect_warning(validate_airr(bad_data)))
})

#### GenotypeSet ####

context("GenotypeSet I/O - good data")

test_that("read_airr loads a GenotypeSet", {
  rep_1 <- read_airr(good_genotype_set_file, validate=T)
  expect_true(is.list(rep_1))
})

context("GenotypeSet I/O - bad data")

test_that("validate_airr with bad data returns an error", {
  bad_data <- read_airr(bad_genotype_set_file, validate=F)
  expect_false(expect_warning(validate_airr(bad_data)))
})

#### Clone ####

context("Clone I/O - good data")

test_that("read_clone loads a data.frame", {
    tbl_1 <- read_clone(good_clone_file)
    expect_true(is.data.frame(tbl_1))
})

test_that("read_clone with bad data returns an error", {
    bad_data <- read_airr(bad_clone_file, validate=F)
    expect_warning(read_clone(bad_clone_file))
})


#### Combined Data ####

context("Combined I/O")

test_that("read_airr loads a combined yaml file", {
    repr <- read_airr(good_combined_yaml, validate=T)
    expect_true(is.list(repr))
    expect_equal(names(repr), good_combined_names)
})

test_that("read_airr loads a combined json file", {
    repr <- read_airr(good_combined_json, validate=T)
    expect_true(is.list(repr))
    expect_equal(names(repr), good_combined_names)
})

test_that("read_airr json and yaml load identical objects", {
    repr_yaml <- read_airr(good_combined_yaml, validate=T)
    repr_json <- read_airr(good_combined_json, validate=T)
    expect_identical(repr_yaml, repr_json)
})

test_that("write_airr writes a combined yaml file", {
    repr <- read_airr(good_combined_yaml, validate=T)
    
    tmp_file <- tempfile(fileext=".yaml")
    write_airr(repr, tmp_file, validate=T, model=F)
    repr_tmp <- read_airr(tmp_file, validate=T, model=F)
    expect_identical(repr, repr_tmp)
})

test_that("write_airr writes a combined json file", {
    repr <- read_airr(good_combined_json, validate=T)
    
    tmp_file <- tempfile(fileext=".json")
    write_airr(repr, tmp_file, validate=T, model=F)
    repr_tmp <- read_airr(tmp_file, validate=T, model=F)
    expect_identical(repr, repr_tmp)
})

test_that("write_airr json and yaml writes identical objects", {
    repr <- read_airr(good_combined_yaml, validate=T)
    
    tmp_yaml <- tempfile(fileext=".yaml")
    write_airr(repr, tmp_yaml, validate=T)
    repr_yaml <- read_airr(tmp_yaml, validate=T)
    
    tmp_json <- tempfile(fileext=".json")
    write_airr(repr, tmp_json, validate=T)
    repr_json <- read_airr(tmp_json, validate=T)
    
    expect_identical(repr_yaml, repr_json)
})

#### DataFile ####

context("DataFile")

test_that("read_airr works with DataFile", {
    rep1 <- read_airr(good_combined_yaml, validate=T, model=F)
    rep2 <- read_airr(good_combined_yaml, validate=T, model=T)
    expect_identical(rep1, rep2)
})

test_that("validate_airr works with DataFile", {
    rep <- read_airr(good_combined_yaml, validate=F, model=F)
    rep[["Nonsense"]] <- list(list(id="id", data="data"))
    expect_true(expect_warning(validate_airr(rep, model=T),
                               "Skipping validation of non-DataFile object: Nonsense"))
    expect_false(expect_warning(validate_airr(rep, model=F),
                                "Unrecognized schema: Nonsense"))
})

test_that("write_airr yaml works with DataFile", {
    # Test data
    repr <- read_airr(good_combined_yaml, validate=F, model=F)
    repr_extra <- repr
    repr_extra[["Nonsense"]] <- list(list(id="id", data="data"))

    # Write without DataFile constraint
    tmp_file <- tempfile(fileext=".yaml")
    expect_warning(write_airr(repr_extra, tmp_file, validate=T, model=F),
                   "Unrecognized schema: Nonsense")
    repr_tmp <- expect_warning(read_airr(tmp_file, validate=T, model=T),
                               "Skipping validation of non-DataFile object: Nonsense")
    expect_true("Nonsense" %in% names(repr_tmp))
    expect_identical(repr_extra, repr_tmp)
    
    # Write with DataFile constraint
    expect_warning(write_airr(repr_extra, tmp_file, validate=T, model=T),
                   "Skipping validation of non-DataFile object: Nonsense")
    repr_tmp <- read_airr(tmp_file, validate=T, model=T)
    expect_false("Nonsense" %in% names(repr_tmp))
    expect_identical(repr, repr_tmp)
})

test_that("write_airr json works with DataFile", {
    # Test data
    repr <- read_airr(good_combined_json, validate=F, model=F)
    repr_extra <- repr
    repr_extra[["Nonsense"]] <- list(list(id="id", data="data"))
    
    # Write without DataFile constraint
    tmp_file <- tempfile(fileext=".json")
    expect_warning(write_airr(repr_extra, tmp_file, validate=T, model=F),
                   "Unrecognized schema: Nonsense")
    repr_tmp <- expect_warning(read_airr(tmp_file, validate=T, model=T),
                               "Skipping validation of non-DataFile object: Nonsense")
    expect_true("Nonsense" %in% names(repr_tmp))
    expect_identical(repr_extra, repr_tmp)
    
    # Write with DataFile constraint
    expect_warning(write_airr(repr_extra, tmp_file, validate=T, model=T),
                   "Skipping validation of non-DataFile object: Nonsense")
    repr_tmp <- read_airr(tmp_file, validate=T, model=T)
    expect_false("Nonsense" %in% names(repr_tmp))
    expect_identical(repr, repr_tmp)
})
