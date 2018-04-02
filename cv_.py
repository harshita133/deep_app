import numpy as np
import cv2 as cv
from core import Core
 
img = cv.imread('p3/4hindi.jpg')
 
(text, interface_lang, label_,arr_all) = Core("4hindi.jpg" , "hi")

print(arr_all)
for i in arr_all:
	pts = np.array(i, np.int32)
	pts = pts.reshape((-1,1,2))
	cv.polylines(img,[pts],True,(255,0,0))
cv.imwrite('test_img.jpg',img)
cv.imshow('Draw01',img)

cv.waitKey(0)