from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')


def make_index(es, index_name):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        es.indices.create(index=index_name)
