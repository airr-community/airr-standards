FROM ubuntu:18.04

LABEL maintainer="AIRR Community"

# uncomment these if building behind UTSW proxy
ENV http_proxy 'http://proxy.swmed.edu:3128/'
ENV https_proxy 'http://proxy.swmed.edu:3128/'
ENV HTTP_PROXY 'http://proxy.swmed.edu:3128/'
ENV HTTPS_PROXY 'http://proxy.swmed.edu:3128/'

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y --fix-missing \
    git \
    python3 \
    python3-pip \
    python3-sphinx \
    python3-scipy \
    libyaml-dev \
    r-base \
    r-base-dev \
    wget

RUN pip3 install \
    pandas \
    biopython


# Copy source
RUN mkdir /airr-standards
COPY . /airr-standards

# Install python package
RUN cd /airr-standards/lang/python && python3 setup.py install

# Install R package
