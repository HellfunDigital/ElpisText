```python
import tkinter as tk
from src.tools.word_count import WordCount
from src.tools.spell_check import SpellCheck
from src.tools.grammar_check import GrammarCheck
from src.tools.character_tracker import CharacterTracker
from src.tools.plot_development import PlotDevelopment

class ToolWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Tools")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.word_count = WordCount(self)
        self.word_count.pack()

        self.spell_check = SpellCheck(self)
        self.spell_check.pack()

        self.grammar_check = GrammarCheck(self)
        self.grammar_check.pack()

        self.character_tracker = CharacterTracker(self)
        self.character_tracker.pack()

        self.plot_development = PlotDevelopment(self)
        self.plot_development.pack()

if __name__ == "__main__":
    root = tk.Tk()
    tool_window = ToolWindow(root)
    tool_window.mainloop()
```