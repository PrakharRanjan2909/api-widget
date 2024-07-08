from flask import Flask, jsonify
from app.elasticsearch_utils import retrieve_data_from_es
from app.data_processing import process_costing_data, process_master_data
from app.config import config

app = Flask(__name__)

@app.route('/api/chargecode', methods=['GET'])
def get_json_result_1():
    try:
        costing_df = retrieve_data_from_es(config['es_index_1'])
        if costing_df.empty:
            return jsonify({'error': 'Failed to retrieve data'}), 500
        nested_data_1 = process_costing_data(costing_df)
        return jsonify(nested_data_1)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/instancecnt', methods=['GET'])
def get_json_result_2():
    try:
        master_df = retrieve_data_from_es(config['es_index_2'])
        if master_df.empty:
            return jsonify({'error': 'Failed to retrieve data'}), 500
        nested_data_2 = process_master_data(master_df)
        return jsonify(nested_data_2)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
