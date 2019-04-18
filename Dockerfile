# Dockerfile for running lost in space and time

# pull base image
FROM ubuntu:16.04
FROM python:3.6

# Install.
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends git \
  python3 \
  python3-pip \
  python3-all-dev \
   gcc \
   python-dev \
   libpng-dev \
   musl-dev \
  build-essential && \
  rm -rf /var/lib/apt/lists/*

#Update pip
RUN \
  pip3 install --upgrade pip

ADD . lispat


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
  && python3 -m spacy download en


RUN pip3 install -r lispat/requirements.txt

#Set the working directory to root.
WORKDIR /root/lispat

#Give the starting argument as lispat for the container.
ENTRYPOINT ["python3"]

CMD ['app.py']
