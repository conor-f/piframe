FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y python3 python3-pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

COPY src /app/src

CMD ["python3", "/app/src/test.py"]
