from flask import jsonify, request
from app.models import Reserva 

def index():
    return jsonify({'message': 'Hello World API Restofinder'})

def create_reserva():
    data = request.json
    new_reserva = Reserva(
        Mail=data.get('Mail'), 
        Telefono=data.get('Telefono'), 
        Fecha_reserva=data.get('Fecha_reserva'), 
        Nombre=data.get('Nombre'), 
        Numero_de_personas=data.get('Numero_de_personas'), 
        Hora_de_reserva=data.get('Hora_de_reserva'), 
        Restaurante=data.get('Restaurante')
    )
    new_reserva.save()
    return jsonify({'message': 'Reserva creada correctamente'}), 201

def get_all_reservas():
    reservas = Reserva.get_all()
    return jsonify([reserva.serialize() for reserva in reservas])

def get_reserva(reserva_id):
    reserva = Reserva.get_by_id(reserva_id)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    return jsonify(reserva.serialize())

def update_reserva(reserva_id):
    reserva = Reserva.get_by_id(reserva_id)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    data = request.json
    reserva.Mail = data.get('Mail')
    reserva.Telefono = data.get('Telefono')
    reserva.Fecha_reserva = data.get('Fecha_reserva')
    reserva.Nombre = data.get('Nombre')
    reserva.Numero_de_personas = data.get('Numero_de_personas')
    reserva.Hora_de_reserva = data.get('Hora_de_reserva')
    reserva.Restaurante = data.get('Restaurante')
    reserva.save()
    return jsonify({'message': 'Reserva actualizada correctamente'})

def delete_reserva(reserva_id):
    reserva = Reserva.get_by_id(reserva_id)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404
    reserva.delete()
    return jsonify({'message': 'Reserva eliminada correctamente'})
