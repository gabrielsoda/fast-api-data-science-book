'''
los parámetros de query son una manera comun de agregar parámetros
dinámicos a la URL
ejemplo:

?param1=foo&param2=bar

en rest api son usados en endpoints de lectura para aplicar filtros
orden, o seleccionar campos específicos

usan la misma sintaxis que los parametros de ruta así que son bastantes simples y directos
'''

from fastapi import FastAPI

app = FastAPI()

@app.get('/users')
async def get_user(page: int = 1, size: int = 10):
    return {'page': page, 'size': size}


# query requerida:

from enum import Enum

class UsersFormat(str, Enum):
    SHORT = 'short'
    FULL = 'full'

@app.get('/users')
async def get_user(format: UsersFormat):

    return {'format': format}