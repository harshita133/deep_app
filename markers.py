from flask import Flask, render_template, request, jsonify, request, send_from_directory

app = Flask(__name__)

@app.route('/markers')
def init():
    return render_template('markers.html')

@app.route('/getmarkerjson')
def sendjson():
    geojson = {
        "type": "FeatureCollection",
        "features": [{
                "type": "Feature",
                "properties": {
                    "title": "San Blas Islands",
                    "imageUrl": "https://c1.staticflickr.com/5/4241/35467523155_346b08810f_q.jpg",
                    "type": "beach",
                    "iconSize": [60, 60],
                    "image_id": "dasjsds1"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [77.10, 28.7]
                }
            },{
                    "type": "Feature",
                    "properties": {
                        "title": "San Blas Islands",
                        "imageUrl": "https://c1.staticflickr.com/5/4241/35467523155_346b08810f_q.jpg",
                        "type": "beach",
                        "iconSize": [60, 60],
                        "image_id": "dasjsds"
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [77.50, 28.6]
                    }
                },{
                        "type": "Feature",
                        "properties": {
                            "title": "San Blas Islands",
                            "imageUrl": "https://c1.staticflickr.com/5/4241/35467523155_346b08810f_q.jpg",
                            "type": "beach",
                            "iconSize": [60, 60],
                            "image_id": "dasjsds2"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [76.10, 27.7]
                        }
                    }]
        }
    return jsonify(geojson)

if __name__ == "__main__":
    app.run(debug = True)
