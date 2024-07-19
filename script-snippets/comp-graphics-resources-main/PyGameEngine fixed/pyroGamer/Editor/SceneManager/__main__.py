


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
print(Fore.BLACK + Style.BRIGHT + "start pyroGamer.Editor.SceneManager ...")


parser = argparse.ArgumentParser(description='Scene Manager Utility')
subparsers = parser.add_subparsers(title= 'subcommands', dest='command')
GetEmptyScene_parser = subparsers.add_parser('GetEmptyScene', help='Get a sample scene')


args = parser.parse_args()

if args.command == "GetEmptyScene":

    defaultGameObject = {
        "ID": "-1",
        "Name": "EmptyGameObject",
        "Components": []
    }

    defaultGameObject["ID"] = "0"

    emptyScene = {
        "ID": "-1",
        "Name": "SampleScene",
        "GameObjects": [defaultGameObject]
    }


    print(f"EmptyScene: {json.dumps(emptyScene)}")