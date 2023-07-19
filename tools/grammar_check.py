```python
import language_tool_python

class GrammarCheck:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')

    def check(self, text):
        matches = self.tool.check(text)
        return matches

    def correct(self, text):
        corrected_text = language_tool_python.correct(text, self.tool.check(text))
        return corrected_text
```