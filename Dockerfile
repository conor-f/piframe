FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /

CMD ["/usr/bin/echo", "'Hello, world!'"]
