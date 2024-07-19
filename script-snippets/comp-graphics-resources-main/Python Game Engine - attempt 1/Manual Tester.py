from Engine.Core.GameObject import GameObject
from Engine.Core.Transform import Transform

from Engine.SceneManagement.SceneManager import SceneManager

from Engine.FileManagement.FileManager import FileManager

from Engine.ProjectManagement import config


import random

if __name__ == "__main__":
    scene = SceneManager.createNewScene("Scene6")

    # Create some GameObject instances and add them to the scene
    obj1 = GameObject()
    obj2 = GameObject()
    scene.GameObjects.extend([obj1, obj2])

    SceneManager.saveToFile(scene)

    print(SceneManager.loadFromFile("Scene"))
