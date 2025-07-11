"""
Request Objects con Múltiples Modelos en FastAPI

Cuando se necesita enviar varios objetos diferentes en una sola petición HTTP,
no se pueden armar en el cuerpo múltiples modelos Pydantic como parámetros separados
en tu función endpoint porque FastAPI no sabría cómo estructurar el JSON esperado.

La solución es crear un "modelo contenedor" que agrupe todos los objetos relacionados.
Esto le dice claramente a FastAPI:
1. Qué estructura JSON esperar
2. Cómo validar cada parte del request
3. Cómo generar la documentación automática

Es como crear una "caja organizadora" donde cada objeto tiene su lugar específico
dentro de la petición HTTP.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str

# Modelo contenedor que agrupa ambos objetos
class UserCompanyRequest(BaseModel):
    user: User
    company: Company

@app.post('/user')
async def create_user(request: UserCompanyRequest):
    # acceso a cada objeto por separado
    user_data = request.user
    company_data = request.company
    
    return {
        'user': user_data,
        'company': company_data
    }
'''
http POST localhost:8000/user \
  user:='{"name": "Juan", "age": 25}' \
  company:='{"name": "Mi Empresa"}'
'''