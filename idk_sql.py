import sqlite3


conn = sqlite3.connect(r'D:\trying_db\idk.sqlite')
cursor = conn.cursor()

cursor.execute('SELECT * FROM products')
rows = cursor.fetchall()

print(rows)

conn.close()