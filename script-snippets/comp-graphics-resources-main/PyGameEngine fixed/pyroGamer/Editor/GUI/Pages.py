


import re
import sys
import typing
import argparse
import json
import subprocess
import os
import configparser
import pprint
import textwrap
import ast
from pathlib import Path
from colorama import Fore, Back, Style, init
init(autoreset=True)

from PyQt6.QtGui import (
    QPalette, QColor,
    QFont,
    QAction, QIcon,
)

from PyQt6.QtCore import (
    QSize, Qt,
    QSortFilterProxyModel,
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QTabWidget, 
    QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QLabel,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QStatusBar,
    QFileDialog, QInputDialog, QDialog, QMessageBox,
    QFrame, QSplitterHandle, QSplitter, QSizePolicy,
)

from pyroGamer.Editor.GUI.Tabs.Assets import AssetsTab
from pyroGamer.Editor.GUI.Tabs.Terminal import TerminalTab
from pyroGamer.Editor.GUI.Tabs.Hierarchy import HierarchyTab


class ProjectPage(QMainWindow):
    def GetWindowSize():
        result = subprocess.run(['python', '-m', 'pyroGamer.Configs.Editor', '--GetWindowSize'],
                                capture_output=True, text=True)

        if result.returncode != 0:
            print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
            print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
            sys.exit(1)
        
        for line in result.stdout.splitlines():
            if line.startswith("EditorWindowSize: "):
                line = line.replace("EditorWindowSize: ", "")
                data = json.loads(line)
                return QSize(data[0], data[1])
    def __init__(self, projectPath):
        super().__init__()
        self.resize(ProjectPage.GetWindowSize())
        self.setWindowTitle(f"Editor - {projectPath}")


        # self.setStatusBar(QStatusBar(self))
        def setMenuBar():
            menu = self.menuBar()

            fileMenu = menu.addMenu("&File")
            fileMenu.addAction("&New Scene")
            fileMenu.addAction("&Open Scene...")
            fileMenu.addSeparator()
            fileMenu.addAction("&Save Scene")
            fileMenu.addAction("&Save Scene As...")
            fileMenu.addSeparator()
            fileMenu.addAction("&New Project...")
            fileMenu.addAction("&Open Project...")
            fileMenu.addSeparator()
            fileMenu.addAction("&Build Settings...")
            fileMenu.addAction("&Run")

            editMenu = menu.addMenu("&Edit")
            editMenu.addAction("&Undo")
            editMenu.addAction("&Redo")
            editMenu.addSeparator()
            editMenu.addAction("&Cut")
            editMenu.addAction("&Copy")
            editMenu.addAction("&Paste")
            editMenu.addSeparator()
            editMenu.addAction("&Delete")
            editMenu.addAction("&Duplicate")
            editMenu.addSeparator()
            editMenu.addAction("&Select All")
            editMenu.addAction("&Deselect All")

            assetsMenu = menu.addMenu("&Assets")
            createAssetsMenu = assetsMenu.addMenu("&Create")
            createAssetsMenu.addAction("&Folder")
            createAssetsMenu.addAction("&Python Script")
            createAssetsMenu.addAction("&Scene")
            createAssetsMenu.addAction("&Sprite")
            createAssetsMenu.addAction("&Audio Clip")
            createAssetsMenu.addAction("&Font")
            createAssetsMenu.addAction("&JSON")
            createAssetsMenu.addAction("&Sprite")
            createAssetsMenu.addAction("&3D Model")
            assetsMenu.addSeparator()
            assetsMenu.addAction("&Reveal in File Explorer")
            
            gameObjectMenu = menu.addMenu("&GameObject")
            gameObjectMenu.addAction("&Create Empty")
            gameObjectMenu.addAction("&Create Empty Child")
            gameObjectMenu.addSeparator()
            create3DMenu = gameObjectMenu.addMenu("&3D Objects")
            create3DMenu.addAction("&Cube")
            create3DMenu.addAction("&Sphere")
            create3DMenu.addAction("&Capsule")
            create3DMenu.addAction("&Cylinder")
            create3DMenu.addAction("&Plane")
            create3DMenu.addSeparator()
            create3DMenu.addAction("&Torus")
            create3DMenu.addAction("&Cone")
            create3DMenu.addAction("&Pyramid")
            create3DMenu.addAction("&Tube")
            create3DMenu.addAction("&Monkey")
            create3DMenu.addAction("&Donut")
            create3DMenu.addSeparator()
            create3DMenu.addAction("&3D Model")
            create2DMenu = gameObjectMenu.addMenu("&2D Objects")
            create2DMenu.addAction("&Text")
            create2DMenu.addAction("&Sprite")
            gameObjectMenu.addSeparator()
            gameObjectMenu.addAction("&Light")
            gameObjectMenu.addAction("&Camera")
            gameObjectMenu.addSeparator()
            gameObjectMenu.addAction("&Audio Source")
            gameObjectMenu.addAction("&Audio Listener")
            gameObjectMenu.addSeparator()

            componentMenu = menu.addMenu("&Component")
            meshMenu = componentMenu.addMenu("&Mesh")
            meshMenu.addAction("&Mesh Filter")
            meshMenu.addAction("&Mesh Renderer")
            physicsMenu = componentMenu.addMenu("&Physics")
            physicsMenu.addAction("&Rigidbody")
            physicsMenu.addSeparator()
            physicsMenu.addAction("&Box Collider")
            physicsMenu.addAction("&Sphere Collider")
            physicsMenu.addAction("&Capsule Collider")
            physicsMenu.addAction("&Mesh Collider")
            audioMenu = componentMenu.addMenu("&Audio")
            audioMenu.addAction("&Audio Source")
            audioMenu.addAction("&Audio Listener")
            renderingMenu = componentMenu.addMenu("&Rendering")
            renderingMenu.addAction("&Camera")
            renderingMenu.addAction("&Light")
            renderingMenu.addSeparator()
            renderingMenu.addAction("&Skybox")

            
            

            viewMenu = menu.addMenu("&View")
            viewMenu.addAction("&Scene View")
            viewMenu.addAction("&Game View")
            viewMenu.addAction("&Inspector")
            viewMenu.addAction("&Hierarchy")
            viewMenu.addAction("&Assets")
            viewMenu.addAction("&Console")
            viewMenu.addAction("&Project Settings")

            helpMenu = menu.addMenu("&Help")
            helpMenu.addAction("&About pyroGamer")
            helpMenu.addAction("&Manual")
            helpMenu.addSeparator()
            helpMenu.addAction("&Support")
            helpMenu.addAction("&Check for Updates")

            return menu
        
        setMenuBar()

        # self.setStyleSheet(Path("pyroGamer/Editor/GUI/styles/projectWindow.css").read_text())

        # TODO:
        # set ActiveScene to DefaultScene.json if it exists
        # else set ActiveScene to first scene in Assets/Scenes

        centralWidget = QWidget()
        centralWidget.setObjectName("body")
        self.setCentralWidget(centralWidget)

        mainLayout = QGridLayout(centralWidget)

        leftFrame = QFrame()
        leftFrame.setObjectName("leftFrame")
        leftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        leftFrame.setFrameShadow(QFrame.Shadow.Raised)
        leftLayout = QVBoxLayout(leftFrame)
        tabWidget = QTabWidget()
        tabWidget.tabBar().setMovable(True)
        # tabWidget.setStyleSheet("background-color: red;")
        hierarchyWidget = HierarchyTab(projectPath=projectPath)
        hierarchyWidget.setMinimumWidth(200)
        hierarchyWidget.resize(400, 800)
        tabWidget.addTab(hierarchyWidget, "Hierarchy")
        leftLayout.addWidget(tabWidget)
        leftLayout.setContentsMargins(0, 0, 0, 0)




        middleUpFrame = QFrame()
        middleUpFrame.setObjectName("middleUpFrame")
        middleUpFrame.setFrameShape(QFrame.Shape.StyledPanel)
        middleUpFrame.setFrameShadow(QFrame.Shadow.Raised)
        middleUpLayout = QVBoxLayout(middleUpFrame)
        tabWidget2 = QTabWidget()
        tabWidget2.tabBar().setMovable(True)
        tabWidget2.setStyleSheet("background-color: green;")
        sceneViewWidget = QWidget()
        sceneViewWidget.setObjectName("sceneView")
        sceneViewWidget.setMinimumSize(400, 400)
        sceneViewWidget.resize(900, 600)
        tabWidget2.addTab(sceneViewWidget, "Scene View")
        middleUpLayout.addWidget(tabWidget2)
        middleUpLayout.setContentsMargins(0, 0, 0, 0)


        middleDownFrame = QFrame()
        middleDownFrame.setObjectName("middleDownFrame")
        middleDownFrame.setFrameShape(QFrame.Shape.StyledPanel)
        middleDownFrame.setFrameShadow(QFrame.Shadow.Raised)
        middleDownLayout = QVBoxLayout(middleDownFrame)
        tabWidget3 = QTabWidget()
        tabWidget3.tabBar().setMovable(True)
        # tabWidget3.setStyleSheet("background-color: blue;")
        terminalWidget = TerminalTab(projectPath=projectPath)
        terminalWidget.setObjectName("terminal")
        terminalWidget.setMinimumSize(50, 50)
        terminalWidget.resize(900, 200)
        tabWidget3.addTab(terminalWidget, "Terminal")
        assetsWidget = AssetsTab(projectPath=projectPath)
        assetsWidget.setObjectName("assets")
        tabWidget3.addTab(assetsWidget, "Assets")
        middleDownLayout.addWidget(tabWidget3)
        

        middleSplitter = QSplitter(Qt.Orientation.Vertical)
        middleSplitter.addWidget(middleUpFrame)
        middleSplitter.addWidget(middleDownFrame)

        rightFrame = QFrame()
        rightFrame.setObjectName("rightFrame")
        rightFrame.setFrameShape(QFrame.Shape.StyledPanel)
        rightFrame.setFrameShadow(QFrame.Shadow.Raised)
        rightLayout = QVBoxLayout(rightFrame)
        tabWidget4 = QTabWidget()
        tabWidget4.tabBar().setMovable(True)
        tabWidget4.setStyleSheet("background-color: yellow;")
        inspectorWidget = QWidget()
        inspectorWidget.setObjectName("inspector")
        inspectorWidget.setMinimumWidth(200)
        inspectorWidget.resize(300, 800)
        tabWidget4.addTab(inspectorWidget, "Inspector")
        rightLayout.addWidget(tabWidget4)
        rightLayout.setContentsMargins(0, 0, 0, 0)


        mainSplitter = QSplitter(Qt.Orientation.Horizontal)
        mainSplitter.addWidget(leftFrame)
        mainSplitter.addWidget(middleSplitter)
        mainSplitter.addWidget(rightFrame)

        mainLayout.addWidget(mainSplitter)



    def NoProject(self):
        self.setCentralWidget(NoProjectPage())

class NoProjectPage(QMainWindow):
    def GetWindowSize():
        result = subprocess.run(['python', '-m', 'pyroGamer.Configs.Editor', '--GetWindowSize'],
                                capture_output=True, text=True)

        if result.returncode != 0:
            print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
            print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
            sys.exit(1)
        
        for line in result.stdout.splitlines():
            if line.startswith("EditorWindowSize: "):
                line = line.replace("EditorWindowSize: ", "")
                data = json.loads(line)
                return QSize(data[0], data[1])

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor - No Project Loaded")

        self.resize(NoProjectPage.GetWindowSize())
        self.setStyleSheet(Path("pyroGamer/Editor/GUI/styles/noProjectWindow.css").read_text())

        centralWidget = QWidget()
        centralWidget.setObjectName("CentralWidget")
        self.setCentralWidget(centralWidget)        

        mainLayout = QGridLayout()
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        centralWidget.setLayout(mainLayout)

        contentWidget = QWidget()
        contentWidget.setObjectName("ContentWidget")
        contentWidget.setFixedSize(500, 500)
        mainLayout.addWidget(contentWidget)

        contentLayout = QVBoxLayout()
        contentWidget.setLayout(contentLayout)

        label = QLabel("~ No Project Loaded ~ ")
        label.setObjectName("NoProjectLabel")
        label.setFixedSize(480, 230)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contentLayout.addWidget(label)

        buttonsLayout = QHBoxLayout()
        contentLayout.addLayout(buttonsLayout)

        openProjectButton = QPushButton("Open")
        openProjectButton.setObjectName("OpenProjectButton")
        openProjectButton.setFixedSize(230, 230)
        font = QFont()
        font = openProjectButton.font()
        font.setPointSize(40)
        openProjectButton.setFont(font)
        openProjectButton.clicked.connect(self.OpenProject)
        buttonsLayout.addWidget(openProjectButton)

        createProjectButton = QPushButton("Create")
        createProjectButton.setObjectName("CreateProjectButton")
        createProjectButton.setFixedSize(230, 230)
        font = QFont()
        font = createProjectButton.font()
        font.setPointSize(40)
        createProjectButton.setFont(font)
        createProjectButton.clicked.connect(self.CreateProject)
        buttonsLayout.addWidget(createProjectButton)



    """
    # 
    # Button Functions
    # 
    """

    def OpenProject(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '',"Project Files (*.json)")
        if fname[0] == "":
            return
        selectedPath = Path(fname[0]).as_posix()

        result = subprocess.run(['python', '-m', 'pyroGamer.FileManager.Editor',
                                'isValidProject', '--path', selectedPath],
                                capture_output=True, text=True)
        if result.returncode != 0:
            print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
            print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
            sys.exit(1)
        
        for line in result.stdout.splitlines():
            if line.startswith("isValidProject: "):
                line = line.replace("isValidProject: ", "")
                isValid = ast.literal_eval(line)
                if not isValid:
                    QMessageBox.critical(self, "Error", "The selected file is not a valid project file")
                    return
                else:
                    subprocess.Popen(['python', '-m', 'pyroGamer.Editor',
                                            'OpenProject', '--path', selectedPath])
                    sys.exit(0)
            
    def CreateProject(self):
        inputDialog = QDialog()
        inputDialog.setWindowTitle("Create new project")
        inputDialog.setWindowIcon(QIcon('pyroGamer/Editor/GUI/icons/box-label.png'))
        inputDialog.setStyleSheet(Path("pyroGamer/Editor/GUI/styles/createProjWindow.css").read_text())
        inputDialog.setFixedSize(200, 150)

        mainLayout = QVBoxLayout()
        nameInput = QLineEdit()
        nameInput.setPlaceholderText("Project Name")
        nameInput.textChanged.connect(lambda: nameInput.setText(re.sub(r'^\d|\W', '', nameInput.text())))
        mainLayout.addWidget(nameInput)

        pathInput = QLineEdit()
        pathInput.setPlaceholderText("Parent Folder Path")
        pathInput.setReadOnly(True)
        mainLayout.addWidget(pathInput)

        def browse():
            return pathInput.setText(QFileDialog.getExistingDirectory(self, "Select Directory"))
        
        browseAction = QAction("Browse")
        browseAction.setIcon(QIcon("pyroGamer/Editor/GUI/icons/blue-document-search-result.png"))
        browseAction.triggered.connect(browse)
        pathInput.addAction(browseAction, QLineEdit.ActionPosition.TrailingPosition)
        mainLayout.addWidget(pathInput)

        buttonsLayout = QHBoxLayout()
        cancelButton = QPushButton("Cancel")
        cancelButton.setObjectName("Cancel")
        cancelButton.clicked.connect(inputDialog.reject)
        buttonsLayout.addWidget(cancelButton)
        createButton = QPushButton("Create")
        createButton.setEnabled(False)
        createButton.setObjectName("Create")
        createButton.clicked.connect(inputDialog.accept)
        buttonsLayout.addWidget(createButton)
        mainLayout.addLayout(buttonsLayout)

        inputDialog.setLayout(mainLayout)

        def checkInput():
            createButton.setEnabled(nameInput.text() != "" and pathInput.text() != "")

        nameInput.textChanged.connect(checkInput)
        pathInput.textChanged.connect(checkInput)

        if inputDialog.exec() == QDialog.DialogCode.Accepted:
            name = nameInput.text()
            path = pathInput.text()
            if name == "" or path == "":
                QMessageBox.critical(self, "Error", "Please fill all fields")
                return        
            result = subprocess.run(['python', '-m', 'pyroGamer.FileManager.Editor',
                                    'createProject', '--name', name, '--path', path],
                                    capture_output=True, text=True)
            if result.returncode != 0:
                print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
                print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
                sys.exit(1)
            newProjectPath = Path(os.path.join(path, name)).as_posix()
            subprocess.Popen(['python', '-m', 'pyroGamer.Editor',
                              'OpenProject', '--path', newProjectPath])
            sys.exit(0)
            

