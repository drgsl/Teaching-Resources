
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
    QTreeView,
)
from PyQt6.QtGui import (
    QFileSystemModel, QStandardItemModel, QStandardItem,
)



class HierarchyTab(QWidget): 
    def __init__(self, projectPath):
        super().__init__()
        self.projectPath = Path(projectPath)
        self.layout = QGridLayout(self)

        self.treeView = QTreeView()
        self.layout.addWidget(self.treeView)
        self.treeView.header().hide()


        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)

        if not self.projectPath.is_dir():
            self.projectPath = self.projectPath.parent

        scenesFolderPath = Path(os.path.join(self.projectPath, "Assets", "Scenes")).as_posix()

        # TODO: get the active scene from the ProjectData.json file

        activeScene = None
        result = subprocess.run(['python', '-m', 'pyroGamer.FileManager.Editor', 
                                'getLatestSavedScene', '--projectPath', self.projectPath.as_posix()],
                                capture_output=True, text=True) 
        if result.returncode != 0:
            print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
            print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
            sys.exit(1)          
        for line in result.stdout.splitlines():
            if line.startswith("LatestSavedScene: "):
                activeScene = line.replace("LatestSavedScene: ", "")
                activeScenePath = Path(activeScene).as_posix()
        
        with open(activeScene, "r") as f:
            scene = json.load(f)

        self.rootItem = QStandardItem(scene["Name"])
        self.model.appendRow(self.rootItem)

        for obj in scene["GameObjects"]:
            self.rootItem.appendRow(QStandardItem(obj["Name"]))
            


class GameObject(QStandardItem):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.name = name
        self.parent = parent
        self.children = []
        self.components = []

    def addChild(self, child):
        self.children.append(child)

    def addComponent(self, component):
        self.components.append(component)

    def __repr__(self):
        return f"GameObject({self.name})"

    def __str__(self):
        return f"GameObject({self.name})"





