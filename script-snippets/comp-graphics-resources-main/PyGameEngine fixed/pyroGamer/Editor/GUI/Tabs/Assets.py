
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



class AssetsTab(QWidget):
    def __init__(self, projectPath):
        super().__init__()
        self.projectPath = Path(projectPath)
        if(not Path(projectPath).is_dir()):
            self.projectPath = Path(projectPath).parent.as_posix()
            print(Fore.BLACK + Style.BRIGHT + self.projectPath)

        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.model = QFileSystemModel()
        self.model.setRootPath(Path(self.projectPath).as_posix())
        print(Fore.BLACK + Style.BRIGHT + Path(self.projectPath).as_posix())

        self.treeView = QTreeView()
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(Path(self.projectPath).as_posix()))
        self.treeView.setSortingEnabled(True)
        self.treeView.setIndentation(10)

        self.layout.addWidget(self.treeView)


