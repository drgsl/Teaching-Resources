import unittest
from unittest.mock import MagicMock, Mock, patch

from PyUnity.FileHandler.FileManager import FileManager

from PyUnity.DataStruct.SceneManagement.Scene import Scene

from PyUnity.DataStruct.Core.GameObject import GameObject
from PyUnity.DataStruct.Core.Transform import Transform
from PyUnity.DataStruct.Core.Vector3 import Vector3

import random

class TestSceneManager(unittest.TestCase):
    
    def test_saveLoad_EmptyScene(self):
        scene = FileManager.saveEmptyScene(name = "TestEmptyScene")
        loaded_scene = FileManager.loadScene(scene_name = scene.name)

        self.assertEqual(scene.__dict__(), loaded_scene.__dict__())

    def test_saveLoadScene_RandomValues(self):
        scene = FileManager.saveEmptyScene(name = "TestRandomScene")

        go_count = random.randint(1, 100)
        for i in range(go_count):
            scene.addGameObject(GameObject(f"GameObject {i}"))
            scene.GameObjects[i].Transform.Position = Vector3(
                random.randint(-100, 100),
                random.randint(-100, 100),
                random.randint(-100, 100)
            )
            scene.GameObjects[i].Transform.Rotation = Vector3(
                random.randint(-100, 100),
                random.randint(-100, 100),
                random.randint(-100, 100)
            )
            scene.GameObjects[i].Transform.Scale = Vector3(
                random.randint(-100, 100),
                random.randint(-100, 100),
                random.randint(-100, 100)
            )

        FileManager.saveScene(scene)
        loaded_scene = FileManager.loadScene(scene_name = scene.name)

        self.assertEqual(scene.__dict__(), loaded_scene.__dict__())


if __name__ == '__main__':
    unittest.main()