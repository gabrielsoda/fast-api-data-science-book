'''
es parte del rquest http, representa documentos, formularios
etc. en rest api son json, usados para crear objetos estructurados
en una base de datos.
para casos sencillos es lo mismo que query parameters
la diferncia que es siempre implica una Body Function
fastapi busca dentro de los parametros de consulta por default
'''
from fastapi import FastAPI, Body

app = FastAPI()

@app.post('/users')
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {'name': name, 'age': age}
