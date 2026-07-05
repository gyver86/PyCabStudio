import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from app.ui.ui_PyCabStudio import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clearProperties()
        self.ui.pushButtonWall.clicked.connect(self.wallTool)

    def clearProperties(self):
        self.ui.labelSelectedToolOrObject.setVisible(False)

    def wallTool(self):
        self.ui.labelSelectedToolOrObject.setText('Draw Wall')
        self.ui.labelSelectedToolOrObject.setVisible(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())