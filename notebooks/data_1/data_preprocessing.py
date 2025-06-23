import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Función para cargar, preprocesar los datos y guardar el CSV procesado
def cargar_y_preprocesar_datos(ruta_csv, normalizar=True, columnas_a_normalizar=None, guardar_csv=False, ruta_guardado=None):
    # Cargar el CSV
    df = pd.read_csv(ruta_csv)

    # Renombrar columnas
    df.rename(columns={
        'Hours_Studied': 'horas_estudio',
        'Attendance': 'asistencia',
        'Parental_Involvement': 'involucramiento_parental',
        'Access_to_Resources': 'acceso_recursos',
        'Extracurricular_Activities': 'actividades_extracurriculares',
        'Sleep_Hours': 'horas_sueno',
        'Previous_Scores': 'puntuaciones_previas',
        'Motivation_Level': 'nivel_motivacion',
        'Internet_Access': 'acceso_internet',
        'Tutoring_Sessions': 'sesiones_tutoria',
        'Family_Income': 'ingresos_familiares',
        'Teacher_Quality': 'calidad_docente',
        'School_Type': 'tipo_escuela',
        'Peer_Influence': 'influencia_companeros',
        'Physical_Activity': 'actividad_fisica',
        'Learning_Disabilities': 'discapacidad_aprendizaje',
        'Parental_Education_Level': 'nivel_educativo_parental',
        'Distance_from_Home': 'distancia_casa',
        'Gender': 'genero',
        'Exam_Score': 'calificacion_examen',
        'nama_student': 'nombre_estudiante',
        'degree': 'grado',
        'behavior': 'conducta'
    }, inplace=True)

    # Convertir notas a escala 0-20
    if 'calificacion_examen' in df.columns:
        df['calificacion_examen'] = df['calificacion_examen'] * 0.2

    if 'puntuaciones_previas' in df.columns:
        df['puntuaciones_previas'] = df['puntuaciones_previas'] * 0.2

    if 'conducta' in df.columns:
        df['conducta'] = df['conducta'] * 0.2

    # Filtrar columnas seleccionadas para el modelo
    columnas_usadas = [
        'calificacion_examen', 'puntuaciones_previas', 'asistencia', 'horas_estudio', 'sesiones_tutoria', 'conducta'
    ]
    df = df[columnas_usadas]

    # Eliminar duplicados exactos
    df.drop_duplicates(inplace=True)

    # Imputación de valores nulos
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ['int64', 'float64']:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])

    # Tratamiento de outliers (Regla de Tukey)
    def remover_outliers_tukey(df, columnas):
        for col in columnas:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lim_inf = q1 - 1.5 * iqr
            lim_sup = q3 + 1.5 * iqr
            df = df[(df[col] >= lim_inf) & (df[col] <= lim_sup)]
        return df

    # Remover outliers para todas las columnas numéricas
    columnas_numericas = df.select_dtypes(include=['int64', 'float64']).columns
    df = remover_outliers_tukey(df, columnas_numericas)

    # Codificación de variables categóricas
    df = pd.get_dummies(df, drop_first=True)

    # Normalización de datos
    if normalizar and columnas_a_normalizar is not None:
        # Verificar que las columnas a normalizar son numéricas
        columnas_a_normalizar = [col for col in columnas_a_normalizar if
                                 col in df.select_dtypes(include=['int64', 'float64']).columns]
        scaler = MinMaxScaler()
        df[columnas_a_normalizar] = scaler.fit_transform(df[columnas_a_normalizar])

    return df

