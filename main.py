from fastapi import FastAPI

app = FastAPI()

app.get('/')
def hello():
    return {"data": [1,2,34,545,90]}

app.get('/hello')
def hi():
    return {"message": "Hello, World!"}