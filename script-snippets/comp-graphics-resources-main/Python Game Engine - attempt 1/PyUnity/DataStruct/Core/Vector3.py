import json

class Vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def from_json(cls, json):
        return cls(json["x"], json["y"], json["z"])

    def __dict__(self):
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z
        }