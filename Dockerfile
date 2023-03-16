FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y python3 python3-pip git make vim g++

WORKDIR /app

RUN git clone https://github.com/hzeller/rpi-rgb-led-matrix/
RUN cd rpi-rgb-led-matrix && make -C examples-api-use

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

COPY src /app/src

# CMD ["python3", "/app/src/test.py"]
CMD ["./rpi-rgb-led-matrix/examples-api-use/demo", "-D0", "--led-no-hardware-pulse", "--led-gpio-mapping=adafruit-hat", "--led-rows=64", "--led-cols=64"]
