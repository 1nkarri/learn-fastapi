from fastapi import FastAPI, Body
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


@app.get('/movies/', tags=['movies'])
async def get_movies_by_category(category: str, year: int):
    return [movie for movie in movies if movie['category'] == category], year

@app.post('/movies', tags=['movies'])
async def create_movies(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies