from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


def load_ui():
    ui_path = Path(__file__).parent / "ui" / "main_window.ui"

    file = QFile(str(ui_path))
    if not file.open(QFile.ReadOnly):
        raise RuntimeError(f"Cannot open UI file: {ui_path}")

    loader = QUiLoader()
    window = loader.load(file)
    file.close()

    if window is None:
        raise RuntimeError("Failed to load UI file.")

    return window


def main():
    app = QApplication(sys.argv)
    window = load_ui()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()