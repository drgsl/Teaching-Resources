import os
import json

from DataStruct.Core.GameObject import GameObject

class Scene():
    def __init__(self, name = "New Scene"):
        self.name = name
        self.GameObjects = []
    
    def __str__(self):
        return f"Scene: {self.name} with {len(self.GameObjects)} GameObjects"
    
    def addGameObject(self, gameObject = None):
        if(gameObject == None):
            gameObject = GameObject('Empty GameObject')
        self.GameObjects.append(gameObject)
    
    def deleteGameObject(self, gameObject):
        self.GameObjects.remove(gameObject)

    def __dict__(self):
        return {
            "Name": self.name,
            "GameObjects": [gameObject.__dict__() for gameObject in self.GameObjects]
        }
