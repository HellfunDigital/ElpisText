```python
class Chapter:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.word_count = self.calculate_word_count()

    def calculate_word_count(self):
        return len(self.content.split())

    def edit_title(self, new_title):
        self.title = new_title

    def edit_content(self, new_content):
        self.content = new_content
        self.word_count = self.calculate_word_count()

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_word_count(self):
        return self.word_count
```