

import cv2 as cv
import numpy as np
import time
import paho.mqtt.client as mqtt
import sys

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

def on_connect_local(client, userdata, flags, rc): 
    print("connected to local broker with rc: " + str(rc))
 
local_mqttclient = mqtt.Client()
local_mqttclient.loop_start()
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_connect = on_connect_local
time.sleep(1) 

# video feed capture 
cap = cv.VideoCapture(0)

# Cascade face classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

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
		local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg, qos=0, retain=False)
	
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