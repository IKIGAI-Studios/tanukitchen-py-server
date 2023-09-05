# coding: utf-8
import time
from constants.constants import SERVER_TOPICS, CLIENT_TOPICS
from mqtt.client import client
from modules.kitchen import Kitchen
from modules.scale import Scale
from modules.stove import Stove
from modules.smoke import Smoke
from modules.extractor import Extractor

from decouple import config

# Crear cocina
TANUKITCHEN_ID = config("TANUKITCHEN_ID")
kitchen = Kitchen(TANUKITCHEN_ID)

# Crear módulos
scale = object
stove = object
smoke_detector = object
extractor = object

# Inicializar módulos
for module in kitchen.modules:
    if module["name"] == "scale":
        scale = Scale(module["_id"])
    elif module["name"] == "stove":
        stove = Stove(module["_id"])
    elif module["name"] == "smoke_detector":
        smoke_detector = Smoke(module["_id"])
    elif module["name"] == "extractor":
        extractor = Extractor(module["_id"])


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    if (msg.topic == SERVER_TOPICS["stove_action"]):
        print("stove_action: " + str(msg.payload))
        stove.processAction(str(msg.payload))

    elif (msg.topic == SERVER_TOPICS["smoke_action"]):
        print("smoke_action: " + str(msg.payload))
        smoke_detector.processAction(str(msg.payload))

    elif (msg.topic == SERVER_TOPICS["weight_action"]):
        print("weight_action: " + str(msg.payload))
        scale.processAction(str(msg.payload))

    elif (msg.topic == SERVER_TOPICS["extractor_action"]):
        print("weight_action: " + str(msg.payload))
        extractor.processAction(str(msg.payload))


    elif (msg.topic == SERVER_TOPICS["stove_value"]):
        print("stove_value: " + str(msg.payload))
    
    elif (msg.topic == SERVER_TOPICS["smoke_value"]):
        print("smoke_value: " + str(msg.payload))
    
    elif (msg.topic == SERVER_TOPICS["weight_value"]):
        print("weight_value: " + str(msg.payload))
    
    else:
        print("Unknown topic: " + str(msg.topic) + " Message: " + str(msg.payload))



# setting callbacks, use separate functions like above for better visibility
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

def _process():
    while True:
        scale.readValue()
        stove.readValue()
        smoke_detector.readValue()
        time.sleep(0.5)



_process()
client.loop_forever()

# Lectura de datos