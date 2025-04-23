# src/config.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://postgres:james@localhost:5432/eduforge"  # Asegúrate de que la URL esté correcta

# Crear el engine de SQLAlchemy para conectar con PostgreSQL
engine = create_engine(DATABASE_URL)

# Crear la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para los modelos
Base = declarative_base()

# Verificar la conexión a la base de datos
def check_db_connection():
    try:
        # Establecer una conexión y ejecutar la consulta correctamente
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexión a la base de datos exitosa!")
    except OperationalError as e:
        print(f"Error al conectarse a la base de datos: {e}")

# Llamamos a esta función para verificar la conexión
check_db_connection()
