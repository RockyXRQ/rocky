FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# sys
RUN apt update && apt upgrade -y
RUN apt install -y wget

RUN apt install python3-launchpadlib -y
RUN rm -rf ~/.launchpadlib/api.launchpad.net/cache/

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

# git
RUN apt install -y git

# wpilib
RUN pip3 install Jinja2
RUN pip3 install djlint
