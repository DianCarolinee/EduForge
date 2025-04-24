# src/models/pydantic_schemas.py

from pydantic import BaseModel
from typing import List

class StudentRisk(BaseModel):
    student_id: int
    name: str
    grade: str
    risk_level: str

class AttendanceData(BaseModel):
    student_id: int
    attendance: List[float]
    dates: List[str]

class GradeData(BaseModel):
    student_id: int
    grades: List[float]
    months: List[str]
