To GET the api resonse

Run file

cd root
python -m app.run

API Endpoints

1. JSON Result 1
   Endpoint: /chargecode
   Method: GET
   Description: Retrieve nested JSON data from Elasticsearch index charge_out_costing.
2. JSON Result 2
   Endpoint: /instancecount
   Method: GET
   Description: Retrieve nested JSON data from Elasticsearch index charge_out_master.
3. JSON Result 3
   Endpoint: /test
   Method: POST
   Description: {
   Headers: `Content-Type: application/json`
   Body:
   Select raw
   Choose JSON (application/json)
   Enter your JSON data, e.g.,
   {
   "test_param": "example_value"
   }
   }

4. (optional) JSON Result 4
   Endpoint: /test2
   Method: GET
   Description: Retrieve nested JSON data from Elasticsearch index charge_out_master.
