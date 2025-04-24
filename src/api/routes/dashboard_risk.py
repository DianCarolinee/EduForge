# src/api/routes/dashboard_risk.py

from fastapi import APIRouter, Depends
from src.services.risk_service import RiskService
from pydantic import BaseModel
from typing import List

router = APIRouter()

class StudentRisk(BaseModel):
    student_id: int
    name: str
    grade: str  # Primary or Secondary
    risk_level: str  # Indicator of risk (e.g., High, Medium, Low)

@router.get("/students_at_risk", response_model=List[StudentRisk])
async def get_students_at_risk(risk_service: RiskService = Depends()):
    # Llamamos al servicio para obtener la lista de estudiantes en riesgo
    students_at_risk = risk_service.get_students_at_risk()
    return students_at_risk
