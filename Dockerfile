# Dockerfile for running lost in space and time

# pull base image
FROM ubuntu:18.04
FROM python:3.6

#Set the working directory to LISPAT.
WORKDIR /LISPAT

# Copy the current directory contents into the container at /LISPAT
COPY . /LISPAT

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


#Set our spacy as a env variable
ENV SPACY_VERSION 2.0.3

#Update the Image to include some program dependencies that are required for each other.
RUN \
  pip3 install -U numpy\
  pandas\
  requests\
  chardet\
  cffi\
  && pip3 install -U spacy==${SPACY_VERSION}\
  && python3 -m spacy download en_core_web_sm


RUN pip3 install -r requirements.txt

ADD . LISPAT/lispat_app/static

RUN cd lispat_app/static/
RUN npm install
RUN npm run build

#Give the starting argument as lispat for the container.
ENTRYPOINT ["python3"]

CMD ['app.py']
