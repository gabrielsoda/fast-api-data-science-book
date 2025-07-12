# pedido en form


from fastapi import FastAPI, Form

app = FastAPI()

@app.post('/users')
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {'name': name, 'age':age}


# la unica diferencia: usamos form en lugar de body