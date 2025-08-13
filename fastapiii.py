from fastapi import FastAPI
from pydantic import BaseModel
import time
import os

# ======== МОДЕЛЬ ДАННЫХ ========
class Note(BaseModel):
    title: str
    text: str

# ======== ЛОГИКА ХРАНЕНИЯ ========
class NoteManager:
    def __init__(self, filename="notes.txt"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf8") as file:
            return [line.strip() for line in file if line.strip()]

    def save_notes(self):
        with open(self.filename, "w", encoding="utf8") as file:
            for note in self.notes:
                file.write(note + "\n")

    def get_notes(self):
        return self.notes

    def add_note(self, title, text):
        date = time.strftime("%Y-%m-%d %H:%M")
        note = f"{title} || {text} >>> {date}"
        self.notes.append(note)
        self.save_notes()
        return note

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            deleted = self.notes.pop(index)
            self.save_notes()
            return deleted
        return None


# ======== API ========
app = FastAPI(title="Notes API")
manager = NoteManager()

@app.get("/notes")
def get_notes():
    return {"notes": manager.get_notes()}

@app.post("/notes")
def create_note(note: Note):
    new_note = manager.add_note(note.title, note.text)
    return {"message": "Note added", "note": new_note}

@app.delete("/notes/{note_id}")
def remove_note(note_id: int):
    deleted = manager.delete_note(note_id - 1)  # у нас id с 1
    if deleted:
        return {"message": "Note deleted", "note": deleted}
    return {"error": "Note not found"}
