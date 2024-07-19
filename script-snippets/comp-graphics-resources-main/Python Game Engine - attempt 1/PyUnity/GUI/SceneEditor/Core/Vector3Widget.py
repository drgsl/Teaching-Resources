import sys
import typing
from PyQt6 import QtCore

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
)
from PyQt6.QtCore import QSize, Qt

class Vector3Widget(QWidget):

    def __init__(self, property_name: str):
        super().__init__()
        layout = QHBoxLayout()

        layout.addWidget(QLabel(property_name))

        layout.addWidget(QLabel("X:"))
        self.x_field = QDoubleSpinBox()
        self.x_field.setMinimum(-100)
        self.x_field.setMaximum(100)
        self.x_field.setSingleStep(0.5)
        self.x_field.setAccelerated(True)
        self.x_field.valueChanged.connect(lambda i: self.value_changed(property_name ,"x", i))
        layout.addWidget(self.x_field)

        layout.addWidget(QLabel("Y:"))
        self.y_field = QDoubleSpinBox()
        self.y_field.setMinimum(-100)
        self.y_field.setMaximum(100)
        self.y_field.setSingleStep(0.5)
        self.y_field.setAccelerated(True)
        self.y_field.valueChanged.connect(lambda i: self.value_changed(property_name ,"y", i))
        layout.addWidget(self.y_field)

        layout.addWidget(QLabel("Z:"))
        self.z_field = QDoubleSpinBox()
        self.z_field.setMinimum(-100)
        self.z_field.setMaximum(100)
        self.z_field.setSingleStep(0.5)
        self.z_field.setAccelerated(True)
        self.z_field.valueChanged.connect(lambda i: self.value_changed(property_name ,"z", i))
        layout.addWidget(self.z_field)

        self.setLayout(layout)


        # self.activeJson = None

    def update(self, go, json):
        # print(json)
        self.activeJson = json
        self.activeGameObject = go
        self.x_field.setValue(json["x"])
        self.y_field.setValue(json["y"])
        self.z_field.setValue(json["z"])
        # print(self.activeGameObject)

    def value_changed(self, label: str, field: str, i: float):

        newJson = self.activeGameObject.__dict__()["Components"]["Transform"]
        newJson[label][field] = i
        
        # print(newJson)

        self.activeGameObject.updateTransform(newJson)





