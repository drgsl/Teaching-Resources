import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

"""
Widget                  What it does
-----------------------------------------------------------
QCheckbox               A checkbox
QComboBox	            A dropdown list box
QDateEdit	            For editing dates and datetimes
QDateTimeEdit	        For editing dates and datetimes
QDial	                Rotatable dial
QDoubleSpinbox	        A number spinner for floats
QFontComboBox	        A list of fonts
QLCDNumber	            A quite ugly LCD display
QLabel	                Just a label, not interactive
QLineEdit	            Enter a line of text
QProgressBar	        A progress bar
QPushButton	            A button
QRadioButton	        A toggle set, with only one active item
QSlider	                A slider
QSpinBox	            An integer spinner
QTimeEdit	            For editing times
"""