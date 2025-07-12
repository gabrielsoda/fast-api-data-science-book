from fastapi import FastAPI
from enum import Enum

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


app = FastAPI()

@app.get('/users/{type}/{id}/')
async def get_user(type: UserType, id: int):
    return {'type': type, 'id': id}

# Cuando le pasamos el path, tiene que se o standard o admin. esta es la ventaja de usar enum con tipado estrictu