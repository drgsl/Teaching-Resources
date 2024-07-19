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
    QStackedLayout,
    QStatusBar,
    QToolBar,
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import QSize

from PyQt6.QtOpenGLWidgets import QOpenGLWidget

from OpenGL.GL import *
from OpenGL.GLU import *

class SceneView(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500, 500))
        self.mainLayout = QVBoxLayout()
        titleWidget = QLabel("Scene View")
        titleWidget.setFixedSize(QSize(500, 20))
        self.mainLayout.addWidget(titleWidget)

        self.openGLWidget = QOpenGLWidget()
        self.mainLayout.addWidget(self.openGLWidget)

        self.setLayout(self.mainLayout)



class OpenGLCanvas(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glRotatef(1, 3, 1, 1)
        # mesh = Model("Assets/Cube.obj")
        # mesh.renderWireframe()

app = QApplication(sys.argv)
mainWindow = SceneView()
# mainWindow.hide()
# app.exec()
