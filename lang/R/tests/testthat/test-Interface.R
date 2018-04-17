# Toy file pointer
rearrangement_file <- file.path("..", "data-tests", "toy_data.tsv")
#rearrangement_file <- file.path("tests", "data-tests", "toy_data.tsv")

#### Rearrangement I/O  ####

test_that("read_airr", {
    tbl_0 <- read_airr(rearrangement_file, "0")
    expect_true(is.data.frame(tbl_0))
    
    tbl_1 <- read_airr(rearrangement_file, "1")
    expect_true(is.data.frame(tbl_1))
    
    start_positions <- grep("_start$", names(tbl_0), perl=TRUE)
    
    expect_equivalent(tbl_0[, start_positions] - 1, tbl_1[, start_positions])
})

test_that("write_airr", {
    tbl <- read_airr(rearrangement_file)
    write_airr(tbl, "test_out.tsv")
    expect_true(file.exists("test_out.tsv"))
})
