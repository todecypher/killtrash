import numpy as np
import math
import cv2
import answer
import serial 
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import urllib.request

#Image processing
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
cap = cv2.VideoCapture(0)
model=load_model('neural.model')
x=1
frameRate = cap.get(5) #frame rate
frameId = cap.get(1) #current frame number
ret, frame = cap.read()
filename = './test/' +  str(int(x)) + ".jpg";x+=1
cv2.imwrite(filename, frame)
image = frame
image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
# classify the input image
(nonbio, bio) = model.predict(image)[0]
# build the label
label = "bio" if bio > nonbio else "nonbio"
y=label

print(y)
if y == "bio" :
	a="a"
	a=a.encode()
	ser.write(a)
else :
	b="b"
	b=b.encode()
	ser.write(b)
