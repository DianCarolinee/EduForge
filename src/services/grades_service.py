# src/services/grades_service.py
import pandas as pd
from sqlalchemy.orm import Session
from src.config import SessionLocal
from src.models.grades_model import Grade

# Cargar los datos de la base de datos
def load_grades_data(db: Session):
    try:
        query = db.query(Grade)
        df = pd.read_sql(query.statement, db.bind)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        raise e

# Obtener el resumen de las calificaciones por estudiante
def get_grades_summary(db: Session):
    try:
        df = load_grades_data(db)
        return df.groupby("Estudiante_ID")["Calificaciones"].mean().reset_index()
    except Exception as e:
        print(f"Error in get_grades_summary: {e}")
        raise e

# Obtener alertas de calificaciones bajas
def get_low_grade_alerts(db: Session, threshold=11.0):
    try:
        df = get_grades_summary(db)
        return df[df["Calificaciones"] < threshold]
    except Exception as e:
        print(f"Error in get_low_grade_alerts: {e}")
        raise e

# Obtener las tendencias de calificaciones por semestre o mes
def get_grade_trends(db: Session):
    try:
        df = load_grades_data(db)
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df['Mes'] = df['Fecha'].dt.to_period('M')
        return df.groupby(['Mes', 'Estudiante_ID'])["Calificaciones"].mean().reset_index()
    except Exception as e:
        print(f"Error in get_grade_trends: {e}")
        raise e

# Obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()  # Crear una nueva sesión de base de datos
    try:
        yield db  # Proporciona la sesión al usar la función como dependencia
    finally:
        db.close()  # Asegúrate de cerrar la sesión después de usarla
