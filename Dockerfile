FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /

RUN echo "Hello world!"
