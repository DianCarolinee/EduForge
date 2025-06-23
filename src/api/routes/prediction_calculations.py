# src/api/routes/prediction_calculations.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.prediction_service import predict_dropout

router = APIRouter()

# Definimos el modelo de datos para la entrada
class StudentData(BaseModel):
    calificacion: float
    asistencia: float
    conducta: str

# Endpoint para realizar la predicción de deserción
@router.post("/predict_dropout")
async def predict_dropout_api(student: StudentData):
    try:
        result = predict_dropout(student.calificacion, student.asistencia, student.conducta)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar la predicción: {e}")
