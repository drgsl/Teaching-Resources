

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



def GetTempFilePath():
    result = subprocess.run(['python', '-m', 'pyroGamer.ActiveProjectManager.FileManager',
                            '--GetDataFolder'],
                            capture_output=True, text=True)
    print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
    if(result.returncode != 0):
        print(Fore.RED + "Error: " + result.stderr)
        sys.exit(1)
    for line in result.stdout.splitlines():
        if(line.startswith("DataFolderPath: ")):
            return line[16:]    






ActiveProjectPath = None

parser = argparse.ArgumentParser(description='Project Manager Utility')


parser.add_argument('--SetProjectPath', type=str, help='Set the project path')
parser.add_argument('--GetProjectPath', action='store_true', help='Get the project path (if it exists)')

parser.add_argument('--GetScenesFolderPath', action='store_true', help='Get the Scenes folder path of the active project')

args = parser.parse_args()

if args.SetProjectPath:

    def GetSampleScene():
        result = subprocess.run(['python', '-m', 'pyroGamer.SceneManager', '--GetSampleScene'],
                                capture_output=True, text=True)
        if(result.returncode != 0):
            print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
            print(Fore.RED + "Error: " + result.stderr)
            sys.exit(1)
        for line in result.stdout.splitlines():
            if(line.startswith("SampleScene:")):
                sampleSceneJSON = ast.literal_eval(line[12:])
                print(Fore.GREEN + "SampleScene: " + json.dumps(sampleSceneJSON))
        return sampleSceneJSON
    
    ActiveProjectPath = args.SetProjectPath
    print(Fore.GREEN + f"ActiveProjectPath: {ActiveProjectPath}")

    tempFilePath = os.path.join(GetTempFilePath(), "ActiveProjectPath.tmp")

    with open(tempFilePath, "w") as tempFile:
        tempFile.write(ActiveProjectPath)

    sampleSceneJSON = GetSampleScene()

    result = subprocess.run(['python', '-m', 'pyroGamer.ActiveProjectManager.FileManager', 
                             'SaveScene', '--sceneJSON', json.dumps(sampleSceneJSON)],
                            capture_output=True, text=True)
    
    print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))    
    if(result.returncode != 0):
        print(Fore.RED + "Error: " + result.stderr)
        sys.exit(1)
    


    

if args.GetProjectPath:
    if ActiveProjectPath == None:
        tempFilePath = os.path.join(GetTempFilePath(), "ActiveProjectPath.tmp")
        if os.path.exists(tempFilePath):
            with open(tempFilePath, "r") as tempFile:
                ActiveProjectPath = tempFile.read()
                print(Fore.GREEN + f"ActiveProjectPath: {ActiveProjectPath}")
        else:
            print(Fore.RED + "Error: No active project path")
            sys.exit(1)
    else:
        print(Fore.GREEN + f"ActiveProjectPath: {ActiveProjectPath}")

if args.GetScenesFolderPath:
    if ActiveProjectPath == None:
        result = subprocess.run(['python', '-m', 'pyroGamer.ActiveProjectManager',
                                  '--GetProjectPath'],
                                capture_output=True, text=True)
        print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
        if(result.returncode != 0):
            print(Fore.RED + "Error: " + result.stderr)
            sys.exit(1)
        for line in result.stdout.splitlines():
            if(line.startswith("ActiveProjectPath: ")):
                ActiveProjectPath = line[19:]
                print(Fore.GREEN + f"ActiveProjectPath: {ActiveProjectPath}")
    if ActiveProjectPath != None:
        ProjectFolder = Path(ActiveProjectPath).parent.as_posix()
        ScenesFolderPath = os.path.join(ProjectFolder, "Assets", "Scenes")
        ScenesFolderPath = Path(ScenesFolderPath).as_posix()
        print(Fore.GREEN + f"ScenesFolderPath: {ScenesFolderPath}")






