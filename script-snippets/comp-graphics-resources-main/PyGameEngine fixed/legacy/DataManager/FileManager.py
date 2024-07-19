import os
import subprocess

import configparser
import json

class FileManager:
    def __init__(self):
        # print("File Manager initialized")
        #TODO: Make so this doesnt instatiate so many times
        self.DocumentsFolder = self.getDocumentsFolder()
        self.DataFolder = os.path.join(self.DocumentsFolder, "pyroGamer")
        os.makedirs(self.DataFolder, exist_ok=True)

        self.init_config_files()
        self.init_project_list()

    def getDocumentsFolder(self):
        if os.name == 'posix':  # Unix/Linux/MacOS
            try:
                documents_dir = subprocess.check_output(["xdg-user-dir", "DOCUMENTS"]).strip().decode("utf-8")
                if os.path.isdir(documents_dir):
                    return documents_dir
            except FileNotFoundError:
                return os.path.expanduser('~/Documents')
                pass  # xdg-user-dir may not be available on all systems
        elif os.name == 'nt':  # Windows
            return os.path.expanduser('~/Documents')
        else:
            raise NotImplementedError("Platform not supported")
    
    def init_config_files(self):
        hub_config_path = os.path.join(self.DataFolder, 'Hub.ini')
        editor_config_path = os.path.join(self.DataFolder, 'Editor.ini')

        # if not os.path.exists(hub_config_path):
        self.create_default_hub_config(hub_config_path)

        # if not os.path.exists(editor_config_path):
        self.create_default_editor_config(editor_config_path)

    def create_default_hub_config(self, path):
        # print(f"Created {path}")
        config = configparser.ConfigParser()
        config['WINDOW_SIZE'] = {
            'WIDTH': 550,
            'HEIGHT': 350,
        }
        config ['MAIN_WIDGET_OFFSET'] = {
            'X': 10,
            'Y': 10,
        }

        config ['TABLE'] = {
            'WIDTH': 540,
            'HEIGHT': 320,
            'UNIT': 25,
        }

        config ['TABLE_HEADERS'] = {
            'Field1': 'Starred',
            'Field2': 'Name',
            'Field3': 'Path',
            'Field4': 'Created',
            'Field5': 'PlayButton',
            'Field6': 'SettingsButton',
        }

        with open(path, 'w') as configfile:
            config.write(configfile)
        
    def init_project_list(self):
        project_list_path = os.path.join(self.DataFolder, 'Project_List.json')

        if not os.path.exists(project_list_path):
            self.create_default_project_list(project_list_path)

    def create_default_project_list(self, path):
        # print(f"Created {path}")

        default_project_list = []
        # [
        #     {
        #         "ID": 0,
        #         "Star": False, 
        #         "Project Name": "SampleProject 1", 
        #         "Project Path": "C:/Users/Pyro/Desktop/Projects/Project 1",
        #         "Last Modified": "2021-10-10",
        #     },
        #     {
        #         "ID": 1,
        #         "Star": False,
        #         "Project Name": "SampleProject 2",
        #         "Project Path": "C:/Users/Pyro/Desktop/Projects/Project 2",
        #         "Last Modified": "2021-10-10",
        #     },
        # ]

        with open(path, 'w') as jsonfile:
            json.dump(default_project_list, jsonfile)

    def create_default_editor_config(self, path):
        config = configparser.ConfigParser()
        config['WINDOW_SIZE'] = {
            'Width': 1600,
            'Height': 900,
        }

        with open(path, 'w') as configfile:
            config.write(configfile)

