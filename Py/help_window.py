# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDockWidget
from Py.ui_help import Ui_DockWidget  # Підключаємо твій згенерований файл

class HelpWindow(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DockWidget()
        self.setWindowTitle("Help")  # Назва вікна
        self.ui.setupUi(self)
