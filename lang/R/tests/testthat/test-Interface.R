# Toy file pointer
rearrangement_file <- file.path("..", "data-tests", "toy_data.tsv")
#rearrangement_file <- file.path("tests", "data-tests", "toy_data.tsv")

# Toy file pointer
bad_rearrangement_file <- file.path("..", "data-tests", "bad_data.tsv")
#bad_rearrangement_file <- file.path("tests", "data-tests", "bad_data.tsv")

# Expected warnings for bad_rearrangement_file
expected_w <- c(
    "Warning: File is missing AIRR mandatory field(s): sequence",
    "Warning: sequence_id(s) are not unique: IVKNQEJ01AJ44V, IVKNQEJ01AJ44V",
    "Warning: sequence_id is empty for row(s): 7",
    "Warning: rev_comp is not logical for row(s): 4",
    "Warning: productive is not logical for row(s): 1"
)

#### Rearrangement I/O  ####

context("Rearrangement I/O - good data")

test_that("read_airr loads a data.frame", {
    tbl_1 <- read_airr(rearrangement_file, "1")
    expect_true(is.data.frame(tbl_1))
})

test_that("read_arirr applies base", {
    tbl_0 <- read_airr(rearrangement_file, "0")
    tbl_1 <- read_airr(rearrangement_file, "1")
    expect_true(is.data.frame(tbl_0))
    expect_true(validate_airr(tbl_0))
    start_positions <- grep("_start$", names(tbl_0), perl=TRUE)
    expect_equivalent(tbl_0[, start_positions] - 1, tbl_1[, start_positions])
})

test_that("Columns are of expected type", {
    # Create test data
    tmp_file <- tempfile(fileext = ".tsv")

    tbl_0 <- read_airr(rearrangement_file, "1")

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
    write_tsv(tbl_0, tmp_file)

    # Read with col_character() as default
    expect_is(tbl_0 <- read_airr(tmp_file, "1"), "data.frame")
    expect_is(tbl_0$extra.int, "character")
    expect_is(tbl_0$extra.numeric, "character")
    expect_is(tbl_0$extra.character, "character")

    expect_is(read_airr(
        rearrangement_file, "1",
        aux_types =
            c(extra.int = "integer",
              extra.double = "double",
              extra.numeric = "numeric",
              extra.character = "character")), "data.frame")

    expect_is(tbl_0 <- read_airr(
        tmp_file, "1",
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


test_that("write_airr writes a file with logicals encoded T/F", {
    tbl <- read_airr(rearrangement_file)
    out_file <- file.path(tempdir(), "test_out.tsv")
    write_airr(tbl, out_file)
    expect_true(file.exists(out_file))
    reload_tbl <- read.delim(out_file, colClasses="character")
    expect_true(all(reload_tbl[['rev_comp']] == "T"))
    expect_equal(reload_tbl[['productive']],
                 c("T","T","F","T","T","F","F","F","T"))
})

context("Rearrangement I/O - bad data")

test_that("read_airr with bad data", {
    # Expect valid==FALSE
    bad_data <- suppressWarnings(read_airr(bad_rearrangement_file, "1"))
    expect_false(suppressWarnings(validate_airr(bad_data)))
    # Check error messages
    w <- capture_warnings(validate_airr(bad_data))
    expect_equal(w, expected_w)
})

test_that("write_airr writes a bad file, with warnings, with logicals T/T", {
    bad_data <- suppressWarnings(read_airr(bad_rearrangement_file, "1"))
    out_file <- file.path(tempdir(), "test_out.tsv")
    expect_warning(write_airr(bad_data, out_file))
    expect_true(file.exists(out_file))
    reload_tbl <- read.delim(out_file, colClasses="character")
    expect_equal(reload_tbl[['rev_comp']],
                c("T","T","T","","T","T","T","T","T","T","T"))
    expect_equal(reload_tbl[['productive']],
                 c("","T","F","T","T","F","F","F","T","T","T"))
})
