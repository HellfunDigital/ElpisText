```python
import requests
import json

class ThesaurusTool:
    def __init__(self):
        self.api_key = "your_api_key"  # Replace with your API key
        self.endpoint = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/"

    def get_synonyms(self, word):
        response = requests.get(f"{self.endpoint}{word}?key={self.api_key}")
        if response.status_code == 200:
            data = json.loads(response.text)
            if data:
                return data[0]['meta']['syns'][0]
        return []

    def get_antonyms(self, word):
        response = requests.get(f"{self.endpoint}{word}?key={self.api_key}")
        if response.status_code == 200:
            data = json.loads(response.text)
            if data:
                return data[0]['meta']['ants'][0]
        return []
```