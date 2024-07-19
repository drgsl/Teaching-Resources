# from PyUnity.DataStruct.Core.Component import Component

from PyUnity.DataStruct.Core.Vector3 import Vector3



class Transform():
    def __init__(self):
        super().__init__()
        self.Position = Vector3()
        self.Rotation = Vector3()
        self.Scale = Vector3(1,1,1)
    
    @classmethod
    def from_json(cls, json):
        transform = Transform()
        transform.Position = Vector3.from_json(json["Position"])
        transform.Rotation = Vector3.from_json(json["Rotation"])
        transform.Scale = Vector3.from_json(json["Scale"])
        return transform

    def __dict__(self):
        return {
            "Position": self.Position.__dict__(),
            "Rotation": self.Rotation.__dict__(),
            "Scale": self.Scale.__dict__()
        }