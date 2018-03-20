import serial 

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
orig = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])

# classify the input image
(bio, nonbio) = model.predict(image)[0]

# build the label
label = "bio" if bio > nonbio else "nonbio"
x=label
print(x)
proba = bio if bio > nonbio else nonbio
label = "{}: {:.2f}%".format(label, proba * 100)

if x == "bio" :
		ser.write(1)
		print("BIO")
		
		
else :
		ser.write(1)
		print("NONBIO")