from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "First FastAPI Project"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_lenght=5, max_length=15)
    overview: str = Field(min_lenght=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_lenght=5, max_length=15)

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
    return JSONResponse(content=movies)


@app.get('/movies/{id}', tags=['movies'])
async def get_movie(id: int = Path(ge=1, le=2000)):
    return [JSONResponse(content=item) for item in movies if item["id"] == id]


@app.get('/movies/', tags=['movies'])
async def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)

@app.post('/movies', tags=['movies'])
async def create_movies(movie: Movie):
    movies.append(dict(movie))
    return JSONResponse(content={"message": "Se ha registrado la pelicula"})

@app.put('/movies/{id}', tags=['movies'])
async def update_movie(id: int, movie: Movie):
    for item in movies:
        if item['id'] == id:
            item['overview'] == movie.title
            item['year'] == movie.year
            item['rating'] == movie.rating
            item['category'] == movie.category
        return JSONResponse(content={"message": "Se ha modificado la pelicula"})

@app.delete('/movies/{id}', tags=['movies'])
async def delete_movie(id: int):
    [movies.remove(item) for item in movies if item['id'] == id]
    return JSONResponse(content={"message":"Se ha eliminado la pelicula"})