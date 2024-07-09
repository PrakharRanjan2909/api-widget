from flask import Flask, jsonify, request
from app.utils import retrieve_data_from_es, config
from app.data_processing import process_costing_data, process_master_data

app = Flask(__name__)

@app.route('/chargecode', methods=['GET'])
def get_json_result_1():
    try:
        costing_df = retrieve_data_from_es(config['es_index_1'])
        if costing_df.empty:
            return jsonify({'error': 'Failed to retrieve data'}), 500
        nested_data_1 = process_costing_data(costing_df)
        return jsonify(nested_data_1)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/instancecount', methods=['GET'])
def get_json_result_2():
    try:
        master_df = retrieve_data_from_es(config['es_index_2'])
        if master_df.empty:
            return jsonify({'error': 'Failed to retrieve data'}), 500
        nested_data_2 = process_master_data(master_df)
        return jsonify(nested_data_2)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/test', methods=['POST'])
def test_api():
    try:
        req_data = request.get_json()

        if 'test_param' not in req_data:
            return jsonify({'error': 'Missing parameter: test_param'}), 400
        
        test_param_value = req_data['test_param']
        
        return jsonify({'message': f'API is working with test_param={test_param_value}'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/test2', methods=['GET'])
def test_api2():
    try:
        return jsonify({'message': 'API is working'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500