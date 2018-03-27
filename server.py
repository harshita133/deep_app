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
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from core import Core
from ai import Ai


app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjuna'
api = Api(app)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MONGO_DBNAME'] = 'arjuna'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/arjuna'
mongo = PyMongo(app)

df = pd.read_csv('test_dataset.csv' , sep=',')

arr = df['image'].as_matrix()

@app.route('/')
def index():
	return "SIH 2018 - Text Extractor"

@app.route('/uploadform')
def form():
    return render_template('form.html')

class ImageUpload(Resource):
	def post(self):
		data = request.get_json()
		random_string = data["latitude"] + "_" + data["longitude"]
		image_data = data['image']
		fh = open( os.path.join(UPLOAD_FOLDER,random_string+".jpg"), "wb")
		fh.write(image_data.decode('base64'))
		fh.close()
		return "Image Uploaded"

api.add_resource(ImageUpload, '/uploadimage')

@app.route('/images/<string:folder>/<string:image_name>')
def getImage(folder, image_name):
	return send_from_directory(folder, image_name)

# @app.route('/analyse/', methods = ['POST'])


for i in arr:
	(text, extracted_lang, label_) = Core(i)
	(find , aware ) = Ai(extracted_lang , label_)
	print(find , aware)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = 5000)
