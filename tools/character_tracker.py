```python
class CharacterTracker:
    def __init__(self):
        self.characters = {}

    def add_character(self, name, description):
        self.characters[name] = description

    def remove_character(self, name):
        if name in self.characters:
            del self.characters[name]

    def get_character(self, name):
        return self.characters.get(name, None)

    def get_all_characters(self):
        return self.characters

    def update_character(self, name, description):
        if name in self.characters:
            self.characters[name] = description
```