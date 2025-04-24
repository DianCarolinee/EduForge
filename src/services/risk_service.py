# src/services/risk_service.py

from sqlalchemy.orm import Session
from src.config import SessionLocal
from src.models.student_data_model import StudentData
from src.models.prediction_model import PredictionModel  # Asegúrate de que este modelo esté definido


class RiskService:

    def __init__(self):
        # Cargar el modelo de predicción
        self.model = PredictionModel(model_path="path_to_your_model.pkl")  # Ajusta la ruta de tu modelo

    def get_students_at_risk(self):
        """
        Función para obtener los estudiantes en riesgo de deserción utilizando la predicción del modelo ML
        """
        db = SessionLocal()
        try:
            students_data = db.query(StudentData).all()
            students_at_risk = []

            for student in students_data:
                # Obtenemos los datos para la predicción (calificaciones, asistencia, conducta)
                features = [student.calificaciones, student.asistencia, student.conducta]

                # Obtener la predicción del modelo (probabilidad de deserción)
                probability_of_dropout = self.model.predict(features)

                # Cálculo del riesgo en base a la predicción
                if probability_of_dropout > 0.7:
                    risk_level = "Alto"
                else:
                    risk_level = "Bajo"

                # Solo agregar los estudiantes en riesgo
                if risk_level != "Bajo":
                    students_at_risk.append({
                        "student_id": student.estudiante_id,
                        "name": student.nombre,
                        "grade": "Primaria" if student.estudiante_id < 1000 else "Secundaria",
                        # Suponiendo un ID para distinguir
                        "risk_level": risk_level
                    })
            return students_at_risk
        finally:
            db.close()
