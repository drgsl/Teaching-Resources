

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



parser = argparse.ArgumentParser(description='Project Manager Utility')

parser.add_argument('--GetDataFolder', action='store_true', help='Get the Documents/Data folder path')

subparsers = parser.add_subparsers(title= 'subcommands', dest='command')

saveSceneParser = subparsers.add_parser('SaveScene', help='Save a given scene to the Assets/Scenes folder')
# saveSceneParser.add_argument('--sceneName', type=str, help='Scene Name to save')
saveSceneParser.add_argument('--sceneJSON', type=str, help='Scene JSON to save') 


args = parser.parse_args()

if args.GetDataFolder:
    DocumentsFolderPath = Path(os.path.expanduser('~/Documents')).as_posix()
    DataFolderPath = Path(os.path.join(DocumentsFolderPath, "pyroGamer_Data")).as_posix()
    
    os.makedirs(DataFolderPath, exist_ok=True)
    print(Fore.GREEN + f"DataFolderPath: {DataFolderPath}")

if args.command == 'SaveScene':
    if args.sceneJSON == None:
        print(Fore.RED + "Error: No sceneJSON specified")
        sys.exit(1)
    
    sceneJSON = json.loads(args.sceneJSON)

    def GetProjectPath():
        result = subprocess.run(['python', '-m', 'pyroGamer.ActiveProjectManager', '--GetProjectPath'],
                                capture_output=True, text=True)
        print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
        if(result.returncode != 0):
            print(Fore.RED + "Error: " + result.stderr)
            sys.exit(1)
        for line in result.stdout.splitlines():
            if(line.startswith("ActiveProjectPath: ")):
                return line[19:]
            
    def GetScenesFolderPath():
        result = subprocess.run(['python', '-m', 'pyroGamer.ActiveProjectManager', '--GetScenesFolderPath'],
                                capture_output=True, text=True)
        print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
        if(result.returncode != 0):
            print(Fore.RED + "Error: " + result.stderr)
            sys.exit(1)
        for line in result.stdout.splitlines():
            if(line.startswith("ScenesFolderPath: ")):
                return line[18:]
            
    newScenePath = os.path.join(GetScenesFolderPath(), f"{sceneJSON['Name']}.json")
    newScenePath = Path(newScenePath).as_posix()

    with open(newScenePath, "w") as sceneFile:
        json.dump(sceneJSON, sceneFile, indent=4)

    print(Fore.GREEN + f"Saved {sceneJSON['Name']} to: {newScenePath}")






