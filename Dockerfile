FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install generic utils:
RUN apt update -y && apt install -y python3 python3-pip git make vim g++ wget imagemagick

# Needed for building the led-image-viewer from hzeller:
RUN apt install -y libgraphicsmagick++-dev libwebp-dev

# Build the examples and utils from hzeller:
RUN git clone https://github.com/hzeller/rpi-rgb-led-matrix/
RUN cd rpi-rgb-led-matrix && make -C examples-api-use
RUN cd rpi-rgb-led-matrix/utils && make led-image-viewer

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

# Get a demo image as png:
RUN mkdir -p /app/resources/ && cd /app/resources && wget https://picsum.photos/64 -O demo_image && convert demo_image demo_image.png && rm demo_image

COPY src /app/src

# CMD ["python3", "/app/src/test.py"]
CMD ["/rpi-rgb-led-matrix/utils/led-image-viewer", "--led-no-hardware-pulse", "--led-gpio-mapping=adafruit-hat-pwm", "--led-rows=64", "--led-cols=64", "-C", "/app/resources/demo_image.png"]
