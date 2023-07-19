```python
class CharacterDevelopmentTool:
    def __init__(self):
        self.character_attributes = ['name', 'age', 'gender', 'role', 'personality', 'background']

    def create_character(self):
        character = {}
        for attribute in self.character_attributes:
            character[attribute] = input(f"Enter character's {attribute}: ")
        return character

    def edit_character(self, character):
        for attribute in self.character_attributes:
            new_value = input(f"Enter new value for character's {attribute} (leave blank to keep current value): ")
            if new_value:
                character[attribute] = new_value
        return character

    def display_character(self, character):
        for attribute, value in character.items():
            print(f"{attribute.capitalize()}: {value}")

if __name__ == "__main__":
    tool = CharacterDevelopmentTool()
    character = tool.create_character()
    tool.display_character(character)
```