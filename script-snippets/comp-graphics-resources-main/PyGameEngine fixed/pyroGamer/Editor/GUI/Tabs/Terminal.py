
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
    QProcess,
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
    QTextBrowser,
)
from PyQt6.QtGui import (
    QFileSystemModel, QStandardItemModel, QStandardItem,
)


class TerminalTab(QWidget):
    def __init__(self, projectPath):
        super().__init__()
        self.workingDirectory = Path(projectPath)

        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.textDisplay = QTextBrowser()
        self.textDisplay.setReadOnly(True)
        self.layout.addWidget(self.textDisplay)

        self.input = QLineEdit()
        self.input.returnPressed.connect(self.onReturnPressed)
        self.layout.addWidget(self.input)

        # TODO: Look into QProcess

    def onReturnPressed(self):
        command = self.input.text()
        self.input.clear()
        self.textDisplay.append(command)
        self.textDisplay.append(self.executeCommand(command))

    def executeCommand(self, command):
        result = subprocess.run(command, capture_output=True, text=True, cwd=".", shell=True)
        if result.returncode != 0:
            return Fore.RED + result.stderr
        else:
            return Fore.GREEN + result.stdout

