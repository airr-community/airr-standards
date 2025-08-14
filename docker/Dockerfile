FROM ubuntu:24.04

LABEL maintainer="AIRR Community"

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y --fix-missing \
    git \
    python3 \
    python3-pip \
    python3-sphinx \
    python3-scipy \
    python3-venv \
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
    libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev \
    nano

# Create a virtual environment
RUN python3 -m venv /airr-venv

# Activate the virtual environment
ENV PATH="/airr-venv/bin:$PATH"

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

# node
ENV NODE_VER=v14.21.3
RUN wget https://nodejs.org/dist/$NODE_VER/node-$NODE_VER-linux-x64.tar.xz
RUN tar xf node-$NODE_VER-linux-x64.tar.xz
RUN cp -rf /node-$NODE_VER-linux-x64/bin/* /usr/bin
RUN cp -rf /node-$NODE_VER-linux-x64/lib/* /usr/lib
RUN cp -rf /node-$NODE_VER-linux-x64/include/* /usr/include
RUN cp -rf /node-$NODE_VER-linux-x64/share/* /usr/share

# Copy source
RUN mkdir /airr-standards
COPY . /airr-standards

# Install python package
RUN cd /airr-standards/lang/python && pip3 install .

# nodejs package
RUN cd /airr-standards/lang/js && npm install
RUN cd /airr-standards/lang/js && npm run eslint
#RUN cd /airr-standards/lang/js && npm run test

# Generate the documentation
RUN cd /airr-standards && pip3 install -r docs/requirements.txt
RUN cd /airr-standards && sphinx-build -a -E -b html docs docs/_build/html
