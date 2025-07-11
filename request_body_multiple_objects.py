"""
Request Objects con Múltiples Modelos en FastAPI
Los múltiples objetos son útiles cuando:

Necesitas crear varias entidades relacionadas de una vez
se quiere agrupar información que lógicamente va junta
o para reducir el número de peticiones HTTP para mejorar el rendimiento

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

from fastapi import FastAPI, Body
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
async def create_user(request: UserCompanyRequest, priority: int = Body(..., ge=1, le=3)):
    # acceso a cada objeto por separado
    user_data = request.user
    company_data = request.company
    
    return {
        'user': user_data,
        'company': company_data,
        'priority': priority
    }
'''
http POST localhost:8000/user \
  user:='{"name": "Juan", "age": 25}' \
  company:='{"name": "Mi Empresa"}'
'''
#  o lo que es lo mismo en una linea:
#  http -v POST localhost:8000/user user:='{"name":"Juan", "age":25}' company:='{"name":"Empresa"}'