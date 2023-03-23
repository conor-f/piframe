FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install generic utils:
RUN apt update -y && apt install -y python3 python3-pip python3-dev python3-pillow git make vim g++ wget imagemagick python3-tk

# Build the Python bindings from hzeller:
RUN git clone https://github.com/hzeller/rpi-rgb-led-matrix/
RUN cd rpi-rgb-led-matrix/bindings/python && make build-python PYTHON=$(command -v python3) && make install-python PYTHON=$(command -v python3) 

WORKDIR /app

RUN mkdir /app/config/

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

# Get a demo image as png:
RUN mkdir -p /app/resources/ && cd /app/resources && wget https://picsum.photos/64 -O demo_image && convert demo_image demo_image.png && rm demo_image

COPY src /app/src

CMD ["python3", "/app/src/piframe.py"]
