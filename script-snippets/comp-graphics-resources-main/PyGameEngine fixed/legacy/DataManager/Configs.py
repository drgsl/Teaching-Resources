from PyQt6.QtCore import (
    QSize,
)

import os
import subprocess

import configparser
import json
from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime

from pyroGamer.DataManager.FileManager import FileManager

class HubConfig:
    def GetWindowSize(self):
        fileManager = FileManager()
        configFile = configparser.ConfigParser()
        configFile.read(os.path.join(fileManager.DataFolder, 'Hub.ini'))

        HubSize = QSize()
        HubSize.setWidth(int(configFile['WINDOW_SIZE']['WIDTH']))
        HubSize.setHeight(int(configFile['WINDOW_SIZE']['HEIGHT']))

        data = {
            'HUB_SIZE_QSIZE': HubSize, 
            'HUB_SIZE_INT': [int(HubSize.width()), int(HubSize.height())],  
        }

        return data
    
class EditorConfig:
    def GetWindowsSize(self):
        fileManager = FileManager()
        configFile = configparser.ConfigParser()
        configFile.read(os.path.join(fileManager.DataFolder, 'Editor.ini'))

        EditorSize = QSize()
        EditorSize.setWidth(int(configFile['WINDOW_SIZE']['WIDTH']))
        EditorSize.setHeight(int(configFile['WINDOW_SIZE']['HEIGHT']))

        data = {
            'EDITOR_SIZE_QSIZE': EditorSize, 
            'EDITOR_SIZE_INT': [int(EditorSize.width()), int(EditorSize.height())],  
        }

        return data

class ProjectsConfig(ABC):

    @staticmethod
    def GetProjectsTableConfig():
        configFile = configparser.ConfigParser()
        configFile.read(os.path.join(FileManager().DataFolder, 'Hub.ini'))

        TableSize = QSize()
        TableSize.setWidth(int(configFile['TABLE']['WIDTH']))
        TableSize.setHeight(int(configFile['TABLE']['HEIGHT']))

        TableUnit = configFile['TABLE']['UNIT']

        headers = []
        for header in configFile['TABLE_HEADERS']:
            if configFile['TABLE_HEADERS'][header] == 'Starred':
                headers.append('★')
            elif configFile['TABLE_HEADERS'][header].__contains__("Button"):
                headers.append('')
            else:
                headers.append(configFile['TABLE_HEADERS'][header])

        return {
            'TABLE_SIZE_QSIZE': TableSize,
            'TABLE_SIZE_INT': [int(TableSize.width()), int(TableSize.height())],
            'TABLE_HEADERS': headers,
            'TABLE_UNIT': int(TableUnit),
        }
    
    @abstractmethod
    def isProjectPath(self, path):
        pass

    @abstractmethod
    def AddProject(self, path):
        pass

    # @abstractmethod
    # def GetProjectsTableConfig(self):
    #     pass

    @abstractmethod
    def GetProjectList(self):
        pass

    @abstractmethod
    def GetUnusedID(self):
        pass

    @abstractmethod
    def IDExists(self, ID):
        pass

    @abstractmethod
    def SetID(self, projectID, ID):
        pass

    @abstractmethod
    def SetStar(self, projectID, starred):
        pass

    @abstractmethod
    def SetName(self, projectID, name):
        pass

    @abstractmethod
    def SetPath(self, projectID, path):
        pass

    @abstractmethod
    def SetCreated(self, projectID, lastModified):
        pass

    @abstractmethod
    def SetProjectAttribute(self, projectID, attribute, value):
        pass


class LocalConfig(ProjectsConfig):
    def isProjectPath(path):
        # load json from file path
        with open(path, 'r') as jsonfile:
            projectJSON = json.load(jsonfile)
                
        return (
            projectJSON.__contains__('ID') and
            projectJSON.__contains__('Star') and
            projectJSON.__contains__('Project Name') and
            projectJSON.__contains__('Project Path') and
            projectJSON.__contains__('Created')
        )
    
    def AddEmptyProject(name, path):
        projectPath = LocalConfig.CreateEmptyProject(name, path)
        LocalConfig.AddProject(projectPath)

    def CreateEmptyProject(name, path):
        path = Path(path)
        projectFolder = os.path.join(path, f"{name}")
        os.makedirs(projectFolder, exist_ok=True)

        ProjectFilePath = os.path.join(projectFolder, "Project.json")

        projectJSON = {
            "ID": LocalConfig.GetUnusedID(),
            "Star": False,
            "Project Name": name,
            "Project Path": str(path.resolve()),
            "Created": str(datetime.now().strftime("%d/%m/%Y")),
        }
        print(ProjectFilePath)
        with open(ProjectFilePath, 'w') as jsonfile:
            json.dump(projectJSON, jsonfile)

        directories = [
            os.path.join(projectFolder, "Assets"),
            os.path.join(projectFolder, "Assets", "Art"),
            os.path.join(projectFolder, "Assets", "Art", "2D"),
            os.path.join(projectFolder, "Assets", "Art", "3D"),
            os.path.join(projectFolder, "Assets", "Scenes"),
            os.path.join(projectFolder, "Assets", "Scripts"),
        ]

        # Create the directories
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

        # Create an empty scene
        emptyScene = {
            "ID": 0,
            "Name": "SampleScene",



            "GameObjects": [],
        }
        with open(os.path.join(directories[4], "Scene.json"), 'w') as jsonfile:
            json.dump(emptyScene, jsonfile)

        return ProjectFilePath


    def AddProject(path):
        print(f"Adding {path} to project list...")
        if(not LocalConfig.isProjectPath(path)):
            print(f"{path} is not a valid project path")
            return
        
        project_list_path = os.path.join(FileManager().DataFolder, 'Project_List.json')

        with open(project_list_path, 'r') as jsonfile:
            project_list = json.load(jsonfile)
        
        with open(path, 'r') as jsonfile:
            projectJSON = json.load(jsonfile)

        project_list.append({
            "ID": LocalConfig.GetUnusedID(),
            "Star": projectJSON['Star'],
            "Project Name": projectJSON['Project Name'],
            "Project Path": str(Path(path).resolve()),
            "Created": projectJSON['Created'],
        })

        with open(project_list_path, 'w') as jsonfile:
            json.dump(project_list, jsonfile)
        
    
    def GetProjectList():
        project_list_path = os.path.join(FileManager().DataFolder, 'Project_List.json')

        with open(project_list_path, 'r') as jsonfile:
            project_list = json.load(jsonfile)
        
        return project_list
    
    def GetUnusedID():
        # Return the first unused ID
        project_list = LocalConfig.GetProjectList()

        for i in range(len(project_list) + 1):
            if not LocalConfig.IDExists(i):
                return i
            
    def IDExists(ID):
        project_list = LocalConfig.GetProjectList()

        for project in project_list:
            if project['ID'] == ID:
                return True

        return False

    def SetID(projectID, ID):
        LocalConfig.SetProjectAttribute(projectID, 'ID', ID)

    def SetStar(projectID, starred):
        LocalConfig.SetProjectAttribute(projectID, 'Star', starred)
    
    def SetName(projectID, name):
        LocalConfig.SetProjectAttribute(projectID, 'Project Name', name)

    def SetPath(projectID, path):
        LocalConfig.SetProjectAttribute(projectID, 'Project Path', path)

    def SetCreated(projectID, created):
        LocalConfig.SetProjectAttribute(projectID, 'Created', created)

    def SetProjectAttribute(projectID, attribute, value):
        project_list_path = os.path.join(FileManager().DataFolder, 'Project_List.json')

        with open(project_list_path, 'r') as jsonfile:
            project_list = json.load(jsonfile)

        for project in project_list:
            if project['ID'] == projectID:
                # print(f"Found {project} in project list")
                project[attribute] = value
                break

        with open(project_list_path, 'w') as jsonfile:
            json.dump(project_list, jsonfile)

class CloudConfig(ProjectsConfig):
    pass