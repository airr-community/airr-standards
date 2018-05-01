Usage Vignette
==============

Introduction
------------

Since the use of High-throughput sequencing (HTS) was first introduced
to analyze immunoglobulin (B-cell receptor, antibody) and T-cell
receptor repertoires (Freeman et al, 2009; Robins et al, 2009; Weinstein
et al, 2009), the increasing number of studies making use of this
technique has produced enormous amounts of data and there’s a pressing
need to develop and adopt common standards, protocols, and policies for
generating and sharing data sets. The Adaptive Immune Receptor
Repertoire (AIRR) Community formed in 2015 to address this challenge
(Breden et al, 2017) and has stablished the set of minimal metadata
elements (MiAIRR) required for describing published AIRR datasets
(Rubelt et al, 2017) as well as file formats to represent the
information in a machine-readable form. The R package ``airr`` allows to
read and write data following the AIRR format standards and this
vignette provides examples on how to use it.

AIRR Community
~~~~~~~~~~~~~~

The motivations and goals of the AIRR Community are described in detail
in (Breden et al, 2017). Membership in the AIRR Community is open and is
intended to cover all aspects of AIRR-seq technology and its uses. The
profile of its members is diverse, and includes researches with
expertise in a broad range of scientific and legal areas involved in the
generation and analysis of immune repertoire data. Through continuous
cycles of dialogue and collaboration, the AIRR community has developed a
set of metadata standards for the publication and sharing of AIRR-seq
datasets (MiAIRR) (Rubelt et al, 2017) and specific machine-readable
file formats to record AIRR-seq data and its annotation, from the
experiment level to the sequence level.

MiAIRR standards
~~~~~~~~~~~~~~~~

The Community’s recommendations for a minimal set of metadata that
should be used to describe an AIRR-seq data set when published or when
deposited in a AIRR-compliant repository are described in Rubelt et al,
2017. The primary aim of this effort is to make published AIRR datasets
FAIR (findable, accessible, interoperable, reusable).The overall goal of
this standard is that sufficient detail be provided such that a person
skilled in the art of AIRR sequencing and data analysis will be able to
reproduce the experiment and data analyses that were performed.

Following this principles, alignments and rearrangement annotations are
saved in standard tab-delimited format files (TSV) and the metadata for
each of these files is provided in an additional YAML formatted file.
The column names and field names in these files have been defined by the
AIRR community. The use of standardized terms to refer to each piece of
information and the use of a defined data representation format means
that MiAIRR compliant software, API and databases can communicate and
exchange information.

Reading AIRR formatted files
----------------------------

The ``airr`` package contains the function ``read_rearrangement`` to
read and validate rearrangement files following the AIRR standards. The
usage is straightforward, as the file format is a typical tabulated
file. The argument that needs attention is ``base``, with possible
values ``"0"`` and ``"1"``. ``base`` denotes the starting index for
positional fields in the input file. Positional fields are those that
contain alignment coordinates and names ending in “_start" and “_end“.
If the input file is using 0-based coordinates (as in python style
0-based half-open intervals), then positional fields will be converted
to 1-based closed intervals (R style). If ``"1"``, positional fields
will not be modified.

.. code:: r

    library(airr)

    example_data <- file.path("..", "tests", "data-tests", "toy_data.tsv")
    basename(example_data)

::

    ## [1] "toy_data.tsv"

.. code:: r

    airr_rearrangement <- read_rearrangement(example_data, base="0")
    class(airr_rearrangement)

::

    ## [1] "tbl_df"     "tbl"        "data.frame"

.. code:: r

    head(airr_rearrangement)

::

    ## # A tibble: 6 x 44
    ##   rearrangement_id rearrangement_se… sequence_id sequence         rev_comp
    ##   <chr>            <chr>             <chr>       <chr>            <lgl>   
    ## 1 IVKNQEJ01BVGQ6   1                 IVKNQEJ01B… GGCCCAGGACTGGTG… TRUE    
    ## 2 IVKNQEJ01AQVWS   1                 IVKNQEJ01A… GGCCCAGGACTGGTG… TRUE    
    ## 3 IVKNQEJ01AOYFZ   1                 IVKNQEJ01A… GGCCCAGGACTGGTG… TRUE    
    ## 4 IVKNQEJ01EI5S4   1                 IVKNQEJ01E… GGCCCAGGACTGGTG… TRUE    
    ## 5 IVKNQEJ01DGRRI   1                 IVKNQEJ01D… GGCCCAGGACTGGTG… TRUE    
    ## 6 IVKNQEJ01APN5N   1                 IVKNQEJ01A… GGCCCAGGACTGGTG… TRUE    
    ## # ... with 39 more variables: productive <lgl>, sequence_alignment <chr>,
    ## #   germline_alignment <chr>, v_call <chr>, d_call <chr>, j_call <chr>,
    ## #   c_call <chr>, junction <chr>, junction_length <int>,
    ## #   junction_aa <chr>, v_score <dbl>, d_score <dbl>, j_score <dbl>,
    ## #   c_score <dbl>, v_cigar <chr>, d_cigar <chr>, j_cigar <chr>,
    ## #   c_cigar <chr>, v_identity <dbl>, v_evalue <dbl>, d_identity <dbl>,
    ## #   d_evalue <dbl>, j_identity <dbl>, j_evalue <dbl>,
    ## #   v_sequence_start <dbl>, v_sequence_end <int>, v_germline_start <dbl>,
    ## #   v_germline_end <int>, d_sequence_start <dbl>, d_sequence_end <int>,
    ## #   d_germline_start <dbl>, d_germline_end <int>, j_sequence_start <dbl>,
    ## #   j_sequence_end <int>, j_germline_start <dbl>, j_germline_end <int>,
    ## #   np1_length <int>, np2_length <int>, duplicate_count <int>

Writing AIRR formatted files
----------------------------

The ``airr`` package contains the function ``write_rearrangement`` to
write rearrangement files in AIRR format.

.. code:: r

    out_file <- file.path(tempdir(), "airr_out.tsv")
    write_rearrangement(airr_rearrangement, out_file, base="0")

References
----------

1. Breden, F., E. T. Luning Prak, B. Peters, F. Rubelt, C. A. Schramm,
   C. E. Busse, J. A. Vander Heiden, et al. 2017. Reproducibility and
   Reuse of Adaptive Immune Receptor Repertoire Data. *Front Immunol* 8:
   1418.
2. Freeman, J. D., R. L. Warren, J. R. Webb, B. H. Nelson, and R. A.
   Holt. 2009. Profiling the T-cell receptor beta-chain repertoire by
   massively parallel sequencing. *Genome Res* 19 (10): 1817-24.
3. Robins, H. S., P. V. Campregher, S. K. Srivastava, A. Wacher, C. J.
   Turtle, O. Kahsai, S. R. Riddell, E. H. Warren, and C. S. Carlson.
   2009. Comprehensive assessment of T-cell receptor beta-chain
   diversity in alphabeta T cells. *Blood* 114 (19): 4099-4107.
4. Rubelt, F., C. E. Busse, S. A. C. Bukhari, J. P. Burckert, E.
   Mariotti-Ferrandiz, L. G. Cowell, C. T. Watson, et al. 2017. Adaptive
   Immune Receptor Repertoire Community recommendations for sharing
   immune-repertoire sequencing data. *Nat Immunol* 18 (12): 1274-8.
5. Weinstein, J. A., N. Jiang, R. A. White, D. S. Fisher, and S. R.
   Quake. 2009. High-throughput sequencing of the zebrafish antibody
   repertoire. *Science* 324 (5928): 807-10.
