# src/models/student_data_model.py

from sqlalchemy import Column, Integer, Float, String, Date
from src.config import Base


class StudentData(Base):
    __tablename__ = "student_data"

    estudiante_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    calificaciones = Column(Float)  # Podría ser una calificación promedio o un conjunto de calificaciones
    asistencia = Column(Float)  # Porcentaje de asistencia
    conducta = Column(String)  # Comportamiento del estudiante (Buena, Neutral, Mala)
    fecha = Column(Date)  # Fecha en que se registraron los datos

    def __repr__(self):
        return f"<StudentData(estudiante_id={self.estudiante_id}, nombre={self.nombre}, calificaciones={self.calificaciones}, asistencia={self.asistencia}, conducta={self.conducta}, fecha={self.fecha})>"
