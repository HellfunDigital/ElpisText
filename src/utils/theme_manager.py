```python
class ThemeManager:
    def __init__(self):
        self.current_theme = self.load_theme()

    def load_theme(self):
        try:
            with open('src/ui/theme.py', 'r') as file:
                theme = file.read()
                return theme
        except FileNotFoundError:
            return self.default_theme()

    def default_theme(self):
        return {
            'background_color': '#FFFFFF',
            'text_color': '#000000',
            'button_color': '#F0F0F0',
            'button_text_color': '#000000',
            'highlight_color': '#00FF00'
        }

    def set_theme(self, theme):
        self.current_theme = theme
        with open('src/ui/theme.py', 'w') as file:
            file.write(str(theme))

    def get_theme(self):
        return self.current_theme
```