import os
import mysql.connector
from flask import g, current_app
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306)
}

# Función para obtener la conexión a la base de datos
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        create_reservas_table()

# Función para crear la tabla 'reserva'
def create_reservas_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `reserva` (
          `idreserva` int NOT NULL AUTO_INCREMENT,
          `Mail` varchar(100) NOT NULL,
          `Telefono` int NOT NULL,
          `Fecha_reserva` date NOT NULL,
          `Nombre` varchar(100) DEFAULT NULL,
          `Numero de personas` int NOT NULL,
          `Hora de reserva` time NOT NULL,
          `Restaurante` varchar(45) DEFAULT NULL,
          PRIMARY KEY (`idreserva`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """)
    db.commit()
    cursor.close()
