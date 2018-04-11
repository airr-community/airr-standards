# Toy file pointer
rearrangement_file <- file.path("..", "data-tests", "toy_data.tsv")
#rearrangement_file <- file.path("tests", "data-tests", "toy_data.tsv")

#### Rearrangement I/O  ####

test_that("read_airr", {
    tbl <- read_airr(rearrangement_file)
    expect_true(is.data.frame(tbl))
})

# test_that("write_airr", {
#     tbl <- read_airr(rearrangement_file)
#     write_airr(tbl, "test_out.tsv")
# })
