
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the home page"}

@app.get('/about')
def about():
    return {"message": "sdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}

@app.post('/login')
def login(username: str, password: str):
    if username == 'admin' and password == 'password':
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}