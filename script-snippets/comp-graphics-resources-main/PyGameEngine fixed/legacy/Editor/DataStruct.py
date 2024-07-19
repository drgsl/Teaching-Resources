


# class SceneManager():
#     def __init__(self):
#         self.scenes = []

#     def SetActiveScene(self, scene):
#         self.activeScene = scene

#     def CreateNewScene(name):
#         scene = Scene(name)
#         pass

#     def addScene(self, scene):
#         self.scenes.append(scene)

#     def removeScene(self, scene):
#         self.scenes.remove(scene)

    
# class Scene():
#     def __init__(self, name):
#         # self.id = None
#         self.gameobjects = []
#         self.name = name
#         self.path = ""

#         self.AddGameObject(GameObject())

#     def AddGameObject(self, gameObject):
#         self.gameobjects.append(gameObject)
    
#     def RemoveGameObject(self, gameObject):
#         self.gameobjects.remove(gameObject)

# class GameObject():
#     def __init__(self, name = "New GameObject"):
#         # self.id = None
#         self.components = []
#         self.name = name
#         self.transform = Transform()


#     def AddComponent(self, component):
#         self.components.append(component)
    
#     def RemoveComponent(self, component):
#         self.components.remove(component)

# class Transform():
#     def __init__(self):
#         position = Vector3()
#         rotation = Vector3()
#         scale = Vector3()

#     def SetPosition(self, position):
#         self.position = position

#     def SetRotation(self, rotation):
#         self.rotation = rotation

#     def SetScale(self, scale):
#         self.scale = scale

#     def GetPosition(self):
#         return self.position
    
#     def GetRotation(self):
#         return self.rotation
    
#     def GetScale(self):
#         return self.scale
    
#     def Translate(self, translation):
#         self.position += translation

#     def Rotate(self, rotation):
#         self.rotation += rotation

#     def Scale(self, scale):
#         self.scale += scale



# class Vector3():
#     def __init__(self):
#         x = 0
#         y = 0
#         z = 0


# class Component():
#     def __init__():
#         pass
