#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:32:33 2018
@author: rishab
"""

import requests
import base64
import json
import sys

def Core(i,lan):

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
	            "imageContext": { "languageHints":[lan] }
	        })
		request_list2.append({
	            "features": feature_json_obj2,
	            "image": content_json_obj
	        })

	headers = {'Content-Type': 'application/json'}

	key = 'AIzaSyBjFeiqo75n7MEeiFPkXkrlS4tgJj42ZiI'

	data = {"requests":request_list}

	data3 = {"requests":request_list2}

	r = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data))

	r3 = requests.post('https://vision.googleapis.com/v1/images:annotate?key={}'.format(key), headers=headers , data = json.dumps(data3))

	response_extraction = r.json()

	response_label = r3.json()
	print("Response is here")
	print(response_label)
	labels = response_label['responses'][0]["labelAnnotations"]
	print(response_extraction)
	text = response_extraction['responses'][0]['textAnnotations'][0]['description']

	l = len(response_extraction['responses'][0]['textAnnotations'])

	arr_all = []

	for i in range(1,l):
		a1 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][0]['x']
		a2 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][0]['y']
		b1 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][1]['x']
		b2 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][1]['y']
		c1 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][2]['x']
		c2 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][2]['y']
		d1 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][3]['x']
		d2 = response_extraction['responses'][0]['textAnnotations'][i]['boundingPoly']['vertices'][3]['y']
		arr_test = [[a1,a2],[b1,b2],[c1,c2],[d1,d2]]
		arr_all.append(arr_test)

	label_ = []

	for label in labels:
		label_.append(label["description"])

	data2 = {"q":text[:1000] , "target":"en"}

	r2 = requests.post("https://translation.googleapis.com/language/translate/v2?key={}".format(key) , headers = headers , data = json.dumps(data2))

	responspe_translated = r2.json()

	interface_lang = responspe_translated["data"]["translations"][0]["translatedText"]

	#########################
    #
	# text = 'थिस इस टेस्ट'
	# interface_lang = 'school university'
	# label_ = ['education' , 'office']
	# arr_all = [[[2,2],[2,2],[2,2],[2,2]],[[2,2],[2,2],[2,2],[2,2]],[[2,2],[2,2],[2,2],[2,2]]]

	##########################
	print(text, interface_lang, label_)

	text = text.encode('utf8')
    #
	# import csv
	# fields=[text,interface_lang,label_,arr_all]
	# with open(r'testing.csv', 'a') as f:
	#     writer = csv.writer(f)
	#     writer.writerow(fields)

	return (text, interface_lang, label_,arr_all)
