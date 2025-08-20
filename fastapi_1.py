import sqlite3
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    price: float
    quantity: int

class BookUpdate(BaseModel):
    title: str
    author: str
    price: float
    quantity: int


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


def init_db():
    connect = sqlite3.connect('book_shop.db')
    connect.row_factory = sqlite3.Row
    # Ensure tables exist
    connect.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL, quantity INTEGER)')
    connect.execute(
        'CREATE TABLE IF NOT EXISTS users ('
        'id INTEGER PRIMARY KEY, '
        'username TEXT UNIQUE, '
        'password TEXT)'
    )
    connect.commit()
    return connect

init_db()

def get_db():
    connect = init_db()
    books = connect.execute('SELECT * FROM books').fetchall()
    connect.commit()
    connect.close()
    return {'notes': [dict(book) for book in books]}

@app.get('/books')
async def get_books():
    return get_db()

@app.get('/books/{book_id}', response_model=Book)
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

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate):
    connect = init_db()
    exist_book = connect.execute(
        "SELECT * FROM books WHERE id = ?", (book_id,)
    ).fetchone()

    if exist_book is None:
        connect.close()
        raise HTTPException(status_code=404, detail="Book does not exist")

    connect.execute(
        "UPDATE books SET title = ?, author = ?, price = ?, quantity = ? WHERE id = ?",
        (book.title, book.author, book.price, book.quantity, book_id)
    )
    connect.commit()
    connect.close()

    return Book(id=book_id, **book.dict())

@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    connect = init_db()
    connect.execute('DELETE FROM books WHERE id = ?', (book_id,))
    connect.commit()
    connect.close()
    return {'message': 'Book deleted successfully'}

@app.post('/register')
async def register(user: UserCreate):
    connect = init_db()
    exists_user = connect.execute(
        'SELECT * FROM users WHERE username = ?', (user.username,)
    ).fetchone()

    if exists_user is not None:
        raise HTTPException(status_code=404, detail='User with this username already exists')
    connect.execute(
        'INSERT INTO users (username, password) VALUES (?, ?)', (user.username, user.password)
    )
    connect.commit()
    connect.close()
    return {'message': 'reg succesful',
            'login': user.username,
            'password': user.password}

@app.post('/login')
async def login(user: UserCreate):
    connect = init_db()
    db_user = connect.execute(
        'SELECT * FROM users WHERE username = ?', (user.username,)
    ).fetchone()
    connect.close()
    if db_user is None:
        raise HTTPException(status_code=401, detail='Invalid username or password')
    if db_user['password'] != user.password:
        raise HTTPException(status_code=401, detail='Invalid username or password')
    return {'message': 'Login successful', 'login': user.username}




@app.get('/')
async def welcome():
    return {'message': 'Suuuup, this is a smthn like book shop'}

@app.get("/about")
async def about():
    return {"message": "Book Shop API - Manage your book inventory(Am i cool?????)"}

# connect = init_db()
# test = connect.execute('SELECT * FROM users').fetchall()
# print([dict(user) for user in test])



