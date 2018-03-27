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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'arjuna'
api = Api(app)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MONGO_DBNAME'] = 'arjuna'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/arjuna'
mongo = PyMongo(app)

def ai(interface_lang, label_):
	count = CountVectorizer()

	info = [interface_lang]

	bag = count.fit_transform(info)

	analyze = count.build_analyzer()

	arr = analyze(info[0])

	arr2 = np.unique(arr)

	arr3 = np.array(label_)

	arr2 = np.concatenate((arr2 , arr3) , axis = 0)

	edu_tags = ['education' , 'school','university','class']
	medical_tags = ['hospital','health','dispensary','clinic','faculty','surgery','nursing','home','emergency']
	chemist_tags = ['chemist','medical','pharmacy','store']
	water_supply_tags = ['water','supply']
	env_tags = ['forest','river','wildlife','sanctuary','park']
	admin_tags = ['panchayat','office','union','vidhan','system','rural','authority','development','raj']
	power_supply_tags = ['power','electricity','light']
	gas_supply_tags = ['gas','gasoline','lpg','indane','hp']
	filling_stations_tags = ['petrol','diesel','gasoline','cng','petroleum','hp','Indian','oil']
	transport_tags = ['transport','railway','airport','bus','roadways','train']

	awareness_tags = ['scheme','aware','yojna','plan','development']

	find = []
	aware = []
	for i in edu_tags:
	    if i in arr2:
	        find.append([i,'edu_tag'])
	for i in medical_tags:
	    if i in arr2:
	        find.append([i,'medical_tag'])
	for i in chemist_tags:
	    if i in arr2:
	        find.append([i,'chemist_tags'])
	for i in water_supply_tags:
	    if i in arr2:
	        find.append([i,'water_suply_tags'])
	for i in env_tags:
	    if i in arr2:
	        find.append([i,'env_tags'])
	for i in admin_tags:
	    if i in arr2:
	        find.append([i,'admin_tags'])
	for i in power_supply_tags:
	    if i in arr2:
	        find.append([i,'power_supply_tags'])
	for i in gas_supply_tags:
	    if i in arr2:
	        find.append([i,'gas_supply_tags'])
	for i in filling_stations_tags:
	    if i in arr2:
	        find.append([i,'filling_stations_tags'])
	for i in transport_tags:
	    if i in arr2:
	        find.append([i,'transport_tags'])

	for i in awareness_tags:
	    if i in arr2:
	        aware.append([i,'awareness_tags'])

	return (find , aware)


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
def core(i):
	# request_data = request.get_json()
    #
	# random_string = data["latitude"] + "_" + data["longitude"]
	# image_data = request_data['image']
	# fh = open( os.path.join(UPLOAD_FOLDER,random_string+".jpg"), "wb")
	# fh.write(image_data.decode('base64'))
	# fh.close()
	request_list = []
	request_list2 = []

	with open('p3/'+i, 'rb') as image_file:
		content_json_obj = {
			"content": base64.b64encode(image_file.read()).decode('UTF-8')
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

	headers = {'Content-Type': 'application/json'}

	key = 'AIzaSyCdGTSZRnFVchzlNyTcZwwZQ_TQNXhq1As'

	# content_json_obj = {
	# "content": request_data['image']
	# }
    #
	# feature_json_obj=[{"type": "TEXT_DETECTION"}]
	# feature_json_obj2=[{"type": "LABEL_DETECTION"}]
    #
	# request_list.append({
	# "features": feature_json_obj,
	# "image": content_json_obj,
	# "imageContext": { "languageHints":["hi" , "ta"] }
	# })
    #
	# request_list2.append({
	# "features": feature_json_obj2,
	# "image": content_json_obj
	# })

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

	# interface_lang = responspe_translated["data"]["translations"][0]["translatedText"]

	text = 'hi'
	# interface_lang = 'school'
	# label_ = ['education']
	print(text)
	print(interface_lang)
	print(label_)

	return (text, interface_lang, label_)

for i in arr:
	(text, extracted_lang, label_) = core(i)
	(find , aware ) = ai(extracted_lang , label_)
	print(find , aware)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = 5000, debug = True)
