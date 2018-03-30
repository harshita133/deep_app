import json
import cv2
import numpy as np

if __name__ == "__main__":
	f = open("Hindi3_GoogleCloudVisionAPI_data.json","r+")
	j = f.read()
	if '\n' in j:
		j = j.replace('\n','')
	json_data = json.loads(j)
	img_tAnn = cv2.imread("C:/Users/Rohin/Desktop/deep_app/p3/Hindi3.jpg")
	img_word = img_tAnn.copy()
	img_symbols = img_tAnn.copy()
	
	for i in range(len(json_data['textAnnotations'])):
		x = json_data['textAnnotations'][i]['boundingPoly']['vertices']
		pt = list()
		for j in range(len(x)):
			p = [x[j]['x'] , x[j]['y']]
			pt.append(p)
		pts = np.array(pt)
		print(pts)
		pts = pts.reshape(-1,1,2)
		cv2.polylines(img_tAnn, [pts] , True, (0,0,255),2)

	
	cv2.imwrite('img_tAnn.jpg',img_tAnn)