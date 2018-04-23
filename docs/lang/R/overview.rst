.. _ROverview:

R Library
================================================================================

An R library providing AIRR schema definitions and read, write, and validation
functions for AIRR standard formatted data files.

**Download & Installation**

To build from the [source code](https://github.com/airr-community/airr-standards),
first install the build dependencies::

    install.packages(c("devtools", "roxygen2"))

To install the latest development code via devtools::

    library(devtools)
    install_github("airr-community/airr-standards/lang/R@master")

Note, using ``install_github`` will not build the documentation. To generate the
documentation, clone the repository and build as normal. Then run the following
R commands from the package root ``lang/R``::

    library(devtools)
    install_deps(dependencies=T)
    document()
    install()

.. toctree::
    :maxdepth: 3
    :hidden:

    About <about>
    vignettes/Usage-Vignette
    Reference Topics <topics>
    Release Notes <news>
