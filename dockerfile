FROM python:latest
RUN pip3 install requests

WORKDIR /usr/src/app

ADD src/__main__.py ./
ADD src/modules/temperature.py ./modules/
ADD src/modules/helpers.py ./modules/

# Unbuffered output to see print inside docker logs
CMD [ "python3", "-u", "." ]