# Docker Image for hipachectl

FROM prologic/crux-python:latest
MAINTAINER James Mills <prologic@shortcircuitnet.au>

# Startup
ENTRYPOINT ["/usr/bin/hipachectl"]
CMD ["-h"]

# Build/Runtime Dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
	rm /tmp/requirements.txt

# Application
WORKDIR /app
ADD . /app
RUN pip install .
