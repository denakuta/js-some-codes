import sqlite3


conn = sqlite3.connect('idk.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM products WHERE id = ?', (2,))
cursor.execute('INSERT INTO products (id, name, price) '
               'VALUES (?, ?, ?)', (2, 'Скебоб', 2))
cursor.execute('SELECT * FROM products')
# cursor.execute('SELECT price,'
#                ' AVG(price)'
#                ' FROM products'
#                ' GROUP BY price'
#                ' HAVING AVG(price) > ?', (1.4,))
# cursor.execute('SELECT * FROM products ORDER BY price DESC')


conn.commit()


rows = cursor.fetchall()
row_list = []
for row in rows:
    row_dict = {
        'id': row[0],
        'product': row[1],
        'price': row[2]
    }
    row_list.append(row_dict)
print(row_list[0])

conn.close()