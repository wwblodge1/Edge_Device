import paho.mqtt.client as mqtt
import sys

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

REMOTE_MQTT_HOST="3.235.6.54"
REMOTE_MQTT_PORT=32364
REMOTE_MQTT_TOPIC="faces"

def on_connect(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    try:
        print("{} bytes recieved".format(len(msg.payload)))
        msg = msg.payload
        remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])

print("Creating local instance")
local_mqttclient = mqtt.Client()

print("Bind call back function")
local_mqttclient.on_connect = on_connect

print("Connect to local broker")
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

print("Creating remote instance")
remote_mqttclient = mqtt.Client()

print("Connect to remote broker")
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

print("Publishing message...")
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()