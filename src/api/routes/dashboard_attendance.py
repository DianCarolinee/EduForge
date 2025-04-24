# src/api/routes/dashboard_attendance.py

from fastapi import APIRouter, Depends
from src.services.attendance_service import AttendanceService
from pydantic import BaseModel
import matplotlib.pyplot as plt
from io import BytesIO
import base64

router = APIRouter()

class AttendanceData(BaseModel):
    student_id: int
    attendance: list  # Lista de asistencia
    dates: list  # Lista de fechas correspondientes a la asistencia

@router.post("/attendance_trend")
async def get_attendance_trend(data: AttendanceData, attendance_service: AttendanceService = Depends()):
    # Llamamos al servicio para obtener el gráfico de asistencia
    plot_url = attendance_service.generate_attendance_plot(data.student_id)
    return {"plot_url": plot_url}
