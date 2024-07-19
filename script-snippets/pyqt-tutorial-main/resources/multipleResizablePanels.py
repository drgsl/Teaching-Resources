import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplitter, QTextEdit, QPushButton

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        button = QPushButton("Custom Button", self)
        layout.addWidget(button)

class ResizablePanelsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Resizable Panels')
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        splitter = QSplitter()
        layout.addWidget(splitter)

        left_panel = QTextEdit("Left Panel", self)
        right_panel = CustomWidget()

        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)

def main():
    app = QApplication(sys.argv)
    
    window = ResizablePanelsWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
