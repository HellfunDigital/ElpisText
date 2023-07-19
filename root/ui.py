```python
import tkinter as tk
from document_editor import DocumentEditor

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.editor = DocumentEditor()

    def render(self):
        self.root.title("Book Editor")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()

        self.author_label = tk.Label(self.root, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(self.root)
        self.author_entry.pack()

        self.chapter_label = tk.Label(self.root, text="Number of Chapters:")
        self.chapter_label.pack()
        self.chapter_entry = tk.Entry(self.root)
        self.chapter_entry.pack()

        self.save_button = tk.Button(self.root, text="Save", command=self.save_book)
        self.save_button.pack()

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        chapters = int(self.chapter_entry.get())
        self.editor.create_book(title, author, chapters)

if __name__ == "__main__":
    ui = UI()
    ui.render()
```