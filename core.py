def Core(i):

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
	
	#########################

	text = 'hi'
	interface_lang = 'school'
	label_ = ['education']

	##########################

	return (text, interface_lang, label_)