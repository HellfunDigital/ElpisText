import tkinter as tk
from src.document_editor import DocumentEditor
from src.utils.file_manager import FileManager

class ChapterWindow:
    def __init__(self, master, document_editor: DocumentEditor, file_manager: FileManager):
        self.master = master
        self.document_editor = document_editor
        self.file_manager = file_manager
        self.chapter_frame = tk.Frame(self.master)
        self.chapter_frame.pack()

        self.chapter_title_label = tk.Label(self.chapter_frame, text="Chapter Title")
        self.chapter_title_label.pack()

        self.chapter_title_entry = tk.Entry(self.chapter_frame)
        self.chapter_title_entry.pack()

        self.chapter_content_label = tk.Label(self.chapter_frame, text="Chapter Content")
        self.chapter_content_label.pack()

        self.chapter_content_text = tk.Text(self.chapter_frame)
        self.chapter_content_text.pack()

        self.save_button = tk.Button(self.chapter_frame, text="Save Chapter", command=self.save_chapter)
        self.save_button.pack()

    def save_chapter(self):
        chapter_title = self.chapter_title_entry.get()
        chapter_content = self.chapter_content_text.get("1.0", tk.END)
        self.document_editor.add_chapter(chapter_title, chapter_content)
        self.file_manager.save_chapter(chapter_title, chapter_content)
        self.master.destroy()