

from DataStruct.SceneManagement.Scene import Scene
from DataStruct.Core.GameObject import GameObject

class SceneManager():
    

    def createScene(name = "New Scene", scene_json = None):
        if scene_json == None:
            scene = Scene(name)
            scene.addGameObject(GameObject("Empty GameObject"))
            return scene
        else:   
            scene = Scene(scene_json["Name"])
            for gameObject_json in scene_json["GameObjects"]:
                gameObject = GameObject.from_json(json = gameObject_json)
                scene.GameObjects.append(gameObject)
            return scene
