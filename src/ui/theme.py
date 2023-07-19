```python
class Theme:
    def __init__(self):
        self.background_color = "#FFFFFF"
        self.text_color = "#000000"
        self.button_color = "#F0F0F0"
        self.button_text_color = "#000000"
        self.highlight_color = "#FFD700"

    def set_theme(self, background_color, text_color, button_color, button_text_color, highlight_color):
        self.background_color = background_color
        self.text_color = text_color
        self.button_color = button_color
        self.button_text_color = button_text_color
        self.highlight_color = highlight_color

    def get_theme(self):
        return {
            "background_color": self.background_color,
            "text_color": self.text_color,
            "button_color": self.button_color,
            "button_text_color": self.button_text_color,
            "highlight_color": self.highlight_color
        }
```