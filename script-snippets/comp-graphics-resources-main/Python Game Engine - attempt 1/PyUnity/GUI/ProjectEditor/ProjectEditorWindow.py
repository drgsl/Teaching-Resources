import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

#     """
#     This "window" is a QWidget. If it has no parent,
#     it will appear as a free-floating window.
#     """

class ProjectEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel("Project Editor Window")
        layout.addWidget(self.label)

        mainWidget = QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)


app = QApplication(sys.argv)
mainWindow = ProjectEditorWindow()
mainWindow.show()
app.exec()
