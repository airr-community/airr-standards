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

# Expected warnings for bad_rearrangement_file
expected_w <- c(
    "Warning: File is missing AIRR mandatory field(s): sequence",
    "Warning: sequence_id(s) are not unique: IVKNQEJ01AJ44V, IVKNQEJ01AJ44V",
    "Warning: sequence_id is empty for row(s): 7",
    "Warning: rev_comp is not logical for row(s): 4",
    "Warning: productive is not logical for row(s): 1"
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

context("Repertoire I/O - bad data")

test_that("validate_airr with bad data returns an error", {
    bad_data <- expect_warning(read_airr(bad_repertoire_file))
    expect_false(suppressWarnings(validate_airr(bad_data)))
})

#### GermlineSet ####

context("GermlineSet I/O - good data")

# TODO: Update good data so validation passes
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

# TODO: Update good data so validation passes
test_that("read_airr loads a GenotypeSet", {
  rep_1 <- read_airr(good_genotype_set_file, validate=T)
  expect_true(is.list(rep_1))
})

context("GenotypeSet I/O - bad data")

test_that("validate_airr with bad data returns an error", {
  bad_data <- read_airr(bad_genotype_set_file, validate=F)
  expect_false(expect_warning(validate_airr(bad_data)))
})