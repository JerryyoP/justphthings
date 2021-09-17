FROM debian:latest
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN pip3 install -U pip
WORKDIR /app
RUN pip3 install -U -r requirements.txt
CMD python3 ph.py
