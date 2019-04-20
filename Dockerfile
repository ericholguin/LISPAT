# Dockerfile for running lost in space and time

# pull base image
FROM python:3.6

#Set the working directory to LISPAT.
WORKDIR /LISPAT

# Copy the current directory contents into the container at /LISPAT
# COPY . /LISPAT

# Install.
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends git \
  python3 \
  python3-pip \
  python3-all-dev \
  gcc \
  python-dev \
  curl \
  libpng-dev \
  musl-dev \
  build-essential && \
  rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash
RUN apt-get install -y nodejs

#Update pip
RUN \
  pip3 install --upgrade pip

ADD . lispat

# Set our spacy as a env variable
ENV SPACY_VERSION 2.0.3

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash
RUN apt-get install -y nodejs

RUN cd lispat/lispat_app/static && npm install && npm rebuild node-sass --force && npm run build

#Update the Image to include some program dependencies that are required for each other.
RUN \
  pip3 install -U numpy\
  pandas\
  requests\
  chardet\
  cffi\
  && pip3 install -U spacy==${SPACY_VERSION}\
  && python3 -m spacy download en_core_web_sm

ADD . LISPAT

RUN pip3 install -r lispat/requirements.txt

WORKDIR /lispat

CMD python3 app.py
