import numpy as np 
import cv2
import matplotlib.pyplot as plt 

global rect

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('face.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for(x,y,w,h) in faces:
	cv2.rectangle(img, (x-100, y-100), (x+w+100, y+h+100), (0,255,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	rect = (x-70,y-70,w+100,h+140)

img2 = img 
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)


cv2.grabCut(img2, mask, rect,bgdModel,fgdModel, 30, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2 ) | (mask == 0) , 0, 1).astype('uint8')
# cv2.rectangle(img2, (x,y), (w, h), (255,0,0), 2)
img2 = img2*mask2[:, :, np.newaxis]

cv2.imshow('imageINPUT', img)
cv2.imshow('image2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()