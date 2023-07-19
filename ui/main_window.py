```python
import tkinter as tk
from src.document_editor import DocumentEditor
from src.ui.chapter_window import ChapterWindow
from src.ui.tool_window import ToolWindow
from src.ui.settings_window import SettingsWindow
from src.ui.help_window import HelpWindow
from src.ui.about_window import AboutWindow
from src.utils.theme_manager import ThemeManager
from src.utils.style_manager import StyleManager

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Book Editor")
        self.editor = DocumentEditor()
        self.theme_manager = ThemeManager()
        self.style_manager = StyleManager()

        self.create_menus()

    def create_menus(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.editor.new_book)
        file_menu.add_command(label="Open", command=self.editor.open_book)
        file_menu.add_command(label="Save", command=self.editor.save_book)
        file_menu.add_command(label="Exit", command=self.window.quit)

        edit_menu = tk.Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.editor.undo)
        edit_menu.add_command(label="Redo", command=self.editor.redo)

        view_menu = tk.Menu(menu)
        menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Zoom In", command=self.editor.zoom_in)
        view_menu.add_command(label="Zoom Out", command=self.editor.zoom_out)

        tools_menu = tk.Menu(menu)
        menu.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Word Count", command=ToolWindow(self.editor.tools['WordCount']).show)
        tools_menu.add_command(label="Spell Check", command=ToolWindow(self.editor.tools['SpellCheck']).show)
        tools_menu.add_command(label="Grammar Check", command=ToolWindow(self.editor.tools['GrammarCheck']).show)
        tools_menu.add_command(label="Character Tracker", command=ToolWindow(self.editor.tools['CharacterTracker']).show)
        tools_menu.add_command(label="Plot Development", command=ToolWindow(self.editor.tools['PlotDevelopment']).show)

        help_menu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Help", command=HelpWindow().show)
        help_menu.add_command(label="About", command=AboutWindow().show)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    MainWindow().run()
```