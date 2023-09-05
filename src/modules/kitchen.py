# coding=utf-8
import bd.module_controller as module_controller
from bson.objectid import ObjectId

#sudo apt-get update
#sudo apt-get install rpi.gpio

class Kitchen:
    # Constructor
    def __init__(self, id):
        
        self.id = id
        self.name = ""
        self.active = True
        self.modules = []

        self.getData()
    
    # Encender cocina
    def turnOn(self):
        self.active = True
        self.update({
            "active": self.active
        })
    
    # Apagar cocina
    def turnOff(self):
        self.active = False
        self.update({
            "active": self.active
        })
    
    # Obtener datos de la cocina desde la bd
    def getData(self):
        data = module_controller.getDocumentByFilter(
            "kitchens",
            {
                "_id": ObjectId(self.id)
            }
        )
        self.name = data["name"]
        self.active = data["active"]
        self.modules = data["modules"]
    
    # Actualizar cocina
    def update(self, updateDict):
        module_controller.update(
            "kitchens",
            {
                "_id": ObjectId(self.id),
            },
            updateDict
        )
    
    def insertModule(self, id, name):
        module_controller.push(
            "kitchens",
            {
                "_id": ObjectId(self.id),
            },
            "modules",
            {
                "_id": ObjectId(id),
                "name": name
            },
            0
        )