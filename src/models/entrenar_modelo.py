import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle
import os
import joblib  # Mejor alternativa para modelos grandes

# 1. Configuración de paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "trained_model.pkl")

# 2. Dataset más completo (ejemplo extendido)
data = pd.DataFrame({
    "nota_final": [15, 9, 10, 14, 8, 12, 7, 11, 13, 6, 16, 5],
    "asistencia": [10, 3, 5, 9, 2, 7, 1, 6, 8, 4, 10, 0],
    "inasistencia": [2, 9, 8, 3, 10, 4, 11, 5, 3, 8, 1, 12],
    "conducta": ["positivo", "agresivo", "neutral", "positivo", "agresivo", 
                "neutral", "agresivo", "neutral", "positivo", "agresivo", "positivo", "agresivo"],
    "deserta": [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
})

# 3. Codificación más robusta
conducta_map = {"positivo": 0, "neutral": 1, "agresivo": 2}
data["conducta_encoded"] = data["conducta"].map(conducta_map).fillna(1)  # Default neutral

# 4. Features y label con validación
required_features = ["nota_final", "asistencia", "inasistencia", "conducta_encoded"]
X = data[required_features]
y = data["deserta"]

# 5. Entrenamiento con evaluación
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier(
    n_estimators=200,  # Aumentado para mejor performance
    max_depth=5,
    random_state=42,
    class_weight="balanced"  # Manejo de clases desbalanceadas
)

clf.fit(X_train, y_train)

# 6. Evaluación del modelo
y_pred = clf.predict(X_test)
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))
print(f"Exactitud: {accuracy_score(y_test, y_pred):.2f}")

# 7. Guardado seguro del modelo
try:
    joblib.dump(clf, MODEL_PATH)  # Mejor que pickle para modelos sklearn
    print(f"Modelo guardado exitosamente en: {MODEL_PATH}")
except Exception as e:
    print(f"Error al guardar el modelo: {str(e)}")
    raise
