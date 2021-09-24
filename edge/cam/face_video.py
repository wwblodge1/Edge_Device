'''''''''''''''
Call steps: python3 face_video.py <broker addr>
'''''''''''''''

import cv2 as cv
import numpy as np
import time
import paho.mqtt.client as mqtt
import sys

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection to broker suceeded!")
    else:
        print("Connection to broker failed!")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

time.sleep(1) 

# video feed capture 
cap = cv.VideoCapture(0)

# Cascade face classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# start stream 
client.loop_start()

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
	for (x,y,w,h) in faces:
		crop_faces = gray[y:y+h, x:x+w] # changed from img to gray FYI to follow pnpn
		cv.imshow("crop", crop_faces)
		client.publish("face_app", bytearray(cv.imencode('.png', crop_faces)[1]), qos=1)
	
	#OR from instructions
	# your logic goes here; for instance
	# cut out face from the frame.. 
	# rc,png = cv.imencode('.png', face)
	# msg = png.tobytes() 

	# q to quit 
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

time.sleep(1)

# Fin
client.loop_stop()
client.disconnect()
cap.release()
cv.destroyAllWindows()