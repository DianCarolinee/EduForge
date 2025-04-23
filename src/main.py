# src/main.py
import uvicorn
from fastapi import FastAPI
from src.api.routes import dashboard_grades

app = FastAPI(
    title="EduForge API",
    description="Backend para la predicción de deserción escolar y visualización de calificaciones.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a EduForge API"}

# Incluir las rutas de calificaciones
app.include_router(dashboard_grades.router)


