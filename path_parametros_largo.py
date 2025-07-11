from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/users/{id}')
async def get_user(id: int = Path(..., ge=1)):
    return {'id': id}


'''
prestar atención acá que el resultado de path es usado como un valor default 
para el argumento del id en la función de operación del path

... (tres puntos) es un objeto literal predefinido en Python, llamado Ellipsis.

Su uso en FastAPI es semántico: marca parámetros obligatorios, sin valor por defecto.
'''