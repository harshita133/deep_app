import requests
import base64
import json
import sys
import flask
from flask import Flask, render_template, request, jsonify, request, send_from_directory
from flask_pymongo import PyMongo
from flask_restful import Resource, Api, reqparse
import os
import random
import string
import pandas as pd
import numpy as np
from core import Core
from ai import Ai
from cluster import Cluster
from cluster_analysis import Cluster_analysis
from flask import Flask, render_template, request, jsonify, request, send_from_directory
from flask_pymongo import PyMongo
from pprint import pprint
from bson import BSON
from bson import json_util

app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjuna'
api = Api(app)

UPLOAD_FOLDER = os.path.basename('uploads')
p3 = os.path.basename('p3')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MONGO_DBNAME'] = 'arjuna'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/arjuna'
mongo = PyMongo(app)

ip = "0.0.0.0:5000"

@app.route('/')
def index():
	return "SIH 2018 - Text Extractor"

@app.route('/uploadform')
def form():
    return render_template('form.html')

class ImageUpload(Resource):
	def post(self):
		data = request.get_json()
		random_string = "input"
		image_data = data['image']
		fh = open( os.path.join(UPLOAD_FOLDER,random_string+".jpg"), "wb")
		fn = open( os.path.join(p3,random_string+".jpg"), "wb")
		fh.write(image_data.decode('base64'))
		fn.write(image_data.decode('base64'))
		fn.close()
		fh.close()
		return "Image Uploaded"

api.add_resource(ImageUpload, '/uploadimage')

@app.route('/markers')
def init():
    return render_template('markers.html')

@app.route('/images/<string:folder>/<string:image_name>')
def getImage(folder, image_name):
	return send_from_directory(folder, image_name)

@app.route('/getmarkerjson')
def sendjson():
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    image_info = mongo.db.image_info
    images = image_info.find({})
    for item in images:
        image_obj = {}
        image_obj["type"] = "Feature"
        image_obj["properties"] = {
            "title": item["image"],
            "imageUrl": "http://" + ip + "/images/p3/" + item["image"],
            "type": "beach",
            "iconSize": [60, 60],
            "image_id": "test"
        }
        image_obj["geometry"] = {
            "type": "Point",
            "coordinates": [float(item['longitude']), float(item['latitude'])]
        }
        geojson["features"].append(image_obj)
    return jsonify(geojson)

@app.route('/imagescreen/<string:image_name>')
def imageScreen(image_name):
    image_info = mongo.db.image_info
    x = image_info.find_one({"image": image_name})
    return json.dumps(x, sort_keys=True, indent=4, default=json_util.default)

@app.route('/report/<string:image_name>')
def report(image_name):
    image_info = mongo.db.image_info
    x = image_info.find_one({"image": image_name})
    return render_template('report.html')

@app.route('/cluster/<string:cluster_index>')
def cluster_report(cluster_index):
    clusters = mongo.db.image_info
    cluster_info = clusters.find_one({"cluster":cluster_index})
    return render_template('cluster.html', cluster = json.dumps(cluster_info, default=json_util.default))

@app.route('/a')
def a():
    return render_template('horizontal histogram.html')

@app.route('/a1')
def a1():
    return render_template('temp-plot.html')

@app.route('/a2')
def a2():
    return render_template('styled histogram.html')

new_ = Cluster('dataset.csv',2)

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug = True)
