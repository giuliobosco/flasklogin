FROM tiangolo/meinheld-gunicorn-flask:latest
RUN apt-get update
RUN apt-get -y install vim
