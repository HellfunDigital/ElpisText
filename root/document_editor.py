```python
import os
from book import Book
from novel import Novel

class DocumentEditor:
    def __init__(self):
        self.current_document = None

    def create_book(self, title, author, num_chapters):
        self.current_document = Book(title, author, num_chapters)

    def create_novel(self, title, author, num_chapters):
        self.current_document = Novel(title, author, num_chapters)

    def edit_title(self, new_title):
        self.current_document.title = new_title

    def edit_author(self, new_author):
        self.current_document.author = new_author

    def edit_num_chapters(self, new_num_chapters):
        self.current_document.num_chapters = new_num_chapters

    def save_document(self):
        if isinstance(self.current_document, Book):
            file_path = f"root/books/{self.current_document.title}.txt"
        elif isinstance(self.current_document, Novel):
            file_path = f"root/novels/{self.current_document.title}.txt"
        else:
            return "No document to save."

        with open(file_path, 'w') as file:
            file.write(str(self.current_document))

        return "Document saved successfully."

    def load_document(self, title, document_type):
        if document_type.lower() == "book":
            file_path = f"root/books/{title}.txt"
        elif document_type.lower() == "novel":
            file_path = f"root/novels/{title}.txt"
        else:
            return "Invalid document type."

        if not os.path.exists(file_path):
            return "Document not found."

        with open(file_path, 'r') as file:
            document_data = file.read()

        if document_type.lower() == "book":
            self.current_document = Book.from_string(document_data)
        elif document_type.lower() == "novel":
            self.current_document = Novel.from_string(document_data)

        return "Document loaded successfully."
```