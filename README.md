# Proyecto de Gestión de Reservas

Este proyecto es un backend para la gestión de reservas utilizando Flask. A continuación se detallan las instrucciones para instalar y ejecutar el proyecto en local, así como los endpoints disponibles.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio:**

   ```sh
   git clone https://github.com/BFBacchi/cac_backend_restofinder.git
   cd <NOMBRE_DEL_DIRECTORIO>

2. **Crear y activar un entorno virtual:**

   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

3. **Instalar las dependencias:**

   pip install -r requirements.txt

4. **Configurar la base de datos:**

  Asegúrate de tener configurada la base de datos adecuadamente en el archivo app/database.py.
  Puedes importar el archivo sql desde la carpeta /db/reserva.sql

5. **Endpoints**

*Obtener todas las reservas*
URL: /api/reservas/
Método: GET
Descripción: Obtiene una lista de todas las reservas.
Respuesta Exitosa: 200 OK

*crear una nueva reserva*
URL: /api/reservas/
Método: POST
Descripción: Crea una nueva reserva.
Cuerpo de la Solicitud:
{
  "Mail": "example@mail.com",
  "Telefono": "123456789",
  "Fecha_reserva": "2024-07-01",
  "Nombre": "John Doe",
  "Numero_de_personas": 2,
  "Hora_de_reserva": "19:00",
  "Restaurante": "Dadá Bistro"
}

*Obtener una reserva por ID*
URL: /api/reservas/<int:reserva_id>
Método: GET
Descripción: Obtiene los detalles de una reserva específica por ID.
Respuesta Exitosa: 200 OK

*Actualizar una reserva por ID*
URL: /api/reservas/<int:reserva_id>
Método: PUT
Descripción: Actualiza los detalles de una reserva específica por ID.
Cuerpo de la Solicitud:

{
  "Mail": "newexample@mail.com",
  "Telefono": "987654321",
  "Fecha_reserva": "2024-07-02",
  "Nombre": "Jane Doe",
  "Numero_de_personas": 4,
  "Hora_de_reserva": "20:00",
  "Restaurante": "Iñaki"
}

*Eliminar una reserva por ID*

URL: /api/reservas/<int:reserva_id>
Método: DELETE
Descripción: Elimina una reserva específica por ID.
Respuesta Exitosa: 200 OK

{
  "message": "Reserva eliminada exitosamente"
}

*Deploy en pythonanywhere:*  [backend](http://bfbmahakala.pythonanywhere.com/)