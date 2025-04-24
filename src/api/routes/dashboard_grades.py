# src/api/routes/dashboard_grades.py

from fastapi import APIRouter, Depends
from src.services.grades_service import GradesService
from pydantic import BaseModel
import matplotlib.pyplot as plt
from io import BytesIO
import base64

router = APIRouter()

class GradeData(BaseModel):
    student_id: int
    grades: list  # Lista de calificaciones
    months: list  # Lista de meses correspondientes a las calificaciones

@router.post("/grades_trend")
async def get_grades_trend(data: GradeData, grades_service: GradesService = Depends()):
    # Llamamos al servicio para obtener los datos procesados
    plot_url = grades_service.generate_grades_plot(data)
    return {"plot_url": plot_url}
