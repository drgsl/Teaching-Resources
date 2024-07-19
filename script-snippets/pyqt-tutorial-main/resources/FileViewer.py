import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget, QFileSystemModel, QPushButton

class FileViewer(QMainWindow):
    def __init__(self, directory_path):
        super().__init__()

        self.setWindowTitle('File Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.file_model = QFileSystemModel()
        self.file_model.setRootPath(directory_path)

        self.file_list = QListView()
        self.file_list.setModel(self.file_model)
        self.file_list.setRootIndex(self.file_model.index(directory_path))

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.navigate_back)

        layout.addWidget(self.back_button)
        layout.addWidget(self.file_list)

    def navigate_back(self):
        current_index = self.file_list.rootIndex()
        if current_index != self.file_model.index(self.file_model.rootPath()):
            parent_index = self.file_model.parent(current_index)
            self.file_list.setRootIndex(parent_index)

def main():
    app = QApplication(sys.argv)
    
    directory_path = 'E:\thesis\apps\Python Game Engine'
    
    window = FileViewer(directory_path)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
