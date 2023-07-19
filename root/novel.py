```python
class Novel:
    def __init__(self, title, author, num_chapters):
        self.title = title
        self.author = author
        self.num_chapters = num_chapters
        self.chapters = []

    def add_chapter(self, chapter):
        if len(self.chapters) < self.num_chapters:
            self.chapters.append(chapter)
        else:
            print("Error: Maximum number of chapters reached.")

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_num_chapters(self):
        return self.num_chapters

    def get_chapters(self):
        return self.chapters
```