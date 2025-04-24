# src/services/attendance_service.py

import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sqlalchemy.orm import Session
from src.config import SessionLocal
from src.models.student_data_model import StudentData


class AttendanceService:

    def get_attendance_from_db(self, student_id: int):
        """
        Función para obtener la asistencia e inasistencia de la base de datos
        """
        db = SessionLocal()
        try:
            student_data = db.query(StudentData).filter(StudentData.estudiante_id == student_id).all()
            attendance = [data.asistencia for data in student_data]
            dates = [data.fecha.strftime("%b %Y") for data in student_data]  # Convertir la fecha a mes/año
            return attendance, dates
        finally:
            db.close()

    def generate_attendance_plot(self, student_id: int):
        """
        Función para generar el gráfico de asistencia e inasistencia
        """
        attendance, dates = self.get_attendance_from_db(student_id)

        # Asistencia e Inasistencia (inverso de la asistencia)
        present = attendance
        absent = [100 - value for value in attendance]  # La inasistencia es el complemento de la asistencia

        # Crear la figura para el gráfico de barras
        plt.figure(figsize=(10, 6))

        # Graficar barras de Asistencia y Inasistencia
        plt.bar(dates, present, label="Asistencia", color="blue")
        plt.bar(dates, absent, label="Inasistencia", color="gray", bottom=present)

        # Añadir título y etiquetas
        plt.title("Evolución de la Asistencia e Inasistencia")
        plt.xlabel("Fechas")
        plt.ylabel("Porcentaje (%)")
        plt.legend()

        # Convertir el gráfico a un formato de imagen base64
        img_io = BytesIO()
        plt.savefig(img_io, format='png')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        plt.close()

        return f"data:image/png;base64,{img_base64}"
