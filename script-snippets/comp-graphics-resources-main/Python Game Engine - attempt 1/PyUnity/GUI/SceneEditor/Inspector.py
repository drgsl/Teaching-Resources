import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea,
    QSpacerItem,
    QLineEdit,
)
from PyQt6.QtCore import QSize, Qt


from SceneEditor.Core.TransformWidget import TransformWidget


class Inspector(QWidget):
    
    transformWidget = TransformWidget()

    def __init__(self):
        super().__init__()
        
        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(QLabel("Inspector"), 0, 0)

        self.ScrollArea = QScrollArea()
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ScrollArea.setWidgetResizable(True)

        self.Components_Widget = QWidget()
        self.Components_GridLayout = QGridLayout()
        self.Components_GridLayout.RowCount = 5
        self.Components_Widget.setLayout(self.Components_GridLayout)
        self.ScrollArea.setWidget(self.Components_Widget)

        self.Components_GridLayout.addWidget(self.transformWidget)
        self.mainLayout.addWidget(self.ScrollArea, 1, 0)
        self.setLayout(self.mainLayout)

    @staticmethod
    def showGameObject(go):
        for component in go.__dict__()["Components"]:
            if component == 'Transform':
                Inspector.transformWidget.updateTransform(go)




app = QApplication(sys.argv)
mainWindow = Inspector()
# mainWindow.hide()
# app.exec()
