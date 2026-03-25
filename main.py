from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"mensagem": "Hello World"}

@app.get("/teste")
async def funcao():
    return {"teste": "deu certo"}