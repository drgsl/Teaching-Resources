import sys

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
    
)

from PyQt6.QtGui import (
    QAction, QIcon,
)

# from pyroGamer.DataManager.Configs import (
#     LocalConfig, CloudConfig,
# )

import subprocess
import multiprocessing
from pathlib import Path
import json
import argparse
import pprint
import textwrap
from colorama import Fore, Back, Style, init
init(autoreset=True)


from pyroGamer.Hub.Tables import ProjectTable

class LocalTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(QLineEdit())
        openProjectButton = QPushButton("Open")
        buttonsLayout.addWidget(openProjectButton)
        openProjectButton.clicked.connect(self.open_project)
        newProjectButton = QPushButton("New")
        buttonsLayout.addWidget(newProjectButton)
        newProjectButton.clicked.connect(self.new_project)
        self.layout.addLayout(buttonsLayout)

        self.layout.addWidget(ProjectTable.Local())
        
        self.setLayout(self.layout)


        

    def open_project(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '' ,"Json files (*.json)")
        if fname[0] == "":
            return
        path = Path(fname[0])

        # LocalConfig.AddProject(path)
        print(Fore.BLUE + "Calling " + "pyroGamer.HubConfig --AddExistingProject" + " to open project...")
        result = subprocess.run(['python', '-m', 'pyroGamer.HubConfig',
                                  '--AddExistingProject', str(path.as_posix())],
                                  capture_output=True, text=True)
        
        if result.returncode != 0:
            print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout, width=100), '>'))
            print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
            sys.exit(1)

        self.RefreshTable()


    def new_project(self):
        inputDialog = QDialog()
        inputDialog.setWindowTitle("Create new project")
        inputDialog.setFixedSize(200, 200)
        mainLayout = QVBoxLayout()
    
        nameLayout = QHBoxLayout()
        # label = QLabel("Project Name:")
        # nameLayout.addWidget(label)
        NameInput = QLineEdit()
        NameInput.setPlaceholderText("Project Name")
        nameLayout.addWidget(NameInput)
        mainLayout.addLayout(nameLayout)

        pathLayout = QHBoxLayout()
        # label = QLabel("Parent Folder Path:")
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # pathLayout.addWidget(label)
        PathInput = QLineEdit()
        PathInput.setPlaceholderText("Parent Folder Path")
        PathInput.setReadOnly(True)
        pathLayout.addWidget(PathInput)

        def browse():
            return PathInput.setText(QFileDialog.getExistingDirectory(self, "Select Directory"))
        
        browseAction = QAction("Browse")
        browseAction.setIcon(QIcon("pyroGamer/Hub/icons/blue-document-search-result.png"))
        browseAction.triggered.connect(browse)
        PathInput.addAction(browseAction, QLineEdit.ActionPosition.TrailingPosition)

        mainLayout.addLayout(pathLayout)

        buttonsLayout = QVBoxLayout()
        CreateButton = QPushButton("Create")
        buttonsLayout.addWidget(CreateButton)
        def fields_filled():
            return NameInput.text() != "" and PathInput.text() != ""
        
        def createProject():
            if not fields_filled():
                QMessageBox.critical(None, "Error", "Please fill in all fields")
                return
            
            print(Fore.BLUE + "Calling " + "pyroGamer.HubConfig AddNewProject --name --path" + " to add new project...")
            result = subprocess.run(['python', '-m', 'pyroGamer.HubConfig',
                                  'AddNewProject', '--name', NameInput.text(), '--path', Path(PathInput.text()).as_posix()],
                                  capture_output=True, text=True)
            
            if(result.returncode != 0):
                print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout, width=100), '>'))
                print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
                sys.exit(1)
            
            self.RefreshTable()
            inputDialog.close()
        
        CreateButton.clicked.connect(createProject)

        CancelButton = QPushButton("Cancel")
        buttonsLayout.addWidget(CancelButton)
        CancelButton.clicked.connect(lambda: inputDialog.close())
        mainLayout.addLayout(buttonsLayout)

        inputDialog.setLayout(mainLayout)

        inputDialog.exec()

    def RefreshTable(self):
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
                self.layout.removeWidget(widget)

        self.layout.addWidget(ProjectTable.Local())
        self.setLayout(self.layout)
        



# class Local(QWidget):
#     def __init__(self, ProjectListPath):
#         super().__init__()
#         layout = QVBoxLayout()
#         buttonsLayout = QHBoxLayout()
#         buttonsLayout.addWidget(QLineEdit())
        
#         openProjectButton = QPushButton("Open")
#         buttonsLayout.addWidget(openProjectButton)
#         openProjectButton.clicked.connect(self.open_project)

#         newProjectButton = QPushButton("New")
#         buttonsLayout.addWidget(newProjectButton)
#         newProjectButton.clicked.connect(self.new_project)
#         layout.addLayout(buttonsLayout)

#         layout.addWidget(Projects_Table.Local(ProjectListPath))

#         self.setLayout(layout)

#     def open_project(self):
#         fname = QFileDialog.getOpenFileName(self, 'Open file', '' ,"Json files (*.json)")
#         if fname[0] == "":
#             return
#         path = Path(fname[0])

#         LocalConfig.AddProject(path)
#         Local.RefreshTable()

#     def new_project(self):        
#         inputDialog = QDialog()

#         mainLayout = QVBoxLayout()
#         mainLayout.addWidget(QLabel("Create new project"))
        
#         nameLayout = QHBoxLayout()
#         nameLayout.addWidget(QLabel("Project Name:"))
#         NameInput = QLineEdit()
#         nameLayout.addWidget(NameInput)
#         mainLayout.addLayout(nameLayout)

#         pathLayout = QHBoxLayout()
#         pathLayout.addWidget(QLabel("Parent Folder Path:"))
#         PathInput = QLineEdit()
#         PathInput.setReadOnly(True)
#         pathLayout.addWidget(PathInput)
#         BrowsePathButton = QPushButton("Browse")
#         pathLayout.addWidget(BrowsePathButton)
#         def browse():
#             return PathInput.setText(QFileDialog.getExistingDirectory(self, "Select Directory"))
#         BrowsePathButton.clicked.connect(browse)
#         mainLayout.addLayout(pathLayout)

#         buttonsLayout = QHBoxLayout()
#         CreateButton = QPushButton("Create")
#         buttonsLayout.addWidget(CreateButton)
#         def fields_filled():
#             return NameInput.text() != "" and PathInput.text() != ""
#         def createProject():
#             if not fields_filled():
#                 QMessageBox.critical(None, "Error", "Please fill in all fields")
#                 return
#             LocalConfig.AddEmptyProject(name = NameInput.text(), path = Path(PathInput.text())) 
#             Local.RefreshTable()   
#             inputDialog.close()
            
#         CreateButton.clicked.connect(createProject)

#         CancelButton = QPushButton("Cancel")
#         buttonsLayout.addWidget(CancelButton)
#         CancelButton.clicked.connect(lambda: inputDialog.close())
#         mainLayout.addLayout(buttonsLayout)

#         inputDialog.setLayout(mainLayout)

#         inputDialog.exec()

    
#     def RefreshTable():
#         Local.clearTable()
#         Projects_Table.populateTable(Projects_Table.table, LocalConfig.GetProjectList())

#     def clearTable():
#         Projects_Table.table.clearContents()
#         Projects_Table.table.setRowCount(0)


# class Cloud(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QGridLayout()

#         layout.addWidget(Projects_Table.Cloud())

#         self.setLayout(layout)

# class Projects_Table(QTableWidget):
#     LocalTable = QTableWidget()

#     def Cloud():
#         return Projects_Table.From(CloudConfig)

    
#     def Local(ProjectListPath):
#         Projects_Table.initTable(Projects_Table.LocalTable)

#         headers = []
#         for col in range(Projects_Table.table.columnCount()):
#             header_item = Projects_Table.table.horizontalHeaderItem(col)
#             if header_item is not None:
#                 headers.append(header_item.text())


#         def item_changed(item):
#             project_list = configClass.GetProjectList()

#             if (item.column() == headers.index("Name")):
#                 configClass.SetName(project_list[item.row()]["ID"], item.text())
#             # elif (item.column() == headers.index("Path")):
#             #     configClass.SetPath(project_list[item.row()]["ID"], item.text())
#             # elif (item.column() == headers.index("Created")):
#             #     configClass.SetCreated(project_list[item.row()]["ID"], item.text())
#             else:
#                 pass

#         Projects_Table.table.itemChanged.connect(item_changed)

#         Projects_Table.populateTable(Projects_Table.table, configClass.GetProjectList())

#         return Projects_Table.table
    



#     def populateTable(table, project_list):
#         if(table is None):
#             table = Projects_Table.table
#         table.setRowCount(len(project_list))

#         for row, project in enumerate(project_list):
#             table.setCellWidget(row, 0, Buttons.Star(project))

#             project_name = QTableWidgetItem(project["Project Name"])
#             project_name.setFlags(Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled)
#             table.setItem(row, 1, project_name)

#             project_path = QTableWidgetItem(project["Project Path"])
#             project_path.setFlags(Qt.ItemFlag.ItemIsEnabled)
#             table.setItem(row, 2, project_path)

#             created_date = QTableWidgetItem(project["Created"])
#             created_date.setFlags(Qt.ItemFlag.ItemIsEnabled)
#             table.setItem(row, 3, created_date)

#             table.setCellWidget(row, 4, Buttons.Play(project))
#             table.setCellWidget(row, 5, Buttons.Options(project))

#         return table
    
#     def initTable(table):
#         # headers = tableConfig['TABLE_HEADERS']
#         # table.setColumnCount(len(headers))
#         # table.setHorizontalHeaderLabels(headers)

#         table.setSortingEnabled(True)
#         table.setStyleSheet(
#             "QTableWidget::item:selected {"
#             "    background-color: transparent;"
#             "    color: black;"
#             "}"
            
#             "QTableWidget {"
#             "    gridline-color: transparent;"
#             "    border: none;"  # Remove the border around the table
#             "}"
#             "QHeaderView::section {"
#             "    background-color: lightgray;"
#             "    border: none;"  # Remove the header borders
#             "    padding: 4px;"  # Add padding to headers
#             "}"
#             )  
#         # table_unit = tableConfig['TABLE_UNIT']
#         table.setColumnWidth(0, 25)
#         table.setColumnWidth(1, 25 * 5)
#         table.setColumnWidth(2, 25 * 7)
#         table.setColumnWidth(3, 25 * 3)
#         table.setColumnWidth(4, 25)
#         table.setColumnWidth(5, 25)

#         return table


# # Only Local for now
# class Buttons(QPushButton):
#     class Star(QPushButton):
#         def __init__(self, project):
#             super().__init__()
#             self.setCheckable(True)
#             self.toggled.connect(self.buttonClicked(project))
#             self.setStyleSheet(
#             "QPushButton {"
#             "    border: none;"  # Remove the button border
#             "}"
#             "QPushButton:checked {"
#             "    color: black;"
#             "}"
#             "QPushButton:hover {"
#             "    color: grey;"
#             "}"
#             )
#             if(project["Star"]):
#                 self.setChecked(True)
#                 self.setText("★")
#             else:
#                 self.setChecked(False)
#                 self.setText("☆")

#             font = self.font()
#             font.setPointSize(15)
#             self.setFont(font)

#         def buttonClicked(self, project):
#             def toggle():
#                 if(self.isChecked()):
#                     # print(f"Starred + {project['Project Name']}")
#                     # project["Star"] = True
#                     self.setText("★")
#                     LocalConfig.SetStar(project["ID"], True)
#                 else:
#                     # print(f"Unstarred + {project['Project Name']}")
#                     # project["Star"] = False
#                     self.setText("☆")
#                     LocalConfig.SetStar(project["ID"], False)
#             return toggle
        
#     class Play(QPushButton):
#         def __init__(self, project):
#             super().__init__()
#             self.setText("▶")
#             self.activeProjectPath = project["Project Path"]
#             self.clicked.connect(self.buttonClicked)
#             self.setStyleSheet(
#                 "QPushButton {"
#                 "    border: none;"
#                 "    text-align: center;"
#                 "    vertical-align: middle;"
#                 "}"
#                 "QPushButton:hover {"
#                 "    color: green;"
#                 "}"
#             )
#             font = self.font()
#             font.setPointSize(25)
#             self.setFont(font)

#         def buttonClicked(self, project):
#             subprocess.Popen(["python", "-m", "pyroGamer.Editor"] + ["--projectPath", self.activeProjectPath])

#     class Options(QPushButton):
#         def __init__(self, project):
#             super().__init__()
#             self.setText("⋮")
#             self.clicked.connect(lambda: print("Options"))
#             # hide the button's border
#             self.setStyleSheet(
#                 "QPushButton {"
#                 "    border: none;"
#                 "    text-align: center;"
#                 "    vertical-align: middle;"
#                 "}"
#                 "QPushButton:hover {"
#                 "    color: green;"
#                 "}"
#             )
#             font = self.font()
#             font.setPointSize(25)
#             self.setFont(font)
