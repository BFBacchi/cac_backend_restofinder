from app.database import get_db

class Reserva:
    def __init__(self, idreserva=None, Mail=None, Telefono=None, Fecha_reserva=None, Nombre=None, Numero_de_personas=None, Hora_de_reserva=None, Restaurante=None):
        self.idreserva = idreserva
        self.Mail = Mail
        self.Telefono = Telefono
        self.Fecha_reserva = Fecha_reserva
        self.Nombre = Nombre
        self.Numero_de_personas = Numero_de_personas
        self.Hora_de_reserva = Hora_de_reserva
        self.Restaurante = Restaurante

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.idreserva:
            cursor.execute("""
                UPDATE reserva SET Mail = %s, Telefono = %s, Fecha_reserva = %s, Nombre = %s, Numero_de_personas = %s, Hora_de_reserva = %s, Restaurante = %s
                WHERE idreserva = %s
            """, (self.Mail, self.Telefono, self.Fecha_reserva, self.Nombre, self.Numero_de_personas, self.Hora_de_reserva, self.Restaurante, self.idreserva))
        else:
            cursor.execute("""
                INSERT INTO reserva (Mail, Telefono, Fecha_reserva, Nombre, Numero_de_personas, Hora_de_reserva, Restaurante) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (self.Mail, self.Telefono, self.Fecha_reserva, self.Nombre, self.Numero_de_personas, self.Hora_de_reserva, self.Restaurante))
            self.idreserva = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reserva")
        rows = cursor.fetchall()
        reservas = [Reserva(idreserva=row[0], Mail=row[1], Telefono=row[2], Fecha_reserva=row[3], Nombre=row[4], Numero_de_personas=row[5], Hora_de_reserva=row[6], Restaurante=row[7]) for row in rows]
        cursor.close()
        return reservas

    @staticmethod
    def get_by_id(reserva_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reserva WHERE idreserva = %s", (reserva_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reserva(idreserva=row[0], Mail=row[1], Telefono=row[2], Fecha_reserva=row[3], Nombre=row[4], Numero_de_personas=row[5], Hora_de_reserva=row[6], Restaurante=row[7])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reserva WHERE idreserva = %s", (self.idreserva,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'idreserva': self.idreserva,
            'Mail': self.Mail,
            'Telefono': self.Telefono,
            'Fecha_reserva': self.Fecha_reserva.strftime('%Y-%m-%d') if self.Fecha_reserva else None,
            'Nombre': self.Nombre,
            'Numero_de_personas': self.Numero_de_personas,
            'Hora_de_reserva': str(self.Hora_de_reserva),  # Convertir timedelta a cadena o adaptar según sea necesario
            'Restaurante': self.Restaurante,
        }