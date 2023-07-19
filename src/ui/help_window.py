```python
import tkinter as tk
from src.utils.help_manager import HelpManager

class HelpWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Help")
        self.geometry("500x500")
        self.help_manager = HelpManager()
        self.create_widgets()

    def create_widgets(self):
        self.help_text = tk.Text(self)
        self.help_text.pack(fill=tk.BOTH, expand=1)
        self.update_help_text()

    def update_help_text(self):
        help_content = self.help_manager.get_help_content()
        self.help_text.delete(1.0, tk.END)
        self.help_text.insert(tk.END, help_content)
```