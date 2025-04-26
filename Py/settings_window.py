# This Python file uses the following encoding: utf-8
import sys
import json
import os
from PySide6.QtWidgets import QDockWidget, QMessageBox
from Py.ui_settings import Ui_DockWidget # підключаємо твій згенерований ui_settings

class SettingsWindow(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        # Путь до json файлу
        self.settings_file = "settings_data.json"

        # Завантажуємо налаштування
        self.load_settings()

        # Підключаємо кнопку Save якщо вона є
        if hasattr(self.ui, 'save_button'):
            self.ui.save_button.clicked.connect(self.save_settings)

    def load_settings(self):
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, "r", encoding="utf-8") as f:
                    settings = json.load(f)
                    # Тут ти будеш вручну розподіляти що куди
                    # Наприклад:
                    # if hasattr(self.ui, 'username_lineedit'):
                    #     self.ui.username_lineedit.setText(settings.get("username", ""))
                    pass
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load settings: {e}")

    def save_settings(self):
        settings = {}
        # Тут ти вручну будеш зберігати поля
        # Наприклад:
        # if hasattr(self.ui, 'username_lineedit'):
        #     settings["username"] = self.ui.username_lineedit.text()

        try:
            with open(self.settings_file, "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Success", "Settings saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save settings: {e}")
