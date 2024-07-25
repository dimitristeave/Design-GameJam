FROM ubuntu:latest
LABEL authors="Sander"

ENTRYPOINT ["top", "-b"]