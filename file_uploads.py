from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/files')
async def carga_archivo(file: UploadFile = File(...)):
    return {'file_name': file.filename,
            'content_type': file.content_type,
            'file_size': file.size}
#el parámetro de función "File" es lo que en fastapi nos permite cargar archivos a la web
