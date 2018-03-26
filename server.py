import requests
import base64
import json
import sys
import flask
from flask import Flask, render_template, request, jsonify, request
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
	return "Hello World"

@app.route('/uploadform')
def form():
    return render_template('form.html')

class ImageUpload(Resource):
	def post(self):
		random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(7)])
		data = request.get_json()
		image_data = data['image']
		fh = open( os.path.join(UPLOAD_FOLDER,random_string+".jpg"), "wb")
		fh.write(image_data.decode('base64'))
		fh.close()
		return "Image Uploaded"



api.add_resource(ImageUpload, '/uploadimage')

# headers = {'Content-Type': 'application/json'}
#
# key = 'AIzaSyCdGTSZRnFVchzlNyTcZwwZQ_TQNXhq1As'
#
# image_filename = 'uploads/2.jpg'
# request_list = []
# request_list2 = []
#
#
# with open(image_filename, 'rb') as image_file:
# 	content_json_obj = {
# 		"content": base64.b64encode(image_file.read()).decode('UTF-8')
# 		}
#
# 	feature_json_obj=[{"type": "TEXT_DETECTION"}]
#
# 	feature_json_obj2=[{"type": "LABEL_DETECTION"}]
#
# 	request_list.append({
#             "features": feature_json_obj,
#             "image": content_json_obj,
#             "imageContext": { "languageHints":["hi"] }
#         })
# 	request_list2.append({
#             "features": feature_json_obj2,
#             "image": content_json_obj
#         })
#
# @app.route('/core')
# def core():
# 	data = {"requests":request_list}
#
# 	data3 = {"requests":request_list2}
#
# 	r = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data))
#
# 	r3 = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data3))
#
#
# 	response_extraction = r.json()
#
# 	response_label = r3.json()
#
# 	print("JSON Length")
#
# 	print(len(response_extraction['responses']))
#
# 	labels = response_label['responses'][0]["labelAnnotations"]
#
# 	text = response_extraction['responses'][0]['textAnnotations'][0]['description']
#
# 	label_ = []
#
# 	for label in labels:
# 		label_.append(label["description"])
#
# 	data2 = {"q":text , "target":"en"}
#
# 	r2 = requests.post("https://translation.googleapis.com/language/translate/v2?key={}".format(key) , headers = headers , data = json.dumps(data2))
#
# 	responspe_translated = r2.json()
#
# 	interface_lang = responspe_translated["data"]["translations"][0]["translatedText"]
#
# 	print(text)
# 	print(interface_lang)
# 	print(label_)
#
# 	return "Look at the console"

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = 5000)
