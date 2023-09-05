# coding=utf-8
import bd.module_controller as module_controller
from bson.objectid import ObjectId
from datetime import datetime
from utils.get_arduino_value import getValueFromArduino
from mqtt.client import client

#sudo apt-get update
#sudo apt-get install rpi.gpio

class Module:
    # Constructor
    def __init__(self, id, name, code, collection, topic, action):
        self.id = id

        self.name = name
        self.code = code
        self.active = True
        self.value = 0
        self.target = 0
        self.collection = collection
        self.mqtt_client = client
        self.mqtt_topic = topic
        self.mqtt_action = action

        self.getData()
    
    # Función para override
    def readValue(self):
        self.value = getValueFromArduino(self.code)
        self.mqtt_client.publish(self.mqtt_topic, payload=self.value, qos=1)
        self.insertValue(self.value)
    
    # Encender módulo
    def turnOn(self):
        self.updateModule("active", True)
        self.mqtt_client.publish(self.mqtt_action, payload="ON", qos=1)
    
    # Apagar módulo
    def turnOff(self):
        self.updateModule("active", False)
        self.mqtt_client.publish(self.mqtt_action, payload="OFF", qos=1)
    
    def processAction(self, action):
        if action == "ON":
            self.turnOn()
        elif action == "OFF":
            self.turnOff()

    # Obtener datos del módulo
    def getData(self):
        data = module_controller.getDocumentByFilter(
            "modules",
            {
                "_id": ObjectId(self.id)
            }
        )
        self.name = data["name"]
        self.active = data["active"]

        if data.get("value") != None:
            self.value = data["value"]
        if data.get("target") != None:
            self.target = data["target"]

        return data

    
    # Actualizar un dato del módulo
    def updateModule(self, key, value):
        module_controller.update(
            "modules",
            {
                "_id": ObjectId(self.id),
            },
            {
                key: value
            }
        )
    
    # Insertar valor de lectura en el módulo
    def insertValue(self, value):
        module_controller.insert(
            self.collection,
            {
                "date": datetime.now(),
                "value": value
            }
        )

    # Leer valores desde arduino
    # def getValueFromArduino(self, name):
    #     line = self.serial.readline().decode('utf-8').rstrip()
        
    #     # Dividir la línea de datos en las partes correspondientes
    #     parts = line.split('|')

    #     for part in parts:
            
    #         if part.find(name) != -1:
    #             var = part.split(':')

    #             # Recuperar valor del módulos
    #             self.value = float(var[1])
           
