# src/services/prediction_service.py

# Asegúrate de que 'StandardScaler' esté importado correctamente desde sklearn
from sklearn.preprocessing import StandardScaler
from src.models.prediction_model import DropoutPredictionModel

# Usar la ruta completa para el modelo y el scaler entrenados
model_path = r"C:\Users\james\OneDrive\Documentos\PREGRADO UPAO\CICLO 9\Tesis I\EduForge\src\models\trained\dropout_model.pkl"
scaler_path = r"C:\Users\james\OneDrive\Documentos\PREGRADO UPAO\CICLO 9\Tesis I\EduForge\src\models\trained\scaler.pkl"

# Inicializar el modelo y el scaler cargados
model = DropoutPredictionModel(model_path, scaler_path)


def predict_dropout(calificacion: float, asistencia: float, conducta: str):
    """
    Realiza la predicción sobre si un estudiante va a desertar o no.

    :param calificacion: La calificación del estudiante
    :param asistencia: El porcentaje de asistencia del estudiante
    :param conducta: La conducta del estudiante ("Buena", "Mala")
    :return: Un mensaje indicando si el estudiante tiene riesgo de deserción o no
    """
    try:
        # Convertir la conducta en una variable numérica (1 = Buena, 0 = Mala)
        conducta = 1 if conducta.lower() == 'buena' else 0

        # Las características de entrada
        features = [calificacion, asistencia, conducta]

        # Normalizar los datos usando el scaler
        features_scaled = StandardScaler().fit_transform([features])

        # Realizar la predicción
        prediction = model.predict(features_scaled)

        if prediction == 1:
            return {"prediccion": "Sí", "mensaje": "El estudiante tiene riesgo de deserción."}
        else:
            return {"prediccion": "No", "mensaje": "El estudiante no tiene riesgo de deserción."}
    except Exception as e:
        raise Exception(f"Error al realizar la predicción: {e}")
