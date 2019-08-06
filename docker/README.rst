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

    docker pull airrc/airr-standards:latest

Singularity
===========

to be written

