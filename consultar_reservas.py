from sqlalchemy import select
from conexiones import Session
from modelos import Reserva

def consultar_reservas():
    with Session() as session:
        consulta = select(Reserva)
        reservas = session.scalars(consulta).all()

        print("\n================ LISTADO DE RESERVAS ================")
        if not reservas:
            print("No existen reservas registradas.")
            print("=====================================================")
            return

        for reserva in reservas:
            print("-----------------------------------------------------")
            print(f"ID Reserva   : {reserva.id}")
            print(f"Estudiante   : {reserva.estudiante}")
            print(f"Sala         : {reserva.sala.nombre}")
            print(f"Fecha        : {reserva.fecha}")

        print("=====================================================")