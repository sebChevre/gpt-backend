from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import ElasticsearchStore
from store.elasticearch_provider import get_elasticsearch

_es = None

def get_vectorstore_for_index(index_name):
    global _es

    if _es is None:

        _es = get_elasticsearch()

        return ElasticsearchStore(
            embedding=OpenAIEmbeddings(model="text-embedding-3-large"),
            es_connection=_es,
            index_name=index_name
        )


