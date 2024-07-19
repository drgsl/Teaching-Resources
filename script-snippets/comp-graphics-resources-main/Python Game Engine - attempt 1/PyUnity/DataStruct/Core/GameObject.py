# from PyUnity.DataStruct.Core.Transform import Transform

from PyUnity.DataStruct.Core.Transform import Transform
import json


# TODO: Refactor & find a solution for the component problem

class GameObject():
    def __init__(self, name = "New GameObject"):
        self.name = name
        self.Transform = Transform()

    @classmethod
    def from_json(self, json):
        gameObject = GameObject(json["Name"])
        # print(json)
        gameObject.Transform = Transform.from_json(json["Components"]["Transform"])
        return gameObject
    
    def __dict__(self):
        return {
            "Name": self.name,
            "Components" : {
                "Transform": self.Transform.__dict__()
            }
        }
    
    def updateTransform(self, json):
        # print(json)
        self.Transform = Transform.from_json(json)

    def updateName(self, newName):
        self.name = newName