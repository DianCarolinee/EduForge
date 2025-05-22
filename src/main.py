from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.upload import save_uploaded_file
from src.models.predictor import predict_desertion
import os

app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Servidor activo en la raíz."}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = await save_uploaded_file(file)
        return {
            "success": True,
            "message": f"Archivo '{file.filename}' guardado correctamente",
            "filename": file.filename,
            "filepath": file_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir archivo: {str(e)}")

@app.post("/predict")
async def predict(filename: str):
    try:
        # Usa la ruta absoluta consistentemente
        upload_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "uploads"))
        file_path = os.path.join(upload_dir, filename)
        
        print(f"Buscando archivo en: {file_path}")  # Para depuración
        
        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=404,
                detail=f"Archivo no encontrado en: {file_path}. Archivos disponibles: {os.listdir(upload_dir)}"
            )
        
        predictions = predict_desertion(file_path)
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))