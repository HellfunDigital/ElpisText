```python
class StyleManager:
    def __init__(self):
        self.styles = self.load_styles()

    def load_styles(self):
        try:
            with open('styles.json', 'r') as file:
                styles = json.load(file)
        except FileNotFoundError:
            styles = self.default_styles()
        return styles

    def default_styles(self):
        return {
            'font': 'Arial',
            'size': 12,
            'color': 'black',
            'background': 'white'
        }

    def get_style(self, style_name):
        return self.styles.get(style_name, self.default_styles())

    def set_style(self, style_name, style):
        self.styles[style_name] = style
        self.save_styles()

    def save_styles(self):
        with open('styles.json', 'w') as file:
            json.dump(self.styles, file)
```