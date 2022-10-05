from flask import Flask
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



app.run(debug=True)