from flask import Flask, render_template, request, jsonify, request, send_from_directory
from flask_pymongo import PyMongo
from pprint import pprint

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'arjuna'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/arjuna'
mongo = PyMongo(app)

ip = "192.168.43.24:5000"

@app.route('/markers')
def init():
    return render_template('markers.html')

@app.route('/images/<string:folder>/<string:image_name>')
def getImage(folder, image_name):
	return send_from_directory(folder, image_name)

@app.route('/getmarkerjson')
def sendjson():
    print("---------------------------------")
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
        pprint(image_obj)
        geojson["features"].append(image_obj)
    pprint(geojson)
    return jsonify(geojson)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
