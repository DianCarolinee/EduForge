
# EduForge

**Aplicativo web basado en Machine Learning para la predicción de deserción de estudiantes trujillanos**

Este proyecto tiene como objetivo predecir la probabilidad de deserción de los estudiantes utilizando algoritmos de Machine Learning. El sistema analiza diversas variables académicas, como calificaciones, asistencia y conducta, para identificar estudiantes en riesgo de abandonar sus estudios.

---

## 📘 Descripción

**Objetivo:**  
Desarrollar una aplicación web capaz de predecir la deserción escolar de los estudiantes de Trujillo, usando modelos de aprendizaje automático. El sistema ayuda a las instituciones educativas a tomar decisiones informadas para intervenir y prevenir la deserción.

---

## 🚀 Funcionalidades Clave

- 🧠 **Predicción de deserción**: Modelos ML para predecir el riesgo de deserción basado en calificaciones, asistencia y conducta.
- 📊 **Dashboard educativo**: Visualización gráfica interactiva con alertas tipo semáforo para monitorear el riesgo.
- 📈 **Predicción por variables**: Predicción de deserción por calificación, asistencia y conducta.
- 🧾 **Recomendaciones de intervención**: Generación de acciones sugeridas basadas en el riesgo calculado de deserción.

---

## 🧰 Herramientas y Tecnologías Utilizadas

| Categoría           | Herramienta         |
|---------------------|---------------------|
| **Lenguaje**        | Python 3.10+        |
| **Backend**         | FastAPI             |
| **Modelos ML**      | Scikit-learn        |
| **Visualización**   | Plotly, Matplotlib  |
| **Contenedor**      | Docker              |
| **Base de Datos**   | PostgreSQL          |

---

## 🗂 Estructura del Proyecto

```
EduForge/
├── README.md            # Documentación principal del proyecto
├── requirements.txt     # Dependencias del proyecto
├── .gitignore           # Archivos y carpetas ignoradas por Git
├── Dockerfile           # Configuración para contenedor Docker
├── main.py              # Punto de entrada del sistema
│
├── data/                # Datos de entrada
│   ├── raw/             # Datos crudos
│   ├── processed/       # Dataset limpio
│   ├── interim/         # Datos intermedios
│   └── external/        # Otros datos (INEI, MINEDU, etc.)
│
├── models/              # Modelos entrenados
│   ├── trained/         # Modelos listos para predicción
│   ├── checkpoints/     # Pesos parciales
│   └── prediction_model.py  # Lógica de predicción de deserción
│
├── notebooks/           # Cuadernos de Jupyter
│   ├── 1.0-exploration.ipynb
│   ├── 2.0-training.ipynb
│   └── 3.0-evaluation.ipynb
│
├── reports/             # Informes y visualizaciones
│   └── figures/         # Gráficos generados
│
├── references/          # Referencias y teoría
│   ├── dropout-theory.md
│   └── papers/
│
├── src/                 # Código fuente principal
│   ├── __init__.py
│   ├── config.py        # Parámetros globales
│   ├── api/             # Rutas de la API
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── dashboard_grades.py
│   │       ├── prediction_calculations.py
│   │       ├── prediction_by_grades.py
│   │       ├── prediction_by_attendance.py
│   │       └── prediction_by_behavior.py
│   ├── services/        # Lógica del negocio
│   │   ├── grades_service.py
│   │   ├── prediction_service.py
│   │   └── intervention_service.py
│   ├── models/          # Modelos y funciones de predicción
│   │   ├── grades_model.py
│   │   ├── prediction_model.py
│   │   └── intervention_model.py
│
├── frontend/            # Código frontend (React, Vue, etc.)
│   ├── public/          # Archivos públicos (imágenes, iconos)
│   ├── src/             # Código fuente del frontend
│   │   ├── components/  # Componentes del frontend
│   │   │   ├── Dashboard.js
│   │   │   ├── PredictionForm.js
│   │   │   └── RiskLevels.js
│   │   ├── App.js       # Componente principal
│   │   ├── api.js       # Conexión con el backend
│   │   └── utils.js     # Funciones utilitarias
│   ├── package.json     # Dependencias frontend
│   └── webpack.config.js# Configuración de Webpack
│
├── tests/               # Test de servicios y API
├── scripts/             # Scripts adicionales (entrenamiento, carga de modelos)
└── Dockerfile           # Configuración de Docker
```

---

## 🧪 ¿Cómo ejecutar el proyecto?

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/JamesDroide/EduForge.git

cd EduForge
```

### Paso 2: Crear entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scriptsctivate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar el servidor de la API

```bash
uvicorn src.api.main:app --reload
```

### Paso 5: Explorar los cuadernos de Jupyter (opcional)

```bash
cd notebooks/
# Abre los cuadernos con Jupyter o en VSCode
```

---

## 🚧 Alcance y Futuro del Proyecto

### Funcionalidades implementadas:
- **Predicción de deserción escolar** por calificación, asistencia y conducta.
- **Dashboard educativo interactivo** con alertas visuales.
- **API REST** para servir los modelos de predicción.

### Funcionalidades futuras:
- **Frontend responsivo** para visualizar los resultados de forma más interactiva.
- **Integración con bases de datos reales** de instituciones educativas.
- **Autenticación de usuarios** y manejo de perfiles.

---

## 📊 Métricas y Objetivos

- **Aumentar la precisión** de la predicción de deserción escolar.
- **Reducir la tasa de deserción** mediante intervenciones tempranas.
- **Monitorear el progreso de la intervención** con datos históricos.

---

## 👩‍💻 Autores

**James Huaman Zumaeta**  
Estudiante de la Universidad Privada Antenor Orrego (UPAO)
📍 Trujillo, Perú – 2025  
✉️ [jhuamanz1@upao.edu.pe]

**Diana Carolina Chanta Chinchay**  
Estudiante de la Universidad Privada Antenor Orrego (UPAO)
📍 Trujillo, Perú – 2025  
✉️ [dchantac1@upao.edu.pe]

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.