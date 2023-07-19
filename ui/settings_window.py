```python
import tkinter as tk
from src.utils.settings_manager import SettingsManager

class SettingsWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Settings")
        self.settings_manager = SettingsManager()
        self.create_widgets()

    def create_widgets(self):
        self.number_of_chapters_label = tk.Label(self, text="Number of Chapters")
        self.number_of_chapters_label.pack()

        self.number_of_chapters_entry = tk.Entry(self)
        self.number_of_chapters_entry.pack()

        self.save_button = tk.Button(self, text="Save", command=self.save_settings)
        self.save_button.pack()

    def save_settings(self):
        number_of_chapters = self.number_of_chapters_entry.get()
        self.settings_manager.set_number_of_chapters(number_of_chapters)
        self.destroy()
```