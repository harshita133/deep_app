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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjuna'
api = Api(app)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MONGO_DBNAME'] = 'arjuna'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/arjuna'
mongo = PyMongo(app)

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

@app.route('/images/<string:name>')
def getImage(name):
	return send_from_directory('uploads', name)

@app.route('/analyse/', methods = ['POST'])
def core():
	request_data = request.get_json()

	random_string = data["latitude"] + "_" + data["longitude"]
	image_data = request_data['image']
	fh = open( os.path.join(UPLOAD_FOLDER,random_string+".jpg"), "wb")
	fh.write(image_data.decode('base64'))
	fh.close()

	headers = {'Content-Type': 'application/json'}

	key = 'AIzaSyCdGTSZRnFVchzlNyTcZwwZQ_TQNXhq1As'

	request_list = []
	request_list2 = []

	content_json_obj = {
	"content": request_data['image']
	}

	feature_json_obj=[{"type": "TEXT_DETECTION"}]
	feature_json_obj2=[{"type": "LABEL_DETECTION"}]

	request_list.append({
	"features": feature_json_obj,
	"image": content_json_obj,
	"imageContext": { "languageHints":["hi"] }
	})

	request_list2.append({
	"features": feature_json_obj2,
	"image": content_json_obj
	})

	data = {"requests":request_list}

	data3 = {"requests":request_list2}

	# r = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data))
    #
	# r3 = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data3))

	response_extraction = r.json()

	response_label = r3.json()
	print("JSON Length")

	print(len(response_extraction['responses']))

	labels = response_label['responses'][0]["labelAnnotations"]

	text = response_extraction['responses'][0]['textAnnotations'][0]['description']

	label_ = []

	for label in labels:
		label_.append(label["description"])

	data2 = {"q":text , "target":"en"}

	# r2 = requests.post("https://translation.googleapis.com/language/translate/v2?key={}".format(key) , headers = headers , data = json.dumps(data2))
	responspe_translated = r2.json()

	interface_lang = responspe_translated["data"]["translations"][0]["translatedText"]

	print(text)
	print(interface_lang)
	print(label_)

	return "Look at the console"

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = 5000, debug = True)
