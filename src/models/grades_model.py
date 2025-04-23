from sqlalchemy import Column, Integer, String, Float, Date
from src.config import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    Estudiante_ID = Column(Integer)
    Nombre = Column(String)
    Calificaciones = Column(Float)
    Asistencia = Column(Float)
    Conducta = Column(String)
    Fecha = Column(Date)
