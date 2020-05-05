from flask import Flask, jsonify, make_response, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import orm
import model
import config
import repository


orm.start_mappers()
app = Flask(__name__)
get_session = sessionmaker(bind=create_engine(config.database_uri))


@app.route('/', methods=['POST'])
@app.route('/allocate', methods=['POST'])
def allocate_endpoint():
    session = get_session()
    # TODO: Extract OrderLine data from query params
    orderline = (
        request.json['order_id'],
        request.json['sku'],
        request.json['quantity'],
    )
    # TODO: Load All Batches from DB
    # TODO: Call Domain Service
    # TODO: Save Allocation in DB
    response = make_response(jsonify(), 201)
    return response
