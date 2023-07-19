```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def get_chapter(self, index):
        return self.chapters[index]

    def get_number_of_chapters(self):
        return len(self.chapters)

    def get_word_count(self):
        total_words = 0
        for chapter in self.chapters:
            total_words += chapter.get_word_count()
        return total_words

class Chapter:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_word_count(self):
        return len(self.content.split())
```