import os
import json

import DataStruct.ProjectManagement.config as config
from DataStruct.SceneManagement.SceneManager import SceneManager

class FileManager():
    
    '''
    # 
    # Scene Management
    # 
    '''
    
    ##### Scene Saving #####
    
    # TODO: Refactor into a single method
    def saveEmptyScene(name = "SampleScene", path = config.SCENES_PATH):
        scene = SceneManager.createScene(name)
        FileManager.saveScene(scene, path)

        return scene


    def saveScene(scene, path = config.SCENES_PATH):
        if not os.path.exists(path):
            os.makedirs(path)

        fileName = f"{scene.__dict__()['Name']}.json"
        filePath = os.path.join(path, fileName)

        with open(filePath, 'w') as file:
            json.dump(scene.__dict__(), file, indent=4)
            
        print(f"Saved {fileName} to {filePath}")



    ##### Scene Loading #####

    def loadScene(scene_name, path = config.SCENES_PATH):
        fileName = f"{scene_name}.json"
        filePath = os.path.join(path, fileName)

        if not os.path.exists(path):
            return None

        with open(filePath, 'r') as file:
            scene_json = json.load(file)
        print(f"Loaded {fileName} from {filePath}")
        return SceneManager.createScene(scene_json=scene_json)
    
    def searchSampleScene(path = config.SCENES_PATH):
        for file in os.listdir(path):
            if file.endswith(".json"):
                if file[:-5] == "SampleScene":
                    return file[:-5]
        return None

