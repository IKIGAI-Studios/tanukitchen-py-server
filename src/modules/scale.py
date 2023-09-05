from .module import Module
from constants.constants import CLIENT_TOPICS

class Scale(Module):
    def __init__(self, id):
        # Definir puerto y velocidad
        name = "scale"
        code = "HX711"
        collection = "scaleregs"
        mqtt_topic = CLIENT_TOPICS["weight_value"]
        mqtt_action = CLIENT_TOPICS["stove_action"]

        super().__init__(id, name, code, collection, mqtt_topic, mqtt_action)
    