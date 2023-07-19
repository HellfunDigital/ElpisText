```python
import json

class SettingsManager:
    def __init__(self):
        self.settings_file = "settings.json"
        self.default_settings = {
            "theme": "light",
            "font": "Arial",
            "font_size": 12,
            "autosave": True,
            "autosave_interval": 5
        }
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as file:
                settings = json.load(file)
        except FileNotFoundError:
            settings = self.default_settings
            self.save_settings(settings)
        return settings

    def save_settings(self, settings):
        with open(self.settings_file, 'w') as file:
            json.dump(settings, file)

    def get_setting(self, key):
        return self.settings.get(key, self.default_settings.get(key))

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings(self.settings)
```