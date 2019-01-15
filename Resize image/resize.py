import cv2
import numpy as np 

image = cv2.imread("lion.jpg")
#Actual image
print("press any key 	")
cv2.imshow("original" , image)
cv2.waitKey(0)
#dimension of the image
h= image.shape
print(h)

#finding the ratio
r = 200.0 / image.shape[1]
#dimension of the new image
dim = (200, int(image.shape[0] * r))
 
#perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)


