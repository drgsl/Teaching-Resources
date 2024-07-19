from pathlib import Path
import ast
import os
import configparser
import json
from colorama import Fore, Back, Style, init
init(autoreset=True)


class FileManager():
    DocumentsFolder_Path = ""
    DataFolder_Path = ""

    HubConfig_Path = ""
    ProjectsList_Path = ""

    @staticmethod
    def CreateEmptyProject(name, path):
        # path.mkdir(parents=True, exist_ok=True)

        directories = [
            os.path.join(path, name),
            os.path.join(path, name, "Assets"),
            os.path.join(path, name, "Assets", "Art"),
            os.path.join(path, name, "Assets", "Art", "2D"),
            os.path.join(path, name, "Assets", "Art", "3D"),
            os.path.join(path, name, "Assets", "Scenes"),
            os.path.join(path, name, "Assets", "Scripts"),
        ]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)


        projectJSON = {
            "ID": -1,
            "StarButton": False,
            "Name": name,
            "Path": str(Path(path).as_posix()),
        }

        ProjectFilePath = os.path.join(path, name, "Project.json")

        with open(ProjectFilePath, 'w') as jsonfile:
            json.dump(projectJSON, jsonfile)

        # TODO: Create empty scene

        return ProjectFilePath

    @staticmethod
    def AddExistingProject(path):
        FileManager.__init__()

        def GetUnusedID():
            def IDExists(ID):
                with open(FileManager.ProjectsList_Path, 'r') as jsonfile:
                    project_list = json.load(jsonfile)

                for project in project_list:
                    if project['ID'] == ID:
                        return True

                return False
            # Return the first unused ID
            with open(FileManager.ProjectsList_Path, 'r') as jsonfile:
                project_list = json.load(jsonfile)

            for i in range(len(project_list) + 1):
                if not IDExists(i):
                    return i
                

        if(not FileManager.isProjectPath(path)):
            print(Fore.RED + f"{path} is not a valid project path")
            quit()

        with open(FileManager.ProjectsList_Path, 'r') as jsonfile:
            project_list = json.load(jsonfile)
        
        with open(path, 'r') as jsonfile:
            projectJSON = json.load(jsonfile)

        project = {
            "ID": GetUnusedID(),
            "StarButton": projectJSON['StarButton'],
            "Name": projectJSON['Name'],
            "Path": Path(path).as_posix(),
        }

        project_list.append(project)

        with open(FileManager.ProjectsList_Path, 'w') as jsonfile:
            json.dump(project_list, jsonfile)

        with open(project['Path'], 'w') as jsonfile:
            json.dump(project, jsonfile)

    @staticmethod
    def isProjectPath(projectPath):
        with open(projectPath, 'r') as jsonfile:
            projectJSON = json.load(jsonfile)

        return {
            projectJSON.__contains__('ID'),
            projectJSON.__contains__('StarButton'),
            projectJSON.__contains__('Name'),
            projectJSON.__contains__('Path'),
        }

    @staticmethod
    def SetProjectAttribute(projectID, attribute, value):
        project_list_path = FileManager.GetProjectListPath()

        with open(project_list_path, 'r') as jsonfile:
            project_list = json.load(jsonfile)

        for project in project_list:
            if project['ID'] == projectID:
                # print(f"Found {project} in project list")
                project[attribute] = value
                break

        with open(project['Path'], 'w') as jsonfile:
            json.dump(project, jsonfile)

        with open(project_list_path, 'w') as jsonfile:
            json.dump(project_list, jsonfile)


    @staticmethod
    def GetProjectListPath():
        FileManager.__init__()
        return FileManager.ProjectsList_Path

    @staticmethod
    def GetHubWindowSize():
        FileManager.__init__()

        configFile = configparser.ConfigParser()
        configFile.read(os.path.join(FileManager.DataFolder_Path, 'Hub.ini'))

        HubSize = {
            'WIDTH': 0,
            'HEIGHT': 0,
        }
        HubSize['WIDTH'] = int(configFile['WINDOW_SIZE']['WIDTH'])
        HubSize['HEIGHT'] = int(configFile['WINDOW_SIZE']['HEIGHT'])

        return HubSize
    
    @staticmethod
    def GetProjectsTableHeaders():
        FileManager.__init__()

        configFile = configparser.ConfigParser()
        configFile.read(os.path.join(FileManager.DataFolder_Path, 'Hub.ini'))


        return ast.literal_eval(configFile['PROJECTS_TABLE']['HEADERS'])    
    
    

    def __init__():
        print(Fore.BLACK + Style.BRIGHT + "init FileManager...")

        if(FileManager.DocumentsFolder_Path == ""):
            print("Setting DocumentsFolder_Path...")
            FileManager.DocumentsFolder_Path = os.path.expanduser('~/Documents')
            FileManager.DocumentsFolder_Path = Path(FileManager.DocumentsFolder_Path).as_posix()
        if(FileManager.DataFolder_Path == ""):
            print("Setting DataFolder_Path...")
            FileManager.DataFolder_Path = os.path.join(FileManager.DocumentsFolder_Path, "pyroGamer_Data")
            FileManager.DataFolder_Path = Path(FileManager.DataFolder_Path).as_posix()
            os.makedirs(FileManager.DataFolder_Path, exist_ok=True)
        if(not FileManager.HubConfig_Path):
            print("Setting HubConfig_Path...")
            FileManager.HubConfig_Path = os.path.join(FileManager.DataFolder_Path, 'Hub.ini')
            FileManager.HubConfig_Path = Path(FileManager.HubConfig_Path).as_posix()
        if(not FileManager.ProjectsList_Path):
            print("Setting ProjectsList_Path...")
            FileManager.ProjectsList_Path = os.path.join(FileManager.DataFolder_Path, 'ProjectList.json')
            FileManager.ProjectsList_Path = Path(FileManager.ProjectsList_Path).as_posix()

        if(not os.path.exists(FileManager.HubConfig_Path)):
            config = configparser.ConfigParser()
            config['WINDOW_SIZE'] = {
                'WIDTH': 550,
                'HEIGHT': 350,
            }
            config['PROJECTS_TABLE'] = {
                'HEADERS': [ 'StarButton', 'Name', 'Path', 'PlayButton'],
            }
            with open(FileManager.HubConfig_Path, 'w') as configfile:
                config.write(configfile)
            print(Fore.YELLOW + "Created HubConfig.ini because it didn't exist.")

        if(not os.path.exists(FileManager.ProjectsList_Path)):
            with open(FileManager.ProjectsList_Path, 'w') as f:
                f.write("[]")
            print(Fore.YELLOW + "Created ProjectList.json because it didn't exist.")
