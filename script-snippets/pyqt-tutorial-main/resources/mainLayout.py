import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import QSize, Qt

from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QDial, QProgressBar,
    QPushButton, QRadioButton, QButtonGroup
)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Python Game Engine")
        self.setFixedSize(QSize(1500, 750)) # TODO: Make this dynamic

        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(20)

        
        # Left side
        HierarchyLayout = QVBoxLayout()
        HierarchyLayout.addWidget(QLabel("Hierarchy"))
        HierarchyLayout.addWidget(QPushButton("New Game Object"))
        # add a list of all the gameobjects in scene
        HierarchyLayout.addWidget(Color("red"))
        
        mainLayout.addLayout(HierarchyLayout)

        # Middle side
        MiddleLayout = QVBoxLayout()
        SceneViewLayout = QHBoxLayout()
        SceneViewLayout.addWidget(QLabel("Scene View"))
        AssetsFolderLayout = QHBoxLayout()
        AssetsFolderLayout.addWidget(QLabel("Assets Folder"))

        MiddleLayout.addLayout(SceneViewLayout)
        MiddleLayout.addLayout(AssetsFolderLayout)

        mainLayout.addLayout(MiddleLayout)

        # Right side
        InspectorLayout = QVBoxLayout()
        InspectorLayout.addWidget(QLabel("Inspector"))
        InspectorLayout.addWidget(QLabel("Transform Component"))
        InspectorLayout.addWidget(QPushButton("Add Component"))

        mainLayout.addLayout(InspectorLayout)



        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()