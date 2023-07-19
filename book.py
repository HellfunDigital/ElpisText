```python
class Book:
    def __init__(self, title, author, chapters):
        self.title = title
        self.author = author
        self.chapters = chapters

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_chapters(self):
        return self.chapters

    def set_chapters(self, chapters):
        self.chapters = chapters

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def remove_chapter(self, chapter):
        self.chapters.remove(chapter)
```