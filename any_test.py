import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

connect = sqlite3.connect('book_shop.db')
cursor = connect.cursor()

items = cursor.execute('SELECT * FROM books WHERE id = ?')


# items = [
#     {'item_id': 1, 'item_title': 'smthn', 'item_body': 'rand desc'},
#     {'item_id': 2, 'item_title': 'smthn2', 'item_body': 'rand desc2'},
#     {'item_id': 3, 'item_title': 'smthn3', 'item_body': 'rand desc3'},
#     {'item_id': 4, 'item_title': 'smthn4', 'item_body': 'rand desc4'},
# ]


class Item(BaseModel):
    item_id: int
    item_title: str
    item_body: str

@app.post("/items/")
async def create_item(item: Item):
    items.append(item.dict())
    return {"message": "Item created", "item": item}

@app.put('/items/{item_id}')
async def update_item(item_id: int, updated_item: Item):
    for item in items:
        if item['item_id'] == item_id:
            item['item_title'] = updated_item.item_title
            item['item_body'] = updated_item.item_body
            return {"message": "Item updated", "item": item}
    return {"error": "Item not found"}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for item in items:
        if item['item_id'] == item_id:
            items.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item['item_id'] == item_id:
            return item
    return {"error": "Item not found"}

@app.get('/about')
async def about():
    return {'message': 'about'}