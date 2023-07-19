```python
class WordCount:
    def __init__(self):
        pass

    def count_words(self, chapter):
        words = chapter.content.split()
        return len(words)

    def count_words_in_book(self, book):
        total_words = 0
        for chapter in book.chapters:
            total_words += self.count_words(chapter)
        return total_words
```