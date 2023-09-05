from .module import Module
from constants.constants import CLIENT_TOPICS

class Smoke(Module):
    def __init__(self, id):
        # Definir puerto y velocidad
        name = "smoke_detector"
        code = "MQ2PER100"
        collection = "smkregs"
        mqtt_topic = CLIENT_TOPICS["smoke_value"]
        mqtt_action = CLIENT_TOPICS["smoke_action"]

        super().__init__(id, name, code, collection, mqtt_topic, mqtt_action)
    