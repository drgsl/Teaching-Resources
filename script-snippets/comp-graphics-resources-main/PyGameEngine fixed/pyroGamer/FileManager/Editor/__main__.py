


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
print(Fore.BLACK + Style.BRIGHT + "start pyroGamer.FileManager.Editor ...")



parser = argparse.ArgumentParser(description='FileManager Utility')

subparsers = parser.add_subparsers(title= 'subcommands', dest='command')
isProjectPath = subparsers.add_parser('isValidProject', help='Check if path points to a valid project')
isProjectPath.add_argument('--path', type=Path, required=True, help='Path to the project')

createProject = subparsers.add_parser('createProject', help='Create a new project')
createProject.add_argument('--name', type=str, required=True, help='Name of the project')
createProject.add_argument('--path', type=Path, required=True, help='Path to the project')

getActiveScene = subparsers.add_parser('getLatestSavedScene', help='Active Scene Getter/Setter')
getActiveScene.add_argument('--projectPath', type=Path,required=True, help='Get the active scene')


args = parser.parse_args()

if args.command == "isValidProject":
    if args.path:
        isValid = False
        if Path(args.path).is_file():
            with open(args.path, 'r') as jsonfile:
                project_data = json.load(jsonfile)
            
            isValid = (
                project_data.__contains__("ID") and
                project_data.__contains__("Name") and 
                project_data.__contains__("Scenes")
            )
        elif Path(args.path).is_dir():
            project_data_path = os.path.join(args.path, "ProjectData.json")

            if Path(project_data_path).is_file():
                with open(project_data_path, 'r') as jsonfile:
                    project_data = json.load(jsonfile)
                
                isValid = (
                    project_data.__contains__("ID") and
                    project_data.__contains__("Name") and 
                    project_data.__contains__("Scenes")
                )

        print("isValidProject: " + str(isValid))



if args.command == "createProject":
    if args.name and args.path:
        projectPath = os.path.join(args.path, args.name)
        projectPath = Path(projectPath).as_posix()

        directories = [
            os.path.join(projectPath, "Assets"),
            os.path.join(projectPath, "Assets", "Art"),
            os.path.join(projectPath, "Assets", "Art", "2D"),
            os.path.join(projectPath, "Assets", "Art", "3D"),
            os.path.join(projectPath, "Assets", "Scenes"),
            os.path.join(projectPath, "Assets", "Scripts"),
        ]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

        result = subprocess.run(['python', '-m', 'pyroGamer.Editor.SceneManager',
                                'GetEmptyScene'], 
                                capture_output=True, text=True)
        if result.returncode != 0:
            print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
            print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
            sys.exit(1)
        for line in result.stdout.splitlines():
            if line.startswith("EmptyScene: "):
                sceneData = line.replace("EmptyScene: ", "")
                emptyScene = json.loads(sceneData)

        emptyScene["ID"] = 0

        scenesFolderPath = Path(os.path.join(projectPath, "Assets", "Scenes")).as_posix()
        scenePath = Path(os.path.join(scenesFolderPath, f'{emptyScene["Name"]}.json')).as_posix()


        with open(scenePath, 'w') as jsonfile:
            json.dump(emptyScene, jsonfile)


        projectJSON = {
            "ID": -1,
            "Name": args.name,
            "Scenes": [emptyScene],
        }

        ProjectDataPath = os.path.join(projectPath, "ProjectData.json")
        ProjectDataPath = Path(ProjectDataPath).as_posix()

        with open(ProjectDataPath, 'w') as jsonfile:
            json.dump(projectJSON, jsonfile)


if args.command == "getLatestSavedScene":
    if args.projectPath:
        projectPath = args.projectPath
        if not Path(projectPath).is_dir():
            projectPath = Path(projectPath).parent

        scenesFolderPath = Path(os.path.join(projectPath, "Assets", "Scenes")).as_posix()

        scenes = []
        for file in os.listdir(scenesFolderPath):
            if file.endswith(".json"):
                scenes.append(os.path.join(scenesFolderPath, file))

        latestFilePath = max(scenes, key=os.path.getctime)
        latestFilePath = Path(latestFilePath).as_posix()

        print("LatestSavedScene: " + latestFilePath)
