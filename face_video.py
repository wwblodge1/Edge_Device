import numpy as np
import cv2 as cv
import time
import paho.mqtt.client as paho
import sys

#networking stuff

# video feed capture 
cap = cv.VideoCapture(0)

# Cascade face classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# start stream 
#client.loop_start()

# while camera is turned on
while(True):
	#frame by frame capture from feed
	ret, frame = cap.read()
	
	# convert fram to grey
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) #ppz

	# display image 
	img = cv.imshow('frame',gray)
	img
	# publish 
	# for (x,y,w,h) in faces:
	# 	crop_faces = gray[y:y+h, x:x+w] # changed from img to gray FYI to follow pnpn
	# 	cv.imshow("crop", crop_faces)
	# 	client.publish("face_app/test", bytearray(cv.imencode('.png', crop_faces)[1]), qos=1)
	#OR from instructions
	# your logic goes here; for instance
	# cut out face from the frame.. 
	# rc,png = cv.imencode('.png', face)
	# msg = png.tobytes()

	# q to quit 
	if cv.waitKey(1) & 0xFF == ord('q'):
		break


# DELETE - JUST FOR TESTINGWhen everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# gray here is the gray frame you will be getting from a camera
##gray = cv.cvtColor(gray, cv.COLOR_BGR2GRAY)
##faces = face_cascade.detectMultiScale(gray, 1.3, 5)
##for (x,y,w,h) in faces:

	# ...
	#testing
	#test!!