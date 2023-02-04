from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "First FastAPI Project"
app.version = "0.0.1"


@app.get('/', tags=['home'])
async def root():
    return {"message": "Hello World"}

@app.get('/html', tags=['html'])
async def printhtml():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
