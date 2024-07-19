import sys
from random import randint

from SceneEditor.SceneEditorWindow import SceneEditorWindow
from ProjectEditor.ProjectEditorWindow import ProjectEditorWindow

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sceneWindow = SceneEditorWindow()
        self.projectWindow = ProjectEditorWindow()

        mainLayout = QVBoxLayout()
        toggleSceneButton = QPushButton("Toggle Scene Editor")
        toggleSceneButton.clicked.connect(
            lambda checked: self.toggle_window(self.sceneWindow)
        )
        mainLayout.addWidget(toggleSceneButton)

        toggleProjectButton = QPushButton("Toggle Project Editor")
        toggleProjectButton.clicked.connect(
            lambda checked: self.toggle_window(self.projectWindow)
        )
        mainLayout.addWidget(toggleProjectButton)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


if __name__ == "__main__":
    print("bruh")
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
