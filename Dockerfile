FROM python:2
MAINTAINER James Mills <prologic@shortcircuitnet.au>

ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/src/app/hipachectl.py"]