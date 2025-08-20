import psycopg2
from psycopg2.extras import DictCursor


conn = psycopg2.connect(
    host="127.0.0.1",
    dbname="news",
    user="postgres",
    password="Takoyashi2009!",
    port=5432
)
cursor = conn.cursor(cursor_factory=DictCursor)

title = input("Enter a news title: ")
preview = input("Enter a news preview: ")
sql = f"INSERT INTO news (title, preview) VALUES (%s, %s)"

try:
    cursor.execute(sql, (title, preview))
finally:
    conn.close()
conn.commit()



cursor.execute("SELECT * FROM news")


rows = cursor.fetchall()


for news in rows:
    print(news['title'], '--', news['preview'])
print(type(rows[0]))
print(type(rows[0]['title']))
print(type(rows))


cursor.close()
conn.close()
