from fastapi import FastAPI

app = FastAPI()
app.title = "First FastAPI Project"
app.version = "0.0.1"


@app.get('/', tags=['home'])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
