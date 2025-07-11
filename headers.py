# los headers contienen todo tipo de metadata
# se los usa como autenticación, por ejemplo con las cookies
from fastapi import FastAPI, Header

app = FastAPI()

@app.get('/')
async def get_header(hola: str = Header(...)):
    return {"Hola" : hola}