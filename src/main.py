# src/main.py

from fastapi import FastAPI
from src.api.routes import dashboard_grades, prediction_calculations  # Asegúrate de importar correctamente

app = FastAPI(
    title="EduForge API",
    description="Backend para la predicción de deserción escolar y visualización de calificaciones.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a EduForge API"}

# Endpoint de predicción
app.include_router(prediction_calculations.router)  # Asegúrate de incluir el router de prediction_calculations

# Endpoint de calificaciones (si tienes otro router)
app.include_router(dashboard_grades.router)
