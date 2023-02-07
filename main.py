from fastapi import FastAPI, Body, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "First FastAPI Project"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_Lenght=5, max_Length=15)
    overview: str = Field(min_Lenght=15, max_Length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_Lenght=5, max_Length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "El titulo de la pelicula",
                "overview": "Descripción de la pelicula",
                "year": 2022,
                "rating": 5.0,
                "category": "Acción"
            }
        }

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
async def get_movie(id: int = Path(ge=1, le=2000)):
    return [item for item in movies if item["id"] == id]


@app.get('/movies/', tags=['movies'])
async def get_movies_by_category(category: str, year: int):
    return [movie for movie in movies if movie['category'] == category], year

@app.post('/movies', tags=['movies'])
async def create_movies(movie: Movie):
    movies.append(dict(movie))
    return movies

@app.put('/movies/{id}', tags=['movies'])
async def update_movie(id: int, movie: Movie):
    for item in movies:
        if item['id'] == id:
            item['overview'] == movie.title
            item['year'] == movie.year
            item['rating'] == movie.rating
            item['category'] == movie.category
        return movies

@app.delete('/movies/{id}', tags=['movies'])
async def delete_movie(id: int):
    return [item for item in movies if item['id'] != id]