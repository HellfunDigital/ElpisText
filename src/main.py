```python
import sys
from PyQt5.QtWidgets import QApplication

from document_editor import DocumentEditor
from ui.main_window import MainWindow
from utils.file_manager import FileManager
from utils.settings_manager import SettingsManager
from utils.help_manager import HelpManager
from utils.about_manager import AboutManager
from utils.theme_manager import ThemeManager
from utils.style_manager import StyleManager

class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.file_manager = FileManager()
        self.settings_manager = SettingsManager()
        self.help_manager = HelpManager()
        self.about_manager = AboutManager()
        self.theme_manager = ThemeManager()
        self.style_manager = StyleManager()
        self.document_editor = DocumentEditor(self.file_manager, self.settings_manager)
        self.main_window = MainWindow(self.document_editor, self.help_manager, self.about_manager, self.theme_manager, self.style_manager)

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    main = Main()
    main.run()
```