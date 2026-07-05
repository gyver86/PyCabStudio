import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Widgets Example")
        self.resize(300, 400)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Button to trigger new widgets
        self.button = QPushButton("Click to add Widget")
        self.button.clicked.connect(self.add_new_widget)  #
        self.layout.addWidget(self.button)

    @Slot()
    def add_new_widget(self):
        # Create the new widget
        new_label = QLabel("I am a new widget!")

        # Add the new widget to the layout
        self.layout.addWidget(new_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())