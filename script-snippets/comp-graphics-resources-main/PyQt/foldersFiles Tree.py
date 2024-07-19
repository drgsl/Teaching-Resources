import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        
        hlay = QHBoxLayout(self)
        self.treeview = QTreeView()
        hlay.addWidget(self.treeview)

        path = QDir.rootPath()

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        self.treeview.setModel(self.dirModel)

        self.treeview.setRootIndex(self.dirModel.index(path))

        # self.treeview.clicked.connect(self.on_clicked)

    # def on_clicked(self, index):
    #     path = self.dirModel.fileInfo(index).absoluteFilePath()
    #     self.listview.setRootIndex(self.fileModel.setRootPath(path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())