import sqlite3
from pprint import pprint
from icecream import ic

connect = sqlite3.connect('book_shop.db')
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS books ('
               'id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL, quantity INTEGER'
');'
)

cursor.execute("""
INSERT INTO books (title, author, price, quantity) VALUES
('Гарри Поттер и философский камень', 'Дж. К. Роулинг', 500, 10),
('Властелин колец', 'Дж. Р. Р. Толкин', 700, 5),
('Преступление и наказание', 'Ф. М. Достоевский', 350, 8),
('Мастер и Маргарита', 'М. А. Булгаков', 400, 12);
""")

cursor.execute('DELETE FROM books WHERE id > ?', (4,))
connect.commit()

# cursor.execute('SELECT title FROM books WHERE price > ?', (400.0,))

# cursor.execute('SELECT AVG(price) FROM books')

# cursor.execute('SELECT title, author, price FROM books ORDER BY price DESC')
# books = cursor.fetchone()

# cursor.execute('SELECT SUM(quantity) FROM books')

cursor.execute('SELECT * FROM books WHERE author = ?', ('Дж. К. Роулинг',))
books = cursor.fetchall()

for book in books:
    print(f"{book[1]} — {book[2]}, {book[3]}₽, {book[4]} шт")
print(books)
pprint(books)
ic(books)

connect.close()