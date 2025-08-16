import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Database setup
def get_db_connection():
    conn = sqlite3.connect('book_shop.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

# Pydantic model for Book
class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    price: float
    quantity: int

# Create table if not exists
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    conn = get_db_connection()
    cursor = conn.execute(
        'INSERT INTO books (title, author, price, quantity) VALUES (?, ?, ?, ?)',
        (book.title, book.author, book.price, book.quantity)
    )
    book_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return Book(id=book_id, **book.dict(exclude={'id'}))

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    conn.close()
    
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return Book(**dict(book))

@app.get("/books/", response_model=List[Book])
async def get_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    
    return [Book(**dict(book)) for book in books]

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    conn = get_db_connection()
    
    # Check if book exists
    existing_book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    if existing_book is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    
    conn.execute(
        'UPDATE books SET title = ?, author = ?, price = ?, quantity = ? WHERE id = ?',
        (book.title, book.author, book.price, book.quantity, book_id)
    )
    conn.commit()
    conn.close()
    
    return Book(id=book_id, **book.dict())

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    conn = get_db_connection()
    
    # Check if book exists
    existing_book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    if existing_book is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    
    conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    
    return {"message": "Book deleted successfully"}

@app.get("/")
async def root():
    return {"message": "Welcome to Book Shop API"}

@app.get("/about")
async def about():
    return {"message": "Book Shop API - Manage your book inventory"}
