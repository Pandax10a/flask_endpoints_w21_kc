from flask import Flask, request
import dbhelpers as dh
import json

app = Flask(__name__)

@app.get('/api/clients')

def client_list_info():
    result = dh.run_statement('CALL client_list_info()')
    if(type(result) == list):
        client_json = json.dumps(result, default=str)
        return client_json
    else:
        print('error, error, error ')

@app.get('/api/loyal_clients')
def points_greater_than():
    min_point = request.args.get('min_point')
    result = dh.run_statement('CALL client_point_greater(?)', [min_point])
    if(type(result) == list):
        result_json = json.dumps(result, default=str)
        return result_json
    else:
        print('error, error, error ')


app.run(debug=True)