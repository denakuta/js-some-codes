import sqlite3
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    price: float
    quantity: int

app = FastAPI()


def init_db():
    connect = sqlite3.connect('book_shop.db')
    connect.row_factory = sqlite3.Row
    return connect

def get_db():
    connect = init_db()
    books = connect.execute('SELECT * FROM books').fetchall()
    connect.commit()
    connect.close()
    return {'notes': [dict(book) for book in books]}

@app.get('/books')
async def get_books():
    return get_db()

@app.get('/books/{id}', response_model=Book)
async def get_book_on_id(book_id: int):
    connect = init_db()
    book = connect.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    connect.commit()
    connect.close()
    return Book(**dict(book))

@app.post('/books/')
async def add_book(book: Book):
    connect = init_db()
    cursor = connect.execute('INSERT INTO books (title, author, price, quantity) VALUES (?, ?, ?, ?)',
                             (book.title, book.author, book.price, book.quantity))
    book_id = cursor.lastrowid
    connect.commit()
    connect.close()
    return Book(id=book_id, **book.dict(exclude={'id'}))

@app.put('/books/{id}')
async def update_book(book_id: int, book: Book)
    connect = init_db()
    exist_book = connect.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    if exist_book is None:
        raise HTTPException(404, 'Book does not exists')
    new_book = connect.execute('UPDATE books SET title = ?, author = ?, price = ?, quantity = ? WHERE id = ?')
