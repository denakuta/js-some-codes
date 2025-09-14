from pyexpat.errors import messages
from typing import Optional

from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

app = FastAPI()
with sqlite3.connect('notes.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS notes ('
                   'id INTEGER PRIMARY KEY,'
                   'title TEXT,'
                   'body TEXT)')
    conn.commit()


class Note(BaseModel):
    title: str
    body: str


@app.get("/ping")
def ping():
    return {"status": "OK"}


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


@app.post('/notes')
def post_notes(note: Note):
    with sqlite3.connect('notes.db') as conn:
        cursor.execute(
            'INSERT INTO notes (title, body) VALUES (?, ?)',
            (note.title, note.body)
        )
        conn.commit()
        new_id = cursor.lastrowid
    return {'Note created': 'Successfully'}

