import os
import subprocess

from elasticsearch import Elasticsearch
from elasticsearch.client.indices import IndicesClient


def get_all_index(es_host):
    client = Elasticsearch(es_host)
    schema = IndicesClient(client).get_mapping()
    indices_full_list = schema.keys()
    return [index for index in indices_full_list if not index.startswith(".")]


ALL_INDEX_LIST = get_all_index(
    "http://127.0.0.1:9200"
)  # All index character series lists

# Use NPM Install Elasticdump
# Elasticdump's path
ES_DUMP_CMD = os.path.dirname(os.path.realpath(__file__))
ES_QUERY_JSON_DIR = os.path.expanduser("es.json")


def subprocess_popen(statement):
    # Can print out the output of the command
    file_out = subprocess.Popen(statement, shell=True, stdout=subprocess.PIPE)
    break_count = 0
    while True:
        line = file_out.stdout.readline()
        print(line.decode("utf-8").strip("\r\n"))
        if subprocess.Popen.poll(file_out) == 0:
            break
        if not line.decode("utf-8").strip("\r\n"):
            break_count += 1
        else:
            break_count = 0
        if break_count >= 10:
            break


def export_es_data():
    source_es_host = (
        "http://127.0.0.1:9200"  # http://username:password@127.0.0.1:9200"
    )
    # Can only export the query data according to Search_body
    search_body = '{"query": {"match_all": {}}}'
    limit = 10000  # The number of data exported every time, I heard that the maximum is 100,000, I have no test, and adjust it according to the memory size of my own machine
    index_count = 0
    for index_str in ALL_INDEX_LIST[index_count:]:
        es_export_cmd = f"{ES_DUMP_CMD} --limit={limit} --input={source_es_host}/{index_str} --output={index_str}.json --searchBody '{search_body}'"
        print(
            f"-------------export {index_str} ------------- index of ALL_INDEX_LIST: {index_count}"
        )
        print(es_export_cmd)
        subprocess_popen(es_export_cmd)
        index_count += 1


def import_es_data():
    target_es_host = (
        "http://127.0.0.1:9200"  # http://username:password@127.0.0.1:9200"
    )
    index_count = 0
    limit = 10000
    for index_str in ALL_INDEX_LIST[index_count:]:
        es_import_cmd = f"{ES_DUMP_CMD} --limit={limit} --input={ES_QUERY_JSON_DIR}{index_str}.json --output={target_es_host}"
        print(
            f"-------------import {index_str} ------------- index of ALL_INDEX_LIST: {index_count}"
        )
        print(es_import_cmd)
        subprocess_popen(es_import_cmd)
        index_count += 1
        print("")


if __name__ == "__main__":
    export_es_data()  # Export method
    # import_es_data()  #
