from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token

app = FastAPI()
app.title = "First FastAPI Project"
app.version = "0.0.1"


class User(BaseModel):
    email:str
    password:str


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


@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)


@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
async def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)


@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
async def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])


@app.get('/movies/', tags=['movies'], response_model=List[Movie])
async def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)


@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
async def create_movies(movie: Movie) -> dict:
    movies.append(dict(movie))
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})


@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
async def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if item['id'] == id:
            item['overview'] == movie.title
            item['year'] == movie.year
            item['rating'] == movie.rating
            item['category'] == movie.category
        return JSONResponse(status_code=200, content={"message": "Se ha modificado la pelicula"})


@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
async def delete_movie(id: int) -> dict:
    [movies.remove(item) for item in movies if item['id'] == id]
    return JSONResponse(content={"message": "Se ha eliminado la pelicula"})
