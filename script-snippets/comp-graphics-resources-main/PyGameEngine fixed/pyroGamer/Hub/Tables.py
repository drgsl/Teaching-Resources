import typing
# from PyQt6.QtGui import

from PyQt6.QtCore import (
    QSize, Qt,
    QSortFilterProxyModel,
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QTabWidget, 
    QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QCheckBox, QLabel,
    QGridLayout, QVBoxLayout, QHBoxLayout,
    QFileDialog, QHeaderView, 
    QInputDialog, QFormLayout, QDialog, QMessageBox, QErrorMessage,
    QMenu,
)

import subprocess
from colorama import Fore, Back, Style, init
import textwrap 
import json
import sys
import pprint
init(autoreset=True)


# Graphical Settings for a table
class Table(QTableWidget):

    def __init__(self):
        super().__init__()
        self.setSortingEnabled(True)
        self.setShowGrid(False)
        self.setAlternatingRowColors(True)
        self.setCornerButtonEnabled(True)

        self.setSortingEnabled(True)
        self.setStyleSheet(
            "QTableWidget::item:selected {"
            "    background-color: transparent;"
            "    color: black;"
            "}"
            
            "QTableWidget {"
            "    gridline-color: transparent;"
            "    border: none;"  # Remove the border around the table
            "}"
            "QHeaderView::section {"
            "    background-color: lightgray;"
            "    border: none;"  # Remove the header borders
            "    padding: 4px;"  # Add padding to headers
            "}"
            )
        
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # self.horizontalHeader().setMaximumSectionSize(300)
        self.horizontalHeader().stretchLastSection()
    

# Table populated with projects
class ProjectTable():

    def Local():
        localTable = Table()

        def GetProjectTableHeaders():
            print(Fore.BLUE +"Instantiating " + "pyroGamer.HubConfig" + " to get ProjectTableHeaders...")

            result = subprocess.run(['python', '-m', 'pyroGamer.HubConfig', '--GetProjectsTableHeaders'], capture_output=True, text=True)

            if result.returncode != 0:
                print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout, width=100), '>'))
                print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
                sys.exit(1)

            for line in result.stdout.splitlines():
                if line.startswith("ProjectsTableHeaders:"):

                    ProjectsTableHeaders = line.replace("ProjectsTableHeaders: ", "")
                    ProjectsTableHeaders = json.loads(ProjectsTableHeaders)

            print(Fore.GREEN + Style.BRIGHT + "Received ProjectsTableHeaders: " + str(ProjectsTableHeaders))
            return ProjectsTableHeaders
        
        headers = GetProjectTableHeaders()

        localTable.setColumnCount(len(headers))
        headersWithSymbols = headers.copy()
        for header in headersWithSymbols:
            if(header == "StarButton"):
                headersWithSymbols[headers.index(header)] = "★"
            elif(header == "PlayButton"):
                headersWithSymbols[headers.index(header)] = ""
            elif(header == "EditButton"):
                headersWithSymbols[headers.index(header)] = ""
        localTable.setHorizontalHeaderLabels(headersWithSymbols)

        def GetProjectListPath():
            print(Fore.BLUE +"Instantiating " + "pyroGamer.HubConfig" + " to get ProjectListPath...")
            result = subprocess.run(['python', '-m', 'pyroGamer.HubConfig', '--GetProjectListPath'], capture_output=True, text=True)


            if result.returncode != 0:
                print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout, width=100), '>'))
                print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
                sys.exit(1)

            for line in result.stdout.splitlines():
                if line.startswith("ProjectListPath:"):

                    ProjectListPath = line.replace("ProjectListPath: ", "")

            print(Fore.GREEN + Style.BRIGHT + "Received ProjectListPath: " + str(ProjectListPath))
            return ProjectListPath
        
        ProjectListPath = GetProjectListPath()

        with open(ProjectListPath, 'r') as json_file:
            projectList = json.load(json_file)
            localTable.setRowCount(len(projectList))

            for row, project in enumerate(projectList):
                for col, header in enumerate(headers):
                    if(header == "StarButton"):
                        localTable.setCellWidget(row, col, Buttons.Star(project))
                    elif(header == "PlayButton"):
                        localTable.setCellWidget(row, col, Buttons.Play(project))
                    elif(header == "EditButton"):
                        localTable.setCellWidget(row, col, Buttons.Options(project))
                    else:
                        localTable.setItem(row, col, QTableWidgetItem(str(project[header])))
                

        return localTable


class Buttons(QPushButton):
    class Star(QPushButton):
        def __init__(self, project):
            super().__init__()
            self.setCheckable(True)
            self.toggled.connect(self.buttonClicked(project))
            self.setStyleSheet(
            "QPushButton {"
            "    border: none;"  # Remove the button border
            "}"
            "QPushButton:checked {"
            "    color: black;"
            "}"
            "QPushButton:hover {"
            "    color: grey;"
            "}"
            )
            if(project["StarButton"]):
                self.setChecked(True)
                self.setText("★")
            else:
                self.setChecked(False)
                self.setText("☆")

            font = self.font()
            font.setPointSize(15)
            self.setFont(font)

        def buttonClicked(self, project):
            def SetStar(projectID, starred):
                command = ""
                if(starred):
                    command = "--StarProject"
                else:
                    command = "--UnstarProject"
                result = subprocess.run(["python", "-m", "pyroGamer.HubConfig"] +
                                            [command, str(projectID)], 
                                            capture_output=True, text=True)
                if(result.returncode != 0):
                    print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout, width=100), '>'))
                    print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))

                print(Fore.GREEN + f"Called {command} for Project with ID: {str(projectID)}")

            def toggle():
                if(self.isChecked()):
                    self.setText("★")
                    SetStar(project['ID'], True)
                else:
                    self.setText("☆")
                    SetStar(project['ID'], False)
            return toggle
        
    class Play(QPushButton):
        def __init__(self, project):
            super().__init__()
            self.setText("▶")
            self.activeProjectPath = project["Path"]
            self.clicked.connect(self.buttonClicked)
            self.setStyleSheet(
                "QPushButton {"
                "    border: none;"
                "    text-align: center;"
                "    vertical-align: middle;"
                "}"
                "QPushButton:hover {"
                "    color: green;"
                "}"
            )
            font = self.font()
            font.setPointSize(25)
            self.setFont(font)

        def buttonClicked(self, project):
            subprocess.run(["python", "-m", "pyroGamer.Editor"] + ["--projectPath", self.activeProjectPath])

    class Options(QPushButton):
        def __init__(self, project):
            super().__init__()
            self.setText("⋮")
            self.clicked.connect(lambda: print("Options"))
            # hide the button's border
            self.setStyleSheet(
                "QPushButton {"
                "    border: none;"
                "    text-align: center;"
                "    vertical-align: middle;"
                "}"
                "QPushButton:hover {"
                "    color: green;"
                "}"
            )
            font = self.font()
            font.setPointSize(25)
            self.setFont(font)



