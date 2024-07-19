


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
print(Fore.BLACK + Style.BRIGHT + "start pyroGamer.Editor...")

from PyQt6 import QtCore

from PyQt6.QtCore import (
    QSize, Qt,
    QSortFilterProxyModel,
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QTabWidget, 
    QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QStatusBar,
)

from pyroGamer.Editor.GUI import Pages

ProjectDataPath = None


# TODO: Look into positional arguments and if worth it
# OpenProject_Parser.add_argument('path', type=str, help='Path to the projectData.json or the project directory')

parser = argparse.ArgumentParser(description='Editor Utility')
subparsers = parser.add_subparsers(title= 'subcommands', dest='command')
OpenProject_Parser = subparsers.add_parser('OpenProject', help='Instantiate Editor with a projectData.json file')
OpenProject_Parser.add_argument('--path', type=Path, required=True, help='Path to the projectData.json or the project directory')
# OpenProject_Parser.add_argument('--json', type=str, help='ProjectData in json format')

# GetProjectData_Parser = subparsers.add_parser('GetProjectData', help='Get projectData.json')
# GetProjectData_Parser.add_argument('--get-path', action="store_true", help='Path to the projectData.json')
# # GetProjectData_Parser.add_argument('--dirPath', action="store_true", help='Path to the project directory')
# # GetProjectData_Parser.add_argument('--json', action="store_true", help='ProjectData in json format')



args = parser.parse_args()

if args.command == "OpenProject":
    result = subprocess.run(['python', '-m', 'pyroGamer.FileManager.Editor',
                            'isValidProject', '--path', Path(args.path).as_posix()], 
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
        print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
        sys.exit(1)
    for line in result.stdout.splitlines():
        if line.startswith("isValidProject: "):
            line = line.replace("isValidProject: ", "")
            isValid = ast.literal_eval(line)
            if isValid: 
                ProjectDataPath = Path(args.path).as_posix()
            else:
                print(Fore.RED + Style.BRIGHT + "Error: " + str(args.path) + " is not a valid project")
                sys.exit(1)


# if args.command == "GetProjectData":
#     if args.get_path:
#         if(ProjectDataPath == None):
#             print(Fore.RED + "ProjectDataPath: " + str(ProjectDataPath))
#         else:
#             print(Fore.GREEN + "ProjectDataPath: " + ProjectDataPath)






app = QApplication(sys.argv)

if ProjectDataPath == None:
    window = Pages.NoProjectPage()
    window.show()
else:
    window = Pages.ProjectPage(ProjectDataPath)
    window.show()

app.exec()


