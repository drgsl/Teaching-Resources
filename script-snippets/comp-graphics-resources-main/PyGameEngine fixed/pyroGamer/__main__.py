
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtCore import QTimer, QSize, Qt


import subprocess
import sys
import json
import pprint

import textwrap
from termcolor import colored
from colorama import Fore, Back, Style, init
init(autoreset=True)


print(Fore.BLACK + Style.BRIGHT + "start pyroGamer...")


def splash_ended():
    # def GetHubWindowSize():
    #     result = subprocess.run(['python', '-m', 'pyroGamer.HubConfig', '--GetWindowSize'], capture_output=True, text=True, check=True)
    #     # print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))

    #     if result.returncode != 0:
    #         print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
    #         sys.exit(1)

    #     for line in result.stdout.splitlines():
    #         if line.startswith("HubWindowSize:"):

    #             windowSize_data = line.replace("HubWindowSize: ", "")
    #             windowSize_data = json.loads(windowSize_data)

    #             HubWindowSize = QSize()
    #             HubWindowSize.setWidth(int(windowSize_data["WIDTH"]))
    #             HubWindowSize.setHeight(int(windowSize_data["HEIGHT"]))

    #     print(Fore.GREEN + Style.BRIGHT + "Received HubWindowSize: " + str(HubWindowSize))
    #     return HubWindowSize
    
    # def GetProjectListPath():
    #     result = subprocess.run(['python', '-m', 'pyroGamer.HubConfig', '--GetProjectListPath'], capture_output=True, text=True, check=True)

    #     # print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout, width=100), '>'))

    #     if result.returncode != 0:
    #         print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
    #         sys.exit(1)

    #     for line in result.stdout.splitlines():
    #         if line.startswith("ProjectListPath:"):

    #             ProjectListPath = line.replace("ProjectListPath: ", "")

    #     print(Fore.GREEN + Style.BRIGHT + "Received ProjectListPath: " + str(ProjectListPath))
    #     return ProjectListPath
    
    # 

    splash.close()
    subprocess.run(["python", "-m", "pyroGamer.Hub",
                    # "--SetWindowSize", 
                    #     "--width", str(HubWindowSize.width()), 
                    #     "--height", str(HubWindowSize.height()),
                    # "--SetProjectListPath", 
                    #     "--localPath", ProjectListPath,
                    #     # "--cloudPath", str(CloudProjectListPath),
                    # "--SetProjectsTableHeaders", 
                    #     "--headers", str(ProjectsTableHeaders)
                    ])
    sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashImage = QPixmap('splash.jpg')
    splashImage = splashImage.scaled(QSize(250, 250), Qt.AspectRatioMode.KeepAspectRatio)
    
    splash = QSplashScreen(splashImage)
    splash.show()

    QTimer.singleShot(250, splash_ended)
    app.exec()


