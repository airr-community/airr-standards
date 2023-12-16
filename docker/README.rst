=======================================
AIRR Standards Docker/Singularity Image
=======================================

The AIRR Standards docker image provided by the AIRR Community is a
convenience tool for working with the python/R reference libraries,
working with the documentation, and providing a consistent environment
for the tutorials and example code. In general, if you are building a
docker image for your tool, you should install the reference libraries
using the standard mechanism, PyPI for python and CRAN for R, instead
of basing your image upon the AIRR Standards image.

A separate set of docker images are defined for the `ADC API`_ reference
implementation.

.. _`ADC API`: https://github.com/airr-community/adc-api

Download
========

::
    # this may be out of date, sorry, no automated builds

    docker pull airrc/airr-standards:latest

    # the recent version

    docker pull airrc/airr-standards:v1.4.0

    # interactive bash shell in airr container with current directory mapped to /work

    docker run -v $PWD:/work -it airrc/airr-standards bash

Build from Source
=================

More detailed instructions exist in the `Development Setup`_ of CONTRIBUTING.

::
    # get the source code

    git clone https://github.com/airr-community/airr-standards.git

    # build

    cd airr-standards

    docker build -f docker/Dockerfile -t airrc/airr-standards:latest .

.. _`Development Setup`: https://github.com/airr-community/airr-standards/blob/master/CONTRIBUTING.rst#development-setup

Singularity
===========

to be written

