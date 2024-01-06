from .module import Module
import RPi.GPIO as GPIO
from constants.constants import CLIENT_TOPICS

class Extractor(Module):
    def __init__(self, id):
        # Definir puerto y velocidad
        name = "extractor"
        code = ""
        collection = ""
        mqtt_topic = ""
        mqtt_action = CLIENT_TOPICS["extractor_action"]
        #self.time_usage = {}
        self.pin = 24

        super().__init__(id, name, code, collection, mqtt_topic, mqtt_action)
    
    def getData(self):
        data = super().getData()
        #self.time_usage = data["time_usage"]
    
    def turnOn(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        super().turnOn()
        GPIO.output(self.pin, GPIO.HIGH)

    
    def turnOff(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        super().turnOff()
        GPIO.output(self.pin, GPIO.LOW)

    