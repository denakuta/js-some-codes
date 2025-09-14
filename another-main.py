from fastapi import FastAPI, HTTPException
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


class NoteResponse(BaseModel):
    id: int
    title: str
    body: str


def get_db_connection():
    conn = sqlite3.connect('notes.db')
    conn.row_factory = sqlite3.Row  # чтобы можно было обращаться к колонкам по имени
    return conn


@app.get("/ping")
async def ping():
    return {"status": "OK"}


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}


@app.post('/notes')
async def post_notes(note: Note):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO notes (title, body) VALUES (?, ?)',
            (note.title, note.body)
        )
        conn.commit()
        new_id = cursor.lastrowid
    return {'Note created': 'Successfully'}


@app.get('/notes', response_model=list[NoteResponse])
async def get_all_notes():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, body FROM notes")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
