import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QKeySequence, QShortcut
from app.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clearProperties()
        self.ui.pushButtonWall.clicked.connect(self.wallTool)
        self.ui.pushButtonDoor.clicked.connect(self.doorTool)

        self.esc_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)
        self.esc_shortcut.activated.connect(self.my_esc_function)


    def my_esc_function(self):
        if self.ui.labelSelectedToolOrObject.isVisible():
            self.clearProperties()
        else:
            print('DEBUG1: nothing to clear')

    def clearProperties(self):
        self.ui.labelSelectedToolOrObject.setVisible(False)
        self.ui.labelSelectedToolOrObject.setText('')


    def wallTool(self):
        self.ui.labelSelectedToolOrObject.setText('Build Wall')
        self.ui.labelSelectedToolOrObject.setVisible(True)

    def doorTool(self):
        self.ui.labelSelectedToolOrObject.setText('Build Door')
        self.ui.labelSelectedToolOrObject.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())