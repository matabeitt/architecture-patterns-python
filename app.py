from flask import Flask, jsonify, make_response
from model import OrderLine
app = Flask(__name__)


@app.route('/', methods=['POST'])
@app.route('/allocate', methods=['POST'])
def allocate_endpoint():
    # TODO: Extract OrderLine data from query params
    # TODO: Load All Batches from DB
    # TODO: Call Domain Service
    # TODO: Save Allocation in DB
    response = make_response(jsonify(), 201)
    return response
