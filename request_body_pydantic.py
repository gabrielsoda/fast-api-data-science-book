# empezamos a estructurar una request body con pydantic para tener una serie de ventajas:
# reutilizació, menos verbose, no nos queda un choclo gigante en
# en la función de operación de ruta 

# pydantic es una libreria par avalidación de data basada en clases y type hints.
# body, path, query son funciones que usan pydantic

from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post('/users')
async def create_user(user: User) -> User:
    return user
