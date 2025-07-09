from fastapi import FastAPI

app = FastAPI() # Instanciamos un objeto FastAPI llamado app
# este es el objeto principal de la aplicación que conecta las rutas API

#Decorator:
@app.get('/') #definición del gey endpoint en el root path
async def buenas_mundo(): #Corutina
    return {"buenas" : "mundo"}
