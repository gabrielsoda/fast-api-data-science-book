from string import punctuation
from typing import List
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# el parámetro de función "File" es lo que en fastapi nos permite cargar archivos a la web
# cambiamos byte (que habiamos usado antes) porque este tipo guarda
# los archivos en memoria y si bien funciona bien con archivos pequeños,
# genera problemas con archivos más grandes.
# fastapi tiene la clase uploadfile que guarda en memoria y hasta cierto punto,
# luego lo empieza a almacenar en disco

@app.post('/files')
async def carga_multiples_archivos(files: List[UploadFile]  = File(...)):
    return [{'file_name': file.filename,
            'content_type': file.content_type,
            'file_size': file.size}
            for file in files
            ]

# le mandamos multiples archivos pasando una lista a uploadfile