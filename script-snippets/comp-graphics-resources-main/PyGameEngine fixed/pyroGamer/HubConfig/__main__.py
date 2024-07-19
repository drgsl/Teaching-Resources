
import os
import configparser
import argparse
import pprint
import json 


from pyroGamer.HubConfig.FileManager import FileManager

from colorama import Fore, Back, Style, init
init(autoreset=True)


print(Fore.BLACK + Style.BRIGHT + "start HubConfig...")



# TODO: Group the arguments into subcommands
parser = argparse.ArgumentParser(description='HubConfig Utility')
parser.add_argument('--GetWindowSize', action='store_true', help='Get Hub window size')
parser.add_argument('--GetProjectsTableHeaders', action='store_true', help='Get Headers for Projects Table View')

parser.add_argument('--GetProjectListPath', action='store_true', help='Get Path to ProjectList.json')

parser.add_argument('--StarProject', type=int, help='Star a project')
parser.add_argument('--UnstarProject', type=int, help='Unstar a project')

parser.add_argument('--AddExistingProject', type=str, help='Add a project')

subparsers = parser.add_subparsers(title= 'subcommands', dest='command')

add_project_parser = subparsers.add_parser('AddNewProject', help='Add a project')
add_project_parser.add_argument('--name', type=str, help='Name of the project')
add_project_parser.add_argument('--path', type=str, help='Path to the project')
args = parser.parse_args()



if args.GetWindowSize:
    window_size = FileManager.GetHubWindowSize()
    print("HubWindowSize: " + json.dumps(window_size))

if args.GetProjectListPath:
    project_list_path = FileManager.GetProjectListPath()
    print("ProjectListPath: " + project_list_path)

if args.GetProjectsTableHeaders:
    projects_table_headers = FileManager.GetProjectsTableHeaders()
    print("ProjectsTableHeaders: " + json.dumps(projects_table_headers))

if(args.StarProject != None):
    projectID = args.StarProject
    FileManager.SetProjectAttribute(projectID, "StarButton", True)

if(args.UnstarProject != None):
    projectID = args.UnstarProject
    FileManager.SetProjectAttribute(projectID, "StarButton", False)

if(args.AddExistingProject != None):
    projectPath = args.AddExistingProject
    FileManager.AddExistingProject(projectPath)

if args.command == 'AddNewProject':
    emptyProjectPath = FileManager.CreateEmptyProject(args.name, args.path)
    FileManager.AddExistingProject(emptyProjectPath)
