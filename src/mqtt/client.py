# coding: utf-8
import paho.mqtt.client as paho
from paho import mqtt
from decouple import config
from constants.constants import SERVER_TOPICS, CLIENT_TOPICS

# Constants
MQTT_HOST = config("MQTT_HOST")
MQTT_PORT = config("MQTT_PORT")
MQTT_USERNAME = config("MQTT_USERNAME")
MQTT_PASSWORD = config("MQTT_PASSWORD")

client = paho.Client(client_id="hola", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_HOST, int(MQTT_PORT))
client.subscribe(SERVER_TOPICS["tanukitchen_server"], qos=1)