FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y python3

WORKDIR /

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY src src

CMD ["python3", "src/test.py"]
