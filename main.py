import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcao():
    return {True, "num_random":random.randint(0, 500)}