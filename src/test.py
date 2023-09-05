from modules.kitchen import Kitchen
from modules.scale import Scale
from modules.stove import Stove

from decouple import config

# Crear cocina
TANUKITCHEN_ID = config("TANUKITCHEN_ID")
kitchen = Kitchen(TANUKITCHEN_ID)

# insertar módulos
# kitchen.insertModule("64b44247bb9925660ca9d076", "scale")
# kitchen.insertModule("64b44247bb9925660ca9d076", "scale")
# kitchen.insertModule("64b44247bb9925660ca9d075", "smoke_detector")
# kitchen.insertModule("64b44247bb9925660ca9d077", "stove")
# kitchen.insertModule("64b44256bb9925660ca9d07c", "extractor")

# Crear módulos
scale = object
stove = object


for module in kitchen.modules:
    if module["name"] == "scale":
        scale = Scale(module["_id"])
    elif module["name"] == "stove":
        stove = Stove(module["_id"])

while True:
    scale.readValue()
    stove.readValue()
    print (scale.value)
    print (stove.value)