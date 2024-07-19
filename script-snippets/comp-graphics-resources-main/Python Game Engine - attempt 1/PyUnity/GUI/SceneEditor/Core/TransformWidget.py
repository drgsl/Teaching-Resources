import sys

from PyQt6.QtCore import Qt
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
    QDoubleSpinBox,
    QLineEdit,
)
from PyQt6.QtCore import QSize, Qt

from SceneEditor.Core.Vector3Widget import Vector3Widget

class TransformWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)
        mainLayout = QVBoxLayout()    
        
        self.nameEdit = QLineEdit()
        self.nameEdit.returnPressed.connect(lambda: self.name_Edited(self.nameEdit.text()))
        mainLayout.addWidget(self.nameEdit)

        title = QLabel("Transform")
        mainLayout.addWidget(title)

        self.PositionWidget = Vector3Widget("Position")
        self.RotationWidget = Vector3Widget("Rotation")
        self.ScaleWidget = Vector3Widget("Scale")

        mainLayout.addWidget(self.PositionWidget)
        mainLayout.addWidget(self.RotationWidget)
        mainLayout.addWidget(self.ScaleWidget)

        self.setLayout(mainLayout)

    def updateTransform(self, go, transform = None):
        if transform == None:
            transform = go.__dict__()["Components"]["Transform"]
        self.PositionWidget.update(go, transform["Position"])
        self.RotationWidget.update(go, transform["Rotation"])
        self.ScaleWidget.update(go, transform["Scale"])

        self.nameEdit.setText(go.name)
        self.activeGameObject = go


    def name_Edited(self, newName):
        self.activeGameObject.updateName(newName)
        

app = QApplication(sys.argv)
mainWindow = TransformWidget()
# mainWindow.hide()
# app.exec()
