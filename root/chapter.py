class Chapter:
    def __init__(self, title, number, content):
        self.title = title
        self.number = number
        self.content = content

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def __str__(self):
        return f"Chapter {self.number}: {self.title}"