FROM ubuntu:20.04

LABEL maintainer="AIRR Community"

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y --fix-missing \
    git \
    python3 \
    python3-pip \
    python3-sphinx \
    python3-scipy \
    libyaml-dev \
    r-base \
    r-base-dev \
    wget \
    curl \
    libxml2-dev \
    libcurl4-openssl-dev \
    libfontconfig1-dev \
    libssl-dev \
    libharfbuzz-dev libfribidi-dev \
    libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev

RUN pip3 install \
    pandas \
    biopython \
    recommonmark \
    sphinxcontrib-autoprogram \
    sphinx_bootstrap_theme \
    sphinx_book_theme \
    matplotlib \
    jsondiff

# Install R devtools
RUN R -e 'install.packages(c("devtools","knitr","rmarkdown","testthat","readr"),dependencies=T)'

# Copy source
RUN mkdir /airr-standards
COPY . /airr-standards

# Install python package
RUN cd /airr-standards/lang/python && python3 setup.py install

# Generate the documentation
RUN cd /airr-standards && sphinx-build -a -E -b html docs docs/_build/html
