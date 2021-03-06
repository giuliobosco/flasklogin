FROM tiangolo/meinheld-gunicorn-flask:latest
RUN apt-get update
RUN apt-get -y install vim
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
