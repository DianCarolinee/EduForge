# src/models/prediction_model.py

import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler


class DropoutPredictionModel:
    def __init__(self, model_path: str, scaler_path: str):
        """
        Carga el modelo y el scaler desde los archivos especificados.
        :param model_path: Ruta del archivo del modelo entrenado (.pkl)
        :param scaler_path: Ruta del archivo del scaler entrenado (.pkl)
        """
        # Cargar el modelo entrenado
        with open(model_path, 'rb') as file:
            self.model = pickle.load(file)

        # Cargar el scaler
        with open(scaler_path, 'rb') as file:
            self.scaler = pickle.load(file)

    def predict(self, features):
        """
        Realiza la predicción utilizando el modelo cargado.

        :param features: Lista de características del estudiante (calificaciones, asistencia, conducta)
        :return: La probabilidad de deserción del estudiante (1 = deserta, 0 = no deserta)
        """
        # Normalizar los datos de entrada usando el scaler cargado
        features_scaled = self.scaler.transform([features])

        # Realizar la predicción
        return self.model.predict(features_scaled)[0]  # Devuelve 1 o 0
