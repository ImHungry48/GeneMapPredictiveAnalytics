# app.py using Flask
import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from GeneMapAnalytics import get_patient_genes

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# File was largely to be used to trigger python functions to analyze and return results from the algorithms


## This path was an example of triggering a python function from the front-end react application
@app.route('/api/get-patient-genes', methods=['POST'])
def get_patient_genes():
    data = request.json
    
    # Call your method here
    results = get_patient_genes(data)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
