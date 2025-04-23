# src/api/routes/dashboard_grades.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.services.grades_service import get_grades_summary, get_low_grade_alerts, get_grade_trends, get_db

router = APIRouter(prefix="/dashboard/grades", tags=["Dashboard - Calificaciones"])

@router.get("/")
def fetch_grades_summary(db: Session = Depends(get_db)):
    """
    Obtener un resumen de las calificaciones.
    """
    return get_grades_summary(db).to_dict(orient="records")

@router.get("/alerts")
def fetch_grade_alerts(db: Session = Depends(get_db)):
    """
    Obtener alertas de calificaciones bajas.
    """
    return get_low_grade_alerts(db).to_dict(orient="records")

@router.get("/trends")
def fetch_grade_trends(db: Session = Depends(get_db)):
    """
    Obtener tendencias de calificaciones.
    """
    return get_grade_trends(db).to_dict(orient="records")
