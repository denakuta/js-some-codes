import sqlite3

db = sqlite3.connect('testing_mysql.db')

c = db.cursor()

c.execute("""CREATE TABLE articles (
    title text,
    full_text text,
    views integer,
    avtor text
)""")

c.execute("INSERT INTO articles VALUES ('Google is trash', 'Google is idk...', 100, 'Me')")

db.commit()


db.close()