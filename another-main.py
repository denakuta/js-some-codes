from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "OK"}

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)