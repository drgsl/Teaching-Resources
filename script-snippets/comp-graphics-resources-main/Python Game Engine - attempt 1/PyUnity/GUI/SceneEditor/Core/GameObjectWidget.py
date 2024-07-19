import json

from PyQt6.QtGui import (
    QAction,
    QKeySequence,
)

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
    QMenu,
    QCheckBox,
    QStackedLayout,
    QLineEdit,
)
from PyQt6.QtCore import (
    QSize, 
    Qt, 
    QEvent,
)

from SceneEditor.Inspector import Inspector

class GameObjectWidget(QWidget):

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # hierarchyParent = self.parent().parent().parent().parent()
            # hierarchyParent.selectGameObject(self.gameObject)
            Inspector.showGameObject(go=self.gameObject)

    def __init__(self, go):
        super().__init__()
        self.setFixedSize(200, 50)
        self.setStyleSheet("")

        self.gameObject = go

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(QCheckBox())

        self.nameLayout = QStackedLayout();
        self.nameLabel = QLabel(self.gameObject.name)
        self.nameLayout.addWidget(self.nameLabel)

        self.nameEdit = QLineEdit(self.gameObject.name)
        self.nameLayout.addWidget(self.nameEdit)

        self.nameLayout.setCurrentIndex(0)

        self.mainLayout.addLayout(self.nameLayout)

        self.setLayout(self.mainLayout)


        Inspector.showGameObject(go=self.gameObject)

        # Create Actions
        self.context = QMenu(self)
        self.CutAction = QAction("Cut", self)

        self.CopyAction = QAction("Copy", self)
        self.PasteAction = QAction("Paste", self)

        self.RenameAction = QAction("Rename", self)
        self.DeleteAction = QAction("Delete", self)
        self.DuplicateAction = QAction("Duplicate", self)


    """
    # 
    # Mouse Hover Events
    # 
    """
    def enterEvent (self, e):
        self.setStyleSheet("background-color: 'darkgrey';")

    def leaveEvent(self, event):
        self.setStyleSheet("")


    """
    # 
    # Context Menu Events
    # 
    """
    def contextMenuEvent(self, e):

        # self.deleteAction = QAction("Delete", self)
        # deleteAction.triggered.connect(
        #     lambda: deleteGameObject(self.gameObject))

        # self.context = QMenu(self)
        self.context.addAction(self.CutAction)
        self.context.addAction(self.CopyAction)
        self.context.addAction(self.PasteAction)
        self.context.addSeparator()
        self.context.addAction(self.RenameAction)
        self.context.addAction(self.DeleteAction)
        self.context.addAction(self.DuplicateAction)
        self.context.addSeparator()

        self.context.exec(e.globalPos())

    def enterEditMode(self):
        self.nameLayout.setCurrentIndex(1)

    def exitEditMode(self):
        self.nameLayout.setCurrentIndex(0)

