import json
import os

class NotesManager:
    def __init__(self):
        self.file_path = "data/notes.json"
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def add_note(self, title, content):
        with open(self.file_path, "r") as f:
            notes = json.load(f)

        notes.append({"title": title, "content": content})

        with open(self.file_path, "w") as f:
            json.dump(notes, f, indent=4)

    def view_notes(self):
        with open(self.file_path, "r") as f:
            return json.load(f)