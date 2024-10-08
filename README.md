# GPT-BACKEND
Backend Flask fournissant une api permettant d'interroger OPENAI en mode RAG avec des données custom

## Configure systme dempendecies
### Elasticsearch (with docker)
> cd docker
> docker compose up -d

## Install app dependencies
> pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

## Run via script
> py app.py

## Run via Flask server (recommended)
> python -m flask run

# Env values to define
LOG_FILE=<LOG FILE LOCATION>
# Elasticsearch
ES_URI=<ES_URI>
ES_BASIC_USER=<ES_USER>
ES_BASIC_PASS=<ES_BASIC_PATH>
ES_VECTOSTORE_INDEX=<ES INDEX>>
# Openai api
OPENAI_API_KEY=<OPEN_API_KEY>

# Dockerhub
[dockerhub](https://hub.docker.com/repository/docker/sebchevre/gpt-backend/general)