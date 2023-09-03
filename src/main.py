# coding: utf-8
from constants.constants import SERVER_TOPICS, CLIENT_TOPICS
from mqtt.client import client

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
        client.publish(CLIENT_TOPICS["stove_action"], payload=msg.payload, qos=1)

    elif (msg.topic == SERVER_TOPICS["smoke_action"]):
        print("smoke_action: " + str(msg.payload))
        client.publish(CLIENT_TOPICS["smoke_action"], payload=msg.payload, qos=1)

    elif (msg.topic == SERVER_TOPICS["weight_action"]):
        print("weight_action: " + str(msg.payload))
        client.publish(CLIENT_TOPICS["weight_action"], payload=msg.payload, qos=1)

    elif (msg.topic == SERVER_TOPICS["stove_value"]):
        print("stove_value: " + str(msg.payload))
        # set stove value to value recieved
        
    
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

client.loop_forever()