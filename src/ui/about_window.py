import tkinter as tk
from src.utils.about_manager import AboutManager

class AboutWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("About")
        self.geometry("300x200")
        self.resizable(False, False)
        self.about_manager = AboutManager()
        self.create_widgets()

    def create_widgets(self):
        about_info = self.about_manager.get_about_info()
        self.about_label = tk.Label(self, text=about_info, justify=tk.LEFT)
        self.about_label.pack(padx=10, pady=10)

    def update_info(self):
        about_info = self.about_manager.get_about_info()
        self.about_label.config(text=about_info)