import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"mensagem": "Hello World"}

@app.get("/teste")
async def funcao():
    return {True, "num_random":random.randint(0, 200)}