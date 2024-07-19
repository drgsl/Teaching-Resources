import sys
import json 

from PyQt6.QtGui import (
    QAction,
)

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea,
)
from PyQt6.QtCore import (
    QSize, 
    Qt,
)

from SceneEditor.Core.GameObjectWidget import GameObjectWidget
from DataStruct.Core.GameObject import GameObject

class Hierarchy(QWidget):
    _instance = None

    def __new__(cls):
        if(cls._instance == None):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

        self.goWidgets = []

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(QLabel("Hierarchy"), 0, 0)
                
        self.GameObjects_ScrollArea = QScrollArea()
        self.GameObjects_ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.GameObjects_ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.GameObjects_ScrollArea.setWidgetResizable(True)

        self.GameObjects_Widget = QWidget()
        self.GameObjects_GridLayout = QGridLayout()
        self.GameObjects_Widget.setLayout(self.GameObjects_GridLayout)
        self.GameObjects_ScrollArea.setWidget(self.GameObjects_Widget)
        
        self.mainLayout.addWidget(self.GameObjects_ScrollArea, 2, 0)

        newGameObjectButton = QPushButton("New Game Object")
        newGameObjectButton.clicked.connect(self.createNewGameObject)
        self.mainLayout.addWidget(newGameObjectButton, 1, 0)
        
        refreshButton = QPushButton("Refresh")
        refreshButton.clicked.connect(self.refresh)
        self.mainLayout.addWidget(refreshButton, 3, 0)

        self.setLayout(self.mainLayout)


    """
    # 
    # 
    # 
    """

    def refresh(self):
        self.updateScene(self.scene)

    def createNewGameObject(self):
        self.scene.addGameObject()
        self.updateScene(self.scene)

    def clearGameObjects(self):
        for goWidget in self.goWidgets:
            self.GameObjects_GridLayout.removeWidget(goWidget)
            goWidget.deleteLater()

        self.goWidgets = []

    def updateScene(self, scene):
        self.clearGameObjects()
        self.scene = scene

        for go in self.scene.GameObjects:
            goWidget = GameObjectWidget(go)
            self.goWidgets.append(goWidget)

            self.GameObjects_GridLayout.addWidget(goWidget)
            
            goWidget.DeleteAction.triggered.connect(
                lambda: self.deleteGameObject(goWidget))
            
            goWidget.DuplicateAction.triggered.connect(
                lambda: self.duplicateGameObject(goWidget))
            
            goWidget.PasteAction.triggered.connect(
                lambda: self.pasteGameObject(goWidget))
            
            goWidget.CopyAction.triggered.connect(
                lambda: self.copyGameObject(goWidget))
            
            goWidget.CutAction.triggered.connect(
                lambda: self.cutGameObject(goWidget))
            
            # goGUI.RenameAction.triggered.connect(
            #     lambda: self.renameGameObject(goGUI))


    def deleteGameObject(self, goGUI):
        self.scene.deleteGameObject(goGUI.gameObject)
        self.updateScene(self.scene)

    def duplicateGameObject(self, goGUI):
        self.scene.addGameObject(goGUI.gameObject)
        self.updateScene(self.scene)

    def pasteGameObject(self, goGUI):
        try:
            self.scene.addGameObject( GameObject.from_json(json.loads(QApplication.clipboard().text())) )
        except:
            print("Could not paste")
            print(json.load(QApplication.clipboard().text()))
            pass
        self.updateScene(self.scene)

    def copyGameObject(self, goGUI):
        QApplication.clipboard().setText(str(json.dumps(goGUI.gameObject.__dict__())))
        # self.updateScene(self.scene)
    
    def cutGameObject(self, goGUI):
        self.copyGameObject(goGUI)
        self.deleteGameObject(goGUI)

    # def renameGameObject(self, goGUI):
    #     goGUI.enterEditMode()
    #     goGUI.nameEdit.returnPressed.connect(
    #         lambda: goGUI.exitEditMode()
    #         # lambda: goGUI.gameObject.rename(goGUI.nameEdit.text()),
    #     )
    #     goGUI.nameEdit.focusOutEvent = lambda event: goGUI.exitEditMode()

app = QApplication(sys.argv)
mainWindow = Hierarchy()
# mainWindow.hide()
# app.exec()
