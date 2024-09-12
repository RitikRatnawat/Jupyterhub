FROM python:3.11.9-slim

WORKDIR /jupyterhub

RUN apt-get -y update
RUN apt-get -y install nodejs npm git nano
RUN npm install -g configurable-http-proxy
RUN useradd -m test_user

COPY ./jupyterhub_config.py /jupyterhub/jupyterhub_config.py
COPY ./requirements.txt /jupyterhub/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["jupyterhub", "-f", "jupyterhub_config.py"]