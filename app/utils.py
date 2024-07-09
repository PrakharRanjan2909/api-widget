import json
import pandas as pd
from elasticsearch import Elasticsearch

# Load configuration
def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)['elasticsearch']

config = load_config()

def get_es_connection():
    try:
        es = Elasticsearch(
            hosts=[config['es_conn']],
            http_auth=(config['es_user'], config['es_pass']),
        )
        return es
    except Exception as e:
        print(f"Error connecting to Elasticsearch: {e}")
        return None

def retrieve_data_from_es(index_name):
    es = get_es_connection()
    if es:
        try:
            result = es.search(index=index_name, query={"match_all": {}}, size=10000)
            hits = result['hits']['hits']
            data = [hit['_source'] for hit in hits]
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            print(f"Error retrieving data from Elasticsearch: {e}")
            return pd.DataFrame()
    else:
        return pd.DataFrame()
