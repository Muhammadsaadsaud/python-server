from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/process", methods=['POST'])
def process():
    data = (request.data)
    print(data)
    return jsonify(["./../assets/fish1.jpg","./../assets/fish2.jpg","./../assets/fish3.jpg","./../assets/fish4.jpg","./../assets/fish5.jpg"])