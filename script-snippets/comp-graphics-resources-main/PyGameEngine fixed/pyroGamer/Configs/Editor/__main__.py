
import os
import configparser
import argparse
import pprint
import json 


from pyroGamer.Configs.Editor.FileManager import FileManager

from colorama import Fore, Back, Style, init
init(autoreset=True)


print(Fore.BLACK + Style.BRIGHT + "start EditorConfig...")



parser = argparse.ArgumentParser(description='EditorConfig Utility')
parser.add_argument('--GetWindowSize', action='store_true', help='Get Editor window size')

args = parser.parse_args()



if args.GetWindowSize:
    window_size = FileManager.GetEditorWindowSize()
    print("EditorWindowSize: " + json.dumps(window_size))