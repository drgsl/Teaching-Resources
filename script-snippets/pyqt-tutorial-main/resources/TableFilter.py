import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QHeaderView, QWidget, QLineEdit, QApplication, QTableView, QVBoxLayout, QLineEdit, QComboBox
from PyQt5.QtCore import pyqtSignal

class FilterHeader(QHeaderView):
    filterActivated = QtCore.pyqtSignal()

    def __init__(self, parent):
        super().__init__(QtCore.Qt.Horizontal, parent)
        self._editors = []
        self._padding = 4
        self.setStretchLastSection(True)
        #self.setResizeMode(QHeaderView.Stretch)
        self.setDefaultAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.setSortIndicatorShown(False)
        self.sectionResized.connect(self.adjustPositions)
        parent.horizontalScrollBar().valueChanged.connect(self.adjustPositions)

    def setFilterBoxes(self, count):
        while self._editors:
            editor = self._editors.pop()
            editor.deleteLater()
        for index in range(count):
            if index == 3:
                editor = QComboBox(self.parent())
                #editor.returnPressed.connect(self.filterActivated.emit)
                editor.addItems(["One","Two"])
            else:
                editor = QLineEdit(self.parent())
                editor.setPlaceholderText('Filter')
                editor.returnPressed.connect(self.filterActivated.emit)                
            self._editors.append(editor)
        self.adjustPositions()

    def sizeHint(self):
        size = super().sizeHint()
        if self._editors:
            height = self._editors[0].sizeHint().height()
            size.setHeight(size.height() + height + self._padding)
        return size

    def updateGeometries(self):
        if self._editors:
            height = self._editors[0].sizeHint().height()
            self.setViewportMargins(0, 0, 0, height + self._padding)
        else:
            self.setViewportMargins(0, 0, 0, 0)
        super().updateGeometries()
        self.adjustPositions()

    def adjustPositions(self):
        for index, editor in enumerate(self._editors):
            height = editor.sizeHint().height()
            editor.move( self.sectionPosition(index) - self.offset() + 2, height + (self._padding // 2))
            editor.resize(self.sectionSize(index), height)

    def filterText(self, index):
        if 0 <= index < len(self._editors):
            return self._editors[index].text()
        return ''

    def setFilterText(self, index, text):
        if 0 <= index < len(self._editors):
            self._editors[index].setText(text)

    def clearFilters(self):
        for editor in self._editors:
            editor.clear()


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.view = QTableView()
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        header = FilterHeader(self.view)
        self.view.setHorizontalHeader(header)
        model = QtGui.QStandardItemModel(self.view)
        model.setHorizontalHeaderLabels('One Two Three Four Five'.split())
        self.view.setModel(model)
        header.setFilterBoxes(model.columnCount())
        header.filterActivated.connect(self.handleFilterActivated)

    def handleFilterActivated(self):
        header = self.view.horizontalHeader()
        for index in range(header.count()):
            print((index, header.filterText(index)))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 600, 300)
    window.show()
    sys.exit(app.exec_())