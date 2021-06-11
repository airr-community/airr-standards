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
    curl

RUN pip3 install \
    pandas \
    biopython \
    recommonmark \
    sphinxcontrib-autoprogram \
    sphinx_bootstrap_theme \
    sphinx_book_theme \
    matplotlib

# Copy source
RUN mkdir /airr-standards
COPY . /airr-standards

# Install python package
RUN cd /airr-standards/lang/python && python3 setup.py install

# Install R package

# Generate the documentation
RUN cd /airr-standards && sphinx-build -a -E -b html docs docs/_build/html
