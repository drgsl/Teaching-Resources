
import sys
from PyQt5 import QtWidgets, QtCore
 
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
 
        # create a horizontal layout
        layout = QtWidgets.QHBoxLayout(self)
 
        # create a label and a size grip
        self.label = QtWidgets.QLabel("Hello, World!")
        self.size_grip = QtWidgets.QSizeGrip(self)
 
        # add the label and size grip to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.size_grip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
 
        # set the size hint of the size grip
        self.size_grip.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.size_grip.setMaximumSize(self.size_grip.sizeHint())
 
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())