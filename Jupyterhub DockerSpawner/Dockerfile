FROM python:3.11.9-slim

WORKDIR /srv/jupyterhub

RUN apt-get -y update
RUN apt-get -y install nodejs npm git nano
RUN npm install -g configurable-http-proxy

COPY ./requirements.txt /srv/jupyterhub/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]