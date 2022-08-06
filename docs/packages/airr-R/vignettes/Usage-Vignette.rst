Usage Vignette
==============

Introduction
------------

Since the use of High-throughput sequencing (HTS) was first introduced
to analyze immunoglobulin (B-cell receptor, antibody) and T-cell
receptor repertoires (Freeman et al, 2009; Robins et al, 2009; Weinstein
et al, 2009), the increasing number of studies making use of this
technique has produced enormous amounts of data and there exists a
pressing need to develop and adopt common standards, protocols, and
policies for generating and sharing data sets. The `Adaptive Immune
Receptor Repertoire (AIRR) Community <http://airr-community.org>`__
formed in 2015 to address this challenge (Breden et al, 2017) and has
stablished the set of minimal metadata elements (MiAIRR) required for
describing published AIRR datasets (Rubelt et al, 2017) as well as file
formats to represent this data in a machine-readable form. The ``airr``
R package provide read, write and validation of data following the AIRR
Data Representation schemas. This vignette provides a set of simple use
examples.

AIRR Data Standards
~~~~~~~~~~~~~~~~~~~

The AIRR Community’s recommendations for a minimal set of metadata that
should be used to describe an AIRR-seq data set when published or
deposited in a AIRR-compliant public repository are described in Rubelt
et al, 2017. The primary aim of this effort is to make published AIRR
datasets FAIR (findable, accessible, interoperable, reusable); with
sufficient detail such that a person skilled in the art of AIRR
sequencing and data analysis will be able to reproduce the experiment
and data analyses that were performed.

Following this principles, V(D)J reference alignment annotations are
saved in standard tab-delimited files (TSV) with associated metadata
provided in accompanying YAML formatted files. The column names and
field names in these files have been defined by the AIRR Data
Representation Working Group using a controlled vocabulary of
standardized terms and types to refer to each piece of information.

Reading AIRR formatted files
----------------------------

The ``airr`` package contains the function ``read_rearrangement`` to
read and validate files containing AIRR Rearrangement records, where a
Rearrangement record describes the collection of optimal annotations on
a single sequence that has undergone V(D)J reference alignment. The
usage is straightforward, as the file format is a typical tabulated
file. The argument that needs attention is ``base``, with possible
values ``"0"`` and ``"1"``. ``base`` denotes the starting index for
positional fields in the input file. Positional fields are those that
contain alignment coordinates and names ending in "_start" and "_end".
If the input file is using 1-based closed intervals (R style), as
defined by the standard, then positional fields will not be modified
under the default setting of ``base="1"``. If the input file is using
0-based coordinates with half-open intervals (python style), then
positional fields may be converted to 1-based closed intervals using the
argument ``base="0"``.

Reading Rearrangements
~~~~~~~~~~~~~~~~~~~~~~

.. code:: r

   # Imports
   library(airr)
   library(tibble)

   # Read Rearrangement example file
   f1 <- system.file("extdata", "rearrangement-example.tsv.gz", package="airr")
   rearrangement <- read_rearrangement(f1)
   glimpse(rearrangement)

::

   ## Rows: 101
   ## Columns: 33
   ## $ sequence_id        <chr> "SRR765688.7787", "SRR765688.35420", "SRR765688.36681", "SRR765688.33811", "SRR765688.44149", "SRR765688.15636", "SRR765688.20304", "SRR765688.13860", "SRR7656…
   ## $ sequence           <chr> "NNNNNNNNNNNNNNNNNNNNGCTGACCTGCACCTTCTCTGGATTCTCACTCAGTACTAGTGCAGTGGGTGTACACTGGATCCGTCAGCCCCCAGGAAAGGCCCTGGAGTGGCTTGCACTCATTTATTGGGATGATGCCAAATATTACAGCACCAGCCC…
   ## $ rev_comp           <lgl> FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE…
   ## $ productive         <lgl> TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE…
   ## $ vj_in_frame        <lgl> TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, T…
   ## $ stop_codon         <lgl> FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, TRUE, FALSE, FALSE, FALSE, FALSE, FAL…
   ## $ v_call             <chr> "IGHV2-5*02", "IGHV5-51*01", "IGHV7-4-1*02", "IGHV7-4-1*02", "IGHV7-4-1*02", "IGHV2-5*02", "IGHV7-4-1*02", "IGHV6-1*01,IGHV6-1*02", "IGHV7-4-1*02", "IGHV4-39*0…
   ## $ d_call             <chr> "IGHD5-24*01", "IGHD3-16*02,IGHD3-3*01,IGHD3-3*02", "IGHD3-22*01", "IGHD3-9*01", "IGHD1-26*01", "IGHD2-21*02", "IGHD1-26*01,IGHD2-21*02,IGHD3/OR15-3a*01", "IGH…
   ## $ j_call             <chr> "IGHJ4*02", "IGHJ6*02,IGHJ6*04", "IGHJ4*02", "IGHJ6*02", "IGHJ6*01", "IGHJ4*02", "IGHJ5*02", "IGHJ4*02", "IGHJ4*02", "IGHJ4*02", "IGHJ5*02", "IGHJ6*02", "IGHJ6…
   ## $ c_call             <chr> "IGHG", "IGHG", "IGHG", "IGHG", "IGHG", "IGHA", "IGHA", "IGHG", "IGHG", "IGHA", "IGHA", "IGHG", "IGHA", "IGHA", "IGHG", "IGHA", "IGHG", "IGHA", "IGHG", "IGHG",…
   ## $ sequence_alignment <chr> "...........................................................GCTGACCTGCACCTTCTCTGGATTCTCACTCAGT......ACTAGTGCAGTGGGTGTACACTGGATCCGTCAGCCCCCAGGAAAGGCCCTGGAGTGGCT…
   ## $ germline_alignment <chr> "CAGATCACCTTGAAGGAGTCTGGTCCT...ACGCTGGTGAAACCCACACAGACCCTCACGCTGACCTGCACCTTCTCTGGGTTCTCACTCAGC......ACTAGTGGAGTGGGTGTGGGCTGGATCCGTCAGCCCCCAGGAAAGGCCCTGGAGTGGCT…
   ## $ junction           <chr> "TGTGCACACAGTGCGGGATGGCTGCCTGATTACTGG", "TGTGCGAGGCATGGATTATACGGTTGTGATCATACCGGCTGTTATACAAGCTTCTACTACTACGGGATGGACGTCTGG", "TGTGCGAGAGAAGAACGTCGAAGTAGTGGTTATTTT…
   ## $ junction_aa        <chr> "CAHSAGWLPDYW", "CARHGLYGCDHTGCYTSFYYYGMDVW", "CAREERRSSGYFDHW", "CAREGYYFDTTGSPRSHGLDVW", "CARDSGGMDVW", "CVLSRRLGDSGVQKYYFDYW", "CAREGLWDGRVVTDLW", "CARTRYSS…
   ## $ v_cigar            <chr> "20S56N21=1X11=1X7=1X9=3X62=6D2=1X1=2X2=2X50=1X7=1X4=1X22=1X30=", "20S40N15=1X15=1X11=1X2=1X1=1X1=2X3=1X7=1X41=2X2=1X10=1X3=1X1=1X5=2X5=1X4=1X9=1X19=1X24=2X9=1…
   ## $ d_cigar            <chr> "274S5N7=", "305S29N7=", "293S13N12=", "290S9N8=", "283S4N7=", "273S12N8=", "289S6N6=", "267S9N9=", "281S7N5=", "278S7N5=1X7=", "277S8N7=", "297S9N7=", "265S9N…
   ## $ j_cigar            <chr> "288S11N32=1X4=", "318S7N12=1X15=", "305S5N6=1X14=1X21=", "321S15N5=1X23=1X17=", "290S17N19=", "296S26=1X21=", "311S11N4=1X33=", "280S2N17=1X6=1X21=", "299S8N4…
   ## $ v_sequence_start   <int> 21, 21, 21, 21, 21, 21, 21, 20, 22, 21, 21, 20, 21, 21, 21, 21, 19, 21, 21, 21, 20, 21, 21, 21, 21, 21, 20, 23, 19, 21, 20, 21, 21, 20, 20, 21, 20, 22, 21, 21,…
   ## $ v_sequence_end     <int> 269, 276, 283, 283, 283, 264, 283, 259, 281, 266, 264, 294, 258, 283, 273, 279, 274, 259, 278, 280, 262, 271, 281, 262, 264, 283, 259, 279, 278, 280, 261, 260,…
   ## $ v_germline_start   <int> 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, …
   ## $ v_germline_end     <int> 320, 320, 320, 320, 320, 320, 320, 318, 318, 320, 320, 320, 319, 319, 317, 316, 316, 320, 318, 320, 320, 315, 318, 320, 321, 320, 318, 316, 320, 317, 319, 316,…
   ## $ d_sequence_start   <int> 275, 306, 294, 291, 284, 274, 290, 268, 282, 279, 278, 298, 266, 292, 301, 285, 276, NA, 291, 284, 273, 279, 289, 277, 272, 299, 270, 292, 282, 295, 267, 265, …
   ## $ d_sequence_end     <int> 281, 312, 305, 298, 290, 281, 295, 276, 286, 291, 284, 304, 273, 296, 307, 289, 282, NA, 297, 295, 293, 290, 294, 283, 287, 307, 280, 302, 290, 301, 280, 270, …
   ## $ d_germline_start   <int> 6, 30, 14, 10, 5, 13, 7, 10, 8, 8, 9, 10, 10, 7, 22, 14, 4, NA, 24, 4, 2, 5, 8, 9, 6, 3, 1, 3, 7, 7, 4, 6, 11, 14, 12, 8, 2, 11, 8, 10, 5, 24, 4, 17, 5, 5, 4, …
   ## $ d_germline_end     <int> 12, 36, 25, 17, 11, 20, 12, 18, 12, 20, 15, 16, 17, 11, 28, 18, 10, NA, 30, 15, 22, 16, 13, 15, 21, 11, 11, 13, 15, 13, 17, 11, 17, 18, 19, 13, 8, 16, 20, 16, …
   ## $ j_sequence_start   <int> 289, 319, 306, 322, 291, 297, 312, 281, 300, 301, 289, 319, 276, 300, 317, 299, 296, 271, 336, 321, 303, 304, 300, 297, 293, 322, 289, 311, 315, 320, 283, 293,…
   ## $ j_sequence_end     <int> 325, 346, 348, 368, 309, 344, 349, 326, 339, 347, 335, 361, 326, 334, 350, 333, 346, 320, 370, 338, 332, 338, 339, 333, 340, 368, 332, 345, 342, 362, 327, 327,…
   ## $ j_germline_start   <int> 12, 8, 6, 16, 18, 1, 12, 3, 9, 2, 5, 20, 9, 14, 15, 14, 2, 13, 28, 18, 6, 14, 9, 15, 1, 16, 5, 14, 8, 5, 4, 12, 9, 1, 20, 15, 6, 6, 5, 6, 5, 9, 1, 6, 5, 5, 9, …
   ## $ j_germline_end     <int> 48, 35, 48, 62, 36, 48, 49, 48, 48, 48, 51, 62, 59, 48, 48, 48, 52, 62, 62, 35, 35, 48, 48, 51, 48, 62, 48, 48, 35, 47, 48, 46, 48, 44, 62, 48, 48, 51, 50, 53,…
   ## $ junction_length    <int> 36, 78, 45, 66, 33, 60, 48, 45, 36, 61, 51, 48, 51, 30, 54, 30, 48, 42, 71, 66, 78, 42, 36, 51, 57, 66, 51, 42, 72, 60, 45, 45, 45, 42, 36, 36, 57, 48, 51, 45,…
   ## $ np1_length         <int> 5, 29, 10, 7, 0, 9, 6, 8, 0, 12, 13, 3, 7, 8, 27, 5, 1, 11, 12, 3, 10, 7, 7, 14, 7, 15, 10, 12, 3, 14, 5, 4, 4, 6, 1, 7, 1, 5, 4, 5, 26, 5, 0, 15, 26, 26, 8, 7…
   ## $ np2_length         <int> 7, 6, 0, 23, 0, 15, 16, 4, 13, 9, 4, 14, 2, 3, 9, 9, 13, NA, 38, 25, 9, 13, 5, 13, 5, 14, 8, 8, 24, 18, 2, 22, 15, 3, 3, 11, 29, 11, 9, 5, 1, 5, 8, 0, 1, 1, 11…
   ## $ duplicate_count    <int> 3, 3, 13, 3, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2, 2, 2, 3, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 5, 2, 2, 3, 2, 4, 2, 3, 4, 8, 2, 2, 2, 2, 3, 2, 4, 3, 4, 2, 5, 2, 2, 7, 3, 2,…

Reading AIRR Data Models
~~~~~~~~~~~~~~~~~~~~~~~~

AIRR Data Model records, such as Repertoire and GermlineSet, can be read
from either a YAML or JSON formatted file into a nested list.

.. code:: r

   # Read Repertoire example file
   f2 <- system.file("extdata", "repertoire-example.yaml", package="airr")
   repertoire <- read_airr(f2)
   glimpse(repertoire)

::

   ## List of 1
   ##  $ Repertoire:List of 3
   ##   ..$ :List of 5
   ##   .. ..$ repertoire_id  : chr "1841923116114776551-242ac11c-0001-012"
   ##   .. ..$ study          :List of 13
   ##   .. ..$ subject        :List of 15
   ##   .. ..$ sample         :List of 1
   ##   .. ..$ data_processing:List of 1
   ##   ..$ :List of 5
   ##   .. ..$ repertoire_id  : chr "1602908186092376551-242ac11c-0001-012"
   ##   .. ..$ study          :List of 13
   ##   .. ..$ subject        :List of 15
   ##   .. ..$ sample         :List of 1
   ##   .. ..$ data_processing:List of 1
   ##   ..$ :List of 5
   ##   .. ..$ repertoire_id  : chr "2366080924918616551-242ac11c-0001-012"
   ##   .. ..$ study          :List of 13
   ##   .. ..$ subject        :List of 15
   ##   .. ..$ sample         :List of 1
   ##   .. ..$ data_processing:List of 1

.. code:: r

   # Read GermlineSet example file
   f3 <- system.file("extdata", "germline-example.json", package="airr")
   germline <- read_airr(f3, validate=F)
   glimpse(germline)

::

   ## List of 1
   ##  $ GermlineSet:List of 17
   ##   ..$ germline_set_id      : chr "OGRDB:G00007"
   ##   ..$ author               : chr "William Lees"
   ##   ..$ lab_name             : chr ""
   ##   ..$ lab_address          : chr "Birkbeck College, University of London, Malet Street, London"
   ##   ..$ acknowledgements     : list()
   ##   ..$ release_version      : int 1
   ##   ..$ release_description  : chr ""
   ##   ..$ release_date         : chr "2021-11-24"
   ##   ..$ germline_set_name    : chr "CAST IGH"
   ##   ..$ germline_set_ref     : chr "OGRDB:G00007.1"
   ##   ..$ pub_ids              : chr ""
   ##   ..$ species              : chr "Mouse"
   ##   ..$ species_subgroup     : chr "CAST_EiJ"
   ##   ..$ species_subgroup_type: chr "strain"
   ##   ..$ locus                : chr "IGH"
   ##   ..$ allele_descriptions  :List of 2
   ##   .. ..$ :List of 39
   ##   .. ..$ :List of 39
   ##   ..$ notes                : chr ""

Writing AIRR formatted files
----------------------------

The ``airr`` package contains the function ``write_rearrangement`` to
write Rearrangement records to the AIRR TSV format.

Writing Rearrangements
~~~~~~~~~~~~~~~~~~~~~~

.. code:: r

   x1 <- file.path(tempdir(), "airr_out.tsv")
   write_rearrangement(rearrangement, x1)

Writing AIRR Data Models
~~~~~~~~~~~~~~~~~~~~~~~~

AIRR Data Model records can be written to either YAML or JSON using the
``write_airr`` function.

.. code:: r

   x2 <- file.path(tempdir(), "airr_repertoire_out.yaml")
   write_airr(repertoire, x2, format="yaml")

   x3 <- file.path(tempdir(), "airr_germline_out.json")
   write_airr(germline, x3, format="json", validate=F)

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
