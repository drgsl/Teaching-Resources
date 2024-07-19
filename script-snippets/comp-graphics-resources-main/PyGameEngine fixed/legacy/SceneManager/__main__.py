

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

parser = argparse.ArgumentParser(description='Scene Manager Utility')

parser.add_argument('--GetSampleScene', action='store_true', help='Returns an empty scene')

args = parser.parse_args()

if args.GetSampleScene:
    sampleSceneJSON = {
        "ID": -1,
        "Name": "SampleScene",
        "GameObjects": [],
    }
    print(Fore.GREEN + "SampleScene: " + json.dumps(sampleSceneJSON))






