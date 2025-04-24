# src/services/behavior_service.py

import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sqlalchemy.orm import Session
from src.config import SessionLocal
from src.models.student_data_model import StudentData


class BehaviorService:

    def get_behavior_from_db(self, student_id: int):
        """
        Función para obtener la conducta de los estudiantes de la base de datos
        """
        db = SessionLocal()
        try:
            student_data = db.query(StudentData).filter(StudentData.estudiante_id == student_id).all()
            behavior = [data.conducta for data in student_data]  # Recupera los valores de conducta
            dates = [data.fecha.strftime("%b %Y") for data in student_data]  # Convertir la fecha a mes/año
            return behavior, dates
        finally:
            db.close()

    def generate_behavior_plot(self, student_id: int):
        """
        Función para generar el gráfico de conducta (pastel)
        """
        behavior, dates = self.get_behavior_from_db(student_id)

        # Contar las ocurrencias de cada tipo de conducta
        good = behavior.count('Buena')
        neutral = behavior.count('Neutral')
        bad = behavior.count('Mala')

        # Crear el gráfico de pastel
        labels = ['Buena', 'Neutral', 'Mala']
        sizes = [good, neutral, bad]
        colors = ['#66b3ff', '#ffcc99', '#ff6666']  # Colores personalizados para cada categoría

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

        # Añadir título
        plt.title('Distribución de Conducta de los Estudiantes')

        # Convertir el gráfico a un formato de imagen base64
        img_io = BytesIO()
        plt.savefig(img_io, format='png')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        plt.close()

        return f"data:image/png;base64,{img_base64}"
