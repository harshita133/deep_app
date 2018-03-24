import requests
import base64
import json
import sys
import flask
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"


# headers = {'Content-Type': 'application/json'}

# key = 'AIzaSyCdGTSZRnFVchzlNyTcZwwZQ_TQNXhq1As'

# image_filename = 'Hindi1.jpg'
# request_list = []
# request_list2 = []


# with open(image_filename, 'rb') as image_file:
# 	content_json_obj = {
# 		"content": base64.b64encode(image_file.read()).decode('UTF-8')
# 		}

# 	feature_json_obj=[{"type": "TEXT_DETECTION"}]

# 	feature_json_obj2=[{"type": "LABEL_DETECTION"}]

# 	request_list.append({
#             "features": feature_json_obj,
#             "image": content_json_obj,
#             "imageContext": { "languageHints":["hi"] }
#         })
# 	request_list2.append({
#             "features": feature_json_obj2,
#             "image": content_json_obj
#         })

# @app.route('/core')
# def core():
# 	data = {"requests":request_list}

# 	data3 = {"requests":request_list2}

# 	r = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data))
	
# 	r3 = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data3))


# 	response_extraction = r.json()

# 	response_label = r3.json()

# 	print("JSON Length")

# 	print(len(response_extraction['responses']))

# 	labels = response_label['responses'][0]["labelAnnotations"]

# 	text = response_extraction['responses'][0]['textAnnotations'][0]['description']

# 	label_ = []

# 	for label in labels:
# 		label_.append(label["description"])
	
# 	data2 = {"q":text , "target":"en"}
	
# 	r2 = requests.post("https://translation.googleapis.com/language/translate/v2?key={}".format(key) , headers = headers , data = json.dumps(data2))

# 	responspe_translated = r2.json()
	
# 	interface_lang = responspe_translated["data"]["translations"][0]["translatedText"]

# 	print(text)
# 	print(interface_lang)
# 	print(label_)

# 	return (text , interface_lang , label_)


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0' , port = port)
