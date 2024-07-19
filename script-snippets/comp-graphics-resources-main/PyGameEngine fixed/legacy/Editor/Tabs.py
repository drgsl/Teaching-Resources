# import sys

# from PyQt6.QtCore import (
#     QSize, Qt,
#     QSortFilterProxyModel,
#     QAbstractItemModel,
#     QDir,
# )
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, 
#     QWidget, QTabWidget, 
#     QTableWidget, QTableWidgetItem,
#     QPushButton, QLineEdit, QCheckBox, QLabel,
#     QGridLayout, QTreeView,
#     QListView,
# )

# from PyQt6.QtGui import (
#     QFileSystemModel, QStandardItemModel, QStandardItem,
# )


# from PyQt6.QtOpenGLWidgets import (
#     QOpenGLWidget,
# )

# # from PySide6.QtWidgets import (
# #     QFileSystemModel,
# # )

# from pathlib import Path

# class HierarchyTab(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QGridLayout()

#         treeView = QTreeView()

#         model = QStandardItemModel()

#         item = QStandardItem("Test")

#         model.appendRow(item)
#         model.appendRow(QStandardItem("Test22"))

#         treeView.setModel(model)

#         layout.addWidget(treeView)


#         self.setLayout(layout)

# class AssetsTab(QWidget):
#     def __init__(self, projectPath):
#         super().__init__()
#         layout = QGridLayout()

#         self.model = QFileSystemModel()
#         projectPath = Path(projectPath)
#         projectPath = projectPath.parent
#         self.model.setRootPath(str(projectPath))
#         self.tree = QTreeView()
#         self.tree.setModel(self.model)
#         self.tree.setRootIndex(self.model.index(str(projectPath)))
#         self.model.setReadOnly(False)

#         self.tree.setIndentation(7)
#         self.tree.setSortingEnabled(True)

#         self.tree.setColumnHidden(1, True)
#         self.tree.setColumnHidden(2, True)
#         self.tree.setColumnHidden(3, True)

#         layout.addWidget(self.tree)

#         self.setLayout(layout)

# class CanvasTab(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QGridLayout()

#         layout.addWidget(OpenGLCanvas())

#         self.setLayout(layout)


# class OpenGLCanvas(QOpenGLWidget):
#     def __init__(self):
#         super().__init__()
#         pass
