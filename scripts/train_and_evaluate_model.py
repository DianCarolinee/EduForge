# scripts/train_and_evaluate_model.py

import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pickle

# Usar la ruta completa para el directorio 'models/trained/'
trained_dir = r"C:\Users\james\OneDrive\Documentos\PREGRADO UPAO\CICLO 9\Tesis I\EduForge\src\models\trained"

# Crear la carpeta 'models/trained' si no existe
os.makedirs(trained_dir, exist_ok=True)

# Cargar el dataset
df = pd.read_csv("C:\\Users\\james\\OneDrive\\Documentos\\PREGRADO UPAO\\CICLO 9\\Tesis I\\EduForge\\data\\raw\\students.csv")

# Preprocesamiento según las reglas proporcionadas:
df['calificacion'] = df['calificacion'].apply(lambda x: 1 if x >= 11 else 0)
df['asistencia'] = df['asistencia'].apply(lambda x: 1 if x >= 75 else 0)
df['conducta'] = df['conducta'].apply(lambda x: 1 if x >= 11 else 0)

# Crear la columna 'deserta'
def calculate_dropout(row):
    if row['calificacion'] == 0 and row['asistencia'] == 0 and row['conducta'] == 0:
        return 1  # Deserción
    else:
        return 0  # No deserción

df['deserta'] = df.apply(calculate_dropout, axis=1)

# Separar las variables independientes (X) y la variable dependiente (y)
X = df[['calificacion', 'asistencia', 'conducta']]  # Características
y = df['deserta']  # Objetivo

# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear y entrenar el modelo RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Guardar el modelo entrenado
with open(os.path.join(trained_dir, 'dropout_model.pkl'), 'wb') as file:
    pickle.dump(model, file)

# Guardar el scaler
with open(os.path.join(trained_dir, 'scaler.pkl'), 'wb') as file:
    pickle.dump(scaler, file)

print("Modelo y scaler entrenados y guardados exitosamente.")
