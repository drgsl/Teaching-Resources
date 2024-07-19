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

    EditorConfig_Path = ""

    def GetEditorWindowSize():
        FileManager.__init__()

        config = configparser.ConfigParser()
        config.read(FileManager.EditorConfig_Path)

        window_size = ast.literal_eval(config['Editor']['WindowSize'])

        return window_size
    

    def __init__():
        print(Fore.BLACK + Style.BRIGHT + "init FileManager...")

        if(FileManager.DocumentsFolder_Path == ""):
            print("Setting DocumentsFolder_Path...")
            FileManager.DocumentsFolder_Path = os.path.expanduser('~/Documents')
        if(FileManager.DataFolder_Path == ""):
            print("Setting DataFolder_Path...")
            FileManager.DataFolder_Path = os.path.join(FileManager.DocumentsFolder_Path, "pyroGamer_Data")
            os.makedirs(FileManager.DataFolder_Path, exist_ok=True)
        if(not FileManager.EditorConfig_Path):
            print("Setting EditorConfig_Path...")
            FileManager.EditorConfig_Path = os.path.join(FileManager.DataFolder_Path, 'Editor.ini')
        
        if(not os.path.exists(FileManager.EditorConfig_Path)):
            config = configparser.ConfigParser()
            config['Editor'] = {
                'WindowSize': [ 1600, 900 ],
            }
            with open(FileManager.EditorConfig_Path, 'w') as configfile:
                config.write(configfile)
        