from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

app = Flask(__name__)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

# Permitir solicitudes desde cualquier origen
CORS(app)

# Rutas para el CRUD de la entidad reserva
app.route('/', methods=['GET'])(index)
app.route('/api/reservas/', methods=['POST'])(create_reserva)
app.route('/api/reservas/', methods=['GET'])(get_all_reservas)
app.route('/api/reservas/<int:reserva_id>', methods=['GET'])(get_reserva)
app.route('/api/reservas/<int:reserva_id>', methods=['PUT'])(update_reserva)
app.route('/api/reservas/<int:reserva_id>', methods=['DELETE'])(delete_reserva)

if __name__ == '__main__':
    app.run(debug=True)
