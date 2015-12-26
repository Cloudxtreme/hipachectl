FROM prologic/python-runtime:2.7-onbuild
MAINTAINER James Mills <prologic@shortcircuitnet.au>

# Startup
ENTRYPOINT ["/usr/bin/hipachectl"]
CMD ["-h"]
