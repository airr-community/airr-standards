# Toy file pointer
rearrangement_file <- file.path("..", "data-tests", "toy_data.tsv")
#rearrangement_file <- file.path("tests", "data-tests", "toy_data.tsv")

# Toy file pointer
bad_rearrangement_file <- file.path("..", "data-tests", "bad_data.tsv")
#bad_rearrangement_file <- file.path("tests", "data-tests", "bad_data.tsv")


#### Rearrangement I/O  ####

context("Rearrangement I/O - good data")

test_that("read_airr loads a data.frame", {
    tbl_0 <- read_airr(rearrangement_file, "0")
    expect_true(is.data.frame(tbl_0))
})

test_that("read_arirr applies base", {
    tbl_0 <- read_airr(rearrangement_file, "0")
    tbl_1 <- read_airr(rearrangement_file, "1")
    expect_true(is.data.frame(tbl_1))
    expect_true(validate_airr(tbl_0))
    start_positions <- grep("_start$", names(tbl_0), perl=TRUE)
    expect_equivalent(tbl_0[, start_positions] - 1, tbl_1[, start_positions])
})


test_that("write_airr writes a file", {
    tbl <- read_airr(rearrangement_file)
    out_file <- file.path(tempdir(), "test_out.tsv")
    write_airr(tbl, out_file)
    expect_true(file.exists(out_file))
})

context("Rearrangement I/O - bad data")

test_that("read_airr with bad data", {
    # Expect valid==FALSE
    bad_data <- suppressWarnings(read_airr(bad_rearrangement_file, "0"))
    expect_false(suppressWarnings(validate_airr(bad_data)))
    # Check error messages
    w <- capture_warnings(validate_airr(bad_data))
    expected_w <- c(
        "Warning: File is missing AIRR mandatory field(s): sequence",            
        "Warning: sequence_id(s) are not unique: IVKNQEJ01AJ44V, IVKNQEJ01AJ44V",
        "Warning: sequence_id is empty for row(s): 7",
        "Warning:  rev_comp  is not logical for row(s): 4",
        "Warning:  productive  is not logical for row(s): 1"
    )
    expect_equal(w, expected_w)
})

