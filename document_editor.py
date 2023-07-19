```python
from src.book import Book
from src.chapter import Chapter
from src.tools.word_count import WordCount
from src.tools.spell_check import SpellCheck
from src.tools.grammar_check import GrammarCheck
from src.tools.character_tracker import CharacterTracker
from src.tools.plot_development import PlotDevelopment

class DocumentEditor:
    def __init__(self):
        self.book = None
        self.current_chapter = None
        self.word_count_tool = WordCount()
        self.spell_check_tool = SpellCheck()
        self.grammar_check_tool = GrammarCheck()
        self.character_tracker_tool = CharacterTracker()
        self.plot_development_tool = PlotDevelopment()

    def create_new_book(self, title, author):
        self.book = Book(title, author)

    def add_chapter(self, title, content):
        chapter = Chapter(title, content)
        self.book.add_chapter(chapter)
        self.current_chapter = chapter

    def edit_chapter(self, title, content):
        self.current_chapter.title = title
        self.current_chapter.content = content

    def delete_chapter(self, chapter):
        self.book.delete_chapter(chapter)

    def get_word_count(self):
        return self.word_count_tool.get_count(self.current_chapter.content)

    def check_spelling(self):
        return self.spell_check_tool.check(self.current_chapter.content)

    def check_grammar(self):
        return self.grammar_check_tool.check(self.current_chapter.content)

    def track_characters(self):
        return self.character_tracker_tool.track(self.book)

    def develop_plot(self):
        return self.plot_development_tool.develop(self.book)
```