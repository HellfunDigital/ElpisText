```python
import os
import pickle
from src.book import Book

class FileManager:
    def __init__(self):
        self.directory = os.path.join(os.path.expanduser('~'), 'DocumentEditor')

    def save_book(self, book: Book, filename: str):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        with open(os.path.join(self.directory, filename), 'wb') as file:
            pickle.dump(book, file)

    def load_book(self, filename: str) -> Book:
        with open(os.path.join(self.directory, filename), 'rb') as file:
            return pickle.load(file)

    def delete_book(self, filename: str):
        os.remove(os.path.join(self.directory, filename))

    def list_books(self):
        return os.listdir(self.directory)
```