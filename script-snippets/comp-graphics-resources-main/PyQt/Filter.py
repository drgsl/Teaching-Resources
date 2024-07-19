import sys
from PyQt6.QtWidgets import *

from PyQt6 import QtWidgets
from PyQt6 import QtCore,QtGui
import pandas as pd

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 300, 500, 300)
        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.centralwidget = QtWidgets.QWidget(self)

        self.btn1 = QPushButton('Unfilter', self)
        self.btn1.clicked.connect(self.Unfilter)

        # 创建布局
        self.filter_layout = QHBoxLayout()
        self.filter_layout.addStretch(3)
        self.filter_layout.addWidget(self.btn1)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.filter_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.horizontalHeader = self.table.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)
        filename = 'test.xlsx'
        self.df1 = pd.read_excel(filename, engine='openpyxl', sheet_name='Sheet1', header=0)
        # self.df1['Date'] =self.df1['Date'].dt.date
        self.insertData(self.df1)

    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex   = logicalIndex
        self.menuValues     = QtWidgets.QMenu(self)
        self.signalMapper   = QtCore.QSignalMapper(self)

        valuesUnique = [self.table.item(row, self.logicalIndex).text() for row in range(self.table.rowCount()) if not self.table.isRowHidden(row)]

        # 子窗口
        self.Menudialog = QDialog(self)
        self.Menudialog.setWindowTitle('Sub Window')
        self.Menudialog.resize(200, 150)

        self.list_widget = QListWidget(self)
        self.list_widget.addItems(sorted(list(set(valuesUnique))))
        # create QScrollArea，put QListWidget in it
        scroll_area = QScrollArea(self.Menudialog)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.list_widget)

        self.list_widget.currentItemChanged.connect(self.on_list_item_clicked)
        layout = QVBoxLayout(self.Menudialog)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

        headerPos = self.table.mapToGlobal(self.horizontalHeader.pos())
        posY = headerPos.y() + self.horizontalHeader.height()
        # posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)
        posX = headerPos.x() + self.horizontalHeader.sectionViewportPosition(self.logicalIndex)
        print(posX)
        if posX > 1700:
            posX = 1620

        self.Menudialog.setGeometry(posX +100, posY, 200, 300)
        self.Menudialog.exec()

        ''' 
        actionAll = QtGui.QAction("All", self)
        actionAll.triggered.connect(self.Unfilter)
        self.menuValues.addAction(actionAll)
        self.menuValues.addSeparator()

        for actionNumber, actionName in enumerate(sorted(list(set(valuesUnique)))):
            action = QtGui.QAction(actionName, self)
            self.signalMapper.setMapping(action, actionNumber)
            action.triggered.connect(self.signalMapper.map)
            self.menuValues.addAction(action)

        self.signalMapper.mappedInt.connect(self.on_signalMapper_mapped)

        headerPos = self.table.mapToGlobal(self.horizontalHeader.pos())

        posY = headerPos.y() + self.horizontalHeader.height()
        posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)

        self.menuValues.exec(QtCore.QPoint(posX, posY))
        '''
    def on_list_item_clicked(self):
        item = self.list_widget.currentItem()
        column = self.logicalIndex
        for i in range(self.table.rowCount()):
            if self.table.item(i, column).text() != item.text():
                self.table.setRowHidden(i, True)
        self.Menudialog.close()

    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        column = self.logicalIndex
        for i in range(self.table.rowCount()):
            if self.table.item(i, column).text() != stringAction:
                self.table.setRowHidden(i, True)

    def filter(self):
        column = self.filter_box.currentIndex()
        for i in range(self.table.rowCount()):
            if self.table.item(i, column).text() != self.search_box.text() and self.search_box.text() !='':
                self.table.setRowHidden(i, True)

    def search(self):
        text = self.search_box.text()
        for i in range(self.table.rowCount()):
            self.table.setRowHidden(i, False)

        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                if text in self.table.item(i, j).text():
                    break
                else:
                    self.table.setRowHidden(i, True)

    def Unfilter(self):
        for i in range(self.table.rowCount()):
                self.table.showRow(i)
    def insertData(self, df1):
        if len(df1) < 1:
            msgBox = QMessageBox(self)
            msgBox.setWindowTitle('注意')
            msgBox.setText('数据集为空,不能显示!')
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes)
            msgBox.exec()
            return
        # 获取列名
        self.header = df1.columns.tolist()
        # 获取数据
        data = df1.values.tolist()
        self.row =len(data)
        self.col = len(data[0])
        # 设置表格的行数为0，以清空之前的内容
        self.table.setRowCount(0)
        self.table.setRowCount(self.row)
        self.table.setColumnCount(self.col)
        self.table.setHorizontalHeaderLabels(self.header)
        if data:
            # 按行添加数据
            for r in range(self.row):
                for c in range(self.col):
                    # 添加表格数据
                    newItem = QTableWidgetItem(str(data[r][c]))
                    self.table.setItem(r, c, newItem)
        else:
            self.label.setText('无数据')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec())