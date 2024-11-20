from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"data": {"number": [23,4,5,6], "name": "chantha"}}

@app.get('/hello')
def hi():
    return {"message": "Hello, World!"}

@app.get('/about')
def about():
    return {"data": "about page"}

@app.get("/blog/{blog_id}")
def blog(blog_id: int):
    return {"data": blog_id}

@app.get('/blog/{id}/comment')
def comment():
    return {
        "data": {
            "1",
            "2"
        }
    }