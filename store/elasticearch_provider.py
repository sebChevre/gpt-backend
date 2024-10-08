from elasticsearch import Elasticsearch
import os

ES_URI = os.getenv('ES_URI')
ES_BASIC_USER = os.getenv('ES_BASIC_USER')
ES_BASIC_PASS = os.getenv('ES_BASIC_PASS')
ES_CERT_PATH = os.getenv('ES_CERT_PATH')


def get_elasticsearch():

    return  Elasticsearch(
        hosts=[ES_URI],  # URL Elasticsearch avec TLS
        basic_auth=(ES_BASIC_USER, ES_BASIC_PASS)
    )






