.. _ROverview:

R Library
=================================================================================

``airr`` is an R package for working with data formatted according to
the AIRR Standards schemas. It includes the full set of schema
definitions along with simple functions for read, write and validation.

.. toctree::
    :maxdepth: 1
    :caption: Table of Contents

    Usage Vignette <vignettes/Usage-Vignette>
    Reference Manual <topics>
    Release Notes <news>

Download & Installation
--------------------------------------------------------------------------------

To install the latest release from CRAN::

    install.packages("airr")

To build from the `source code <https://github.com/airr-community/airr-standards>`_,
first install the build dependencies::

    install.packages(c("devtools", "roxygen2"))

To install the latest development code via devtools::

    library(devtools)
    install_github("airr-community/airr-standards/lang/R@master")

Note, using ``install_github`` will not build the documentation. To generate the
documentation, clone the repository, and then build as normal using the following
R commands from the package root ``lang/R``::

    library(devtools)
    install_deps(dependencies=T)
    document()
    install()

.. include:: about.rst
