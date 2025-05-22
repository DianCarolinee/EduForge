import pandas as pd
import joblib  
import os
from typing import List, Dict
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 1. Configuración de paths segura
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "trained_model.pkl")

# 2. Carga segura del modelo
try:
    model = joblib.load(MODEL_PATH)
    logger.info("Modelo cargado exitosamente")
except Exception as e:
    logger.error(f"Error al cargar el modelo: {str(e)}")
    raise

# 3. Mapeo de conducta constante
CONDUCTA_MAP = {"positivo": 0, "neutral": 1, "agresivo": 2}

def encode_conducta(valor: str) -> int:
    """Codifica el valor de conducta con manejo de errores robusto"""
    try:
        return CONDUCTA_MAP.get(str(valor).strip().lower(), 1)  # default neutral
    except Exception as e:
        logger.warning(f"Error codificando conducta: {valor}. Error: {str(e)}")
        return 1

def validate_input_data(df: pd.DataFrame) -> bool:
    """Valida que el DataFrame tenga las columnas requeridas"""
    required_columns = ["nota_final", "asistencia", "inasistencia", "conducta"]
    return all(col in df.columns for col in required_columns)

def predict_desertion(file_path: str) -> List[Dict]:
    """
    Realiza predicciones de deserción escolar a partir de un archivo
    
    Args:
        file_path: Ruta al archivo CSV o Excel con los datos
        
    Returns:
        Lista de diccionarios con los datos originales y predicciones
    """
    try:
        # 4. Carga segura de datos
        if file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)
        
        logger.info(f"Datos cargados correctamente. Filas: {len(df)}")
        
        # 5. Validación de datos
        if not validate_input_data(df):
            raise ValueError("El archivo no contiene las columnas requeridas")
        
        # 6. Preprocesamiento
        df["conducta_encoded"] = df["conducta"].apply(encode_conducta)
        
        # 7. Validación de features
        required_features = ["nota_final", "asistencia", "inasistencia", "conducta_encoded"]
        features = df[required_features]
        
        # 8. Predicción
        df["prediccion_desercion"] = model.predict(features)
        df["resultado"] = df["prediccion_desercion"].map({1: "Sí deserta", 0: "No deserta"})
        
        logger.info(f"Predicciones realizadas. Desertores: {df['prediccion_desercion'].sum()}")
        
        return df.to_dict(orient="records")
    
    except Exception as e:
        logger.error(f"Error en predict_desertion: {str(e)}")
        raise

