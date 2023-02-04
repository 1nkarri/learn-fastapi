from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "First FastAPI Project"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]


@app.get('/', tags=['home'])
async def root():
    return {"message": "Hello World"}


@app.get('/html', tags=['html'])
async def printhtml():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/movies', tags=['movies'])
async def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
async def get_movie(id: int):
    return [item for item in movies if item["id"] == id]


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
