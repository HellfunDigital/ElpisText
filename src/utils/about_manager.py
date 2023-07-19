```python
class AboutManager:
    def __init__(self):
        self.about_info = self.load_about_info()

    def load_about_info(self):
        about_info = {
            "app_name": "BookMaker",
            "version": "1.0.0",
            "author": "Your Name",
            "description": "A document editing program for making books and novels with a simple, clean, and responsive UI/UX.",
            "contact": "your-email@example.com"
        }
        return about_info

    def get_about_info(self):
        return self.about_info
```