# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDockWidget
from Py.ui_about import Ui_DockWidget

class AboutWindow(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)
