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


app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjuna'
api = Api(app)

UPLOAD_FOLDER = os.path.basename('uploads')
p3 = os.path.basename('p3')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MONGO_DBNAME'] = 'arjuna'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/arjuna'
mongo = PyMongo(app)

######################### APP ROUTES ##############################

@app.route('/')
def index():
	return "SIH 2018 - Text Extractor"

@app.route('/uploadform')
def form():
    return render_template('form.html')

class ImageUpload(Resource):
	def post(self):
		data = request.get_json()
		# random_string = data["latitude"] + "_" + data["longitude"]
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

@app.route('/images/<string:folder>/<string:image_name>')
def getImage(folder, image_name):
	return send_from_directory(folder, image_name)

new_ = Cluster('dataset.csv',2)

if __name__ == "__main__":
	app.run(port = 5000, debug = True)
