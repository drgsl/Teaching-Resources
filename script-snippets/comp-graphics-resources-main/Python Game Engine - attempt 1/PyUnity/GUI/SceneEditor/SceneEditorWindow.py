import sys
import os
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QToolBar,
    QMenuBar,
    QStatusBar,
    QFileDialog,
)
from PyQt6.QtCore import (
    QSize, 
    Qt,
)
from PyQt6.QtGui import (
    QAction, 
    QIcon,
    QKeySequence,
)

from FileHandler.FileManager import FileManager

from SceneEditor.Hierarchy import Hierarchy
from SceneView import SceneView
from Inspector import Inspector

# from PyUnity.DataStruct.SceneManagement.SceneManager import SceneManager


from PyUnity.GUI.config import GUI_ICONS_PATH

from PyUnity.DataStruct.ProjectManagement.config import SCENES_PATH


class SceneEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.setWindowTitle("PyUnity Scene Editor")
        print("bruh")
        layout = QGridLayout()

        self.Hierarchy = Hierarchy()
        layout.addWidget(self.Hierarchy, 0, 0)

        self.SceneView = SceneView()
        layout.addWidget(self.SceneView, 0, 1)

        self.Inspector = Inspector()
        layout.addWidget(self.Inspector, 0, 2)


        mainWidget = QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)

        # TODO: Search for default scene that should be in Project.config
        if (FileManager.searchSampleScene() == None):
            self.ActiveScene = FileManager.saveEmptyScene()

        self.ActiveScene = FileManager.loadScene(FileManager.searchSampleScene())
        self.Hierarchy.updateScene(self.ActiveScene)

        # Toolbar
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)

        create_scene_action = QAction(QIcon(f"{GUI_ICONS_PATH}/drawer--plus.png"), "New Scene", self)
        create_scene_action.setStatusTip("Create a new scene")
        create_scene_action.setShortcut(QKeySequence.StandardKey.New)
        create_scene_action.triggered.connect(self.CreateNewScene)
        toolbar.addAction(create_scene_action)
        
        load_scene_action = QAction(QIcon(f"{GUI_ICONS_PATH}/drawer--pencil.png"), "Open Scene", self)
        load_scene_action.setStatusTip("Open a scene")
        load_scene_action.setShortcut(QKeySequence.StandardKey.Open)
        load_scene_action.triggered.connect(self.OpenScene)
        toolbar.addAction(load_scene_action)

        save_scene_action = QAction(QIcon(f"{GUI_ICONS_PATH}/drawer--arrow.png"), "Save Scene", self)
        save_scene_action.setStatusTip("Save the current scene to disk")
        save_scene_action.setShortcut(QKeySequence.StandardKey.Save)
        save_scene_action.triggered.connect(self.SaveScene)
        toolbar.addAction(save_scene_action)

        toolbar.addSeparator()

        save_scene_as_action = QAction(QIcon(f"{GUI_ICONS_PATH}/drawer--arrow.png"), "Save Scene as...", self)
        save_scene_as_action.setStatusTip("Save the current scene somewhere on disk")
        save_scene_as_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        save_scene_as_action.triggered.connect(self.SaveSceneAs)
        

        # Menubar
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(create_scene_action)
        file_menu.addAction(load_scene_action)
        file_menu.addAction(save_scene_action)
        file_menu.addAction(save_scene_as_action)
        

        # Statusbar    
        self.setStatusBar(QStatusBar(self))

    def CreateNewScene(self, s):
        fname = QFileDialog.getSaveFileName(self, 'Save file', f'{SCENES_PATH}/SampleScene',"Json files (*.json)")
        if fname[0] == "":
            return
        path = Path(fname[0])
        fname = path.stem
        self.ActiveScene = FileManager.saveEmptyScene(fname)
        self.Hierarchy.updateScene(self.ActiveScene)
        

        
    def OpenScene(self, s):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '' ,"Json files (*.json)")
        if fname[0] == "":
            return
        path = Path(fname[0])
        fname = path.stem
        self.ActiveScene = FileManager.loadScene(fname)
        self.Hierarchy.updateScene(self.ActiveScene)

    def SaveScene(self, s):
        FileManager.saveScene(self.ActiveScene)

    def SaveSceneAs(self, s):
        path = QFileDialog.getSaveFileName(self, 'Save file', f"{SCENES_PATH}/{self.ActiveScene.__dict__()['Name']}","Json files (*.json)")
        if path[0] == "":
            return
        path = Path(path[0])
        fname = path.stem
        self.ActiveScene.name = fname
        justPath = path.parent
        FileManager.saveScene(self.ActiveScene, path = justPath)
        self.Hierarchy.updateScene(self.ActiveScene)
        

print("main")
app = QApplication(sys.argv)
mainWindow = SceneEditorWindow()
mainWindow.show()
app.exec()
