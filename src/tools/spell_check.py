```python
import re
from spellchecker import SpellChecker

class SpellCheck:
    def __init__(self):
        self.spell = SpellChecker()

    def check_spelling(self, text):
        words = re.findall(r'\b\w+\b', text)
        misspelled = self.spell.unknown(words)
        return misspelled

    def suggest_corrections(self, word):
        return self.spell.correction(word)
```