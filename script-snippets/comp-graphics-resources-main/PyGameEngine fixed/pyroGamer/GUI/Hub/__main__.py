import sys

from PyQt6.QtCore import (
    QSize, Qt,
    QSortFilterProxyModel,
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QTabWidget, 
    QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit,
    QGridLayout, QVBoxLayout, QHBoxLayout,
)

from pyroGamer.Hub.Tabs import LocalTab

import pprint
import textwrap
import json
import subprocess
import argparse
from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.BLACK + Style.BRIGHT + "start pyroGamer.Hub...")

parser = argparse.ArgumentParser(description='Hub Utility')
parser.add_argument('--SetWindowSize', action='store_true', help='Set Hub window size')
parser.add_argument('--width', type=int, help='Set Hub window width')
parser.add_argument('--height', type=int, help='Set Hub window height')



class HubWindow(QMainWindow):
    WindowSize = None

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Hub")

        args = parser.parse_args()

        if args.SetWindowSize:
            print(Fore.BLUE + "Received Hub window size from cli")
            if args.width and args.height:
                print(Fore.GREEN + "Setting Hub window size to " + str(args.width) + "x" + str(args.height))
                HubWindow.WindowSize = QSize(args.width, args.height)
            else:
                print(Fore.RED + "Error: --width and --height are required when using --SetWindowSize")
                sys.exit(1)
        else:
            print(Fore.BLUE + "Instantiating " + "pyroGamer.HubConfig" + " to get Hub window size...")
            result = subprocess.run(['python', '-m', 'pyroGamer.HubConfig', '--GetWindowSize'], capture_output=True, text=True)

            if result.returncode != 0:
                print(Fore.LIGHTBLACK_EX + textwrap.indent(pprint.pformat(result.stdout), '>'))
                print(Fore.RED + Style.BRIGHT + "Error: " + str(result.stderr))
                sys.exit(1)

            for line in result.stdout.splitlines():
                if line.startswith("HubWindowSize:"):
                    windowSize_data = line.replace("HubWindowSize: ", "")
                    windowSize_data = json.loads(windowSize_data)

                    HubWindow.WindowSize = QSize()
                    HubWindow.WindowSize.setWidth(int(windowSize_data["WIDTH"]))
                    HubWindow.WindowSize.setHeight(int(windowSize_data["HEIGHT"]))

                    print(Fore.GREEN + "Received HubWindowSize: " + 
                          str(HubWindow.WindowSize.width()) + "x" + 
                          str(HubWindow.WindowSize.height()))


        self.setFixedSize(HubWindow.WindowSize)

        layout = QVBoxLayout()

        Tabs_Widget = QTabWidget()

        Tabs_Widget.addTab(LocalTab(), "Local Projects")
        # Tabs_Widget.addTab(Cloud(), "Cloud Projects")
        Tabs_Widget.tabBar().setMovable(True)

        layout.addWidget(Tabs_Widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = HubWindow()
window.show()

app.exec()
