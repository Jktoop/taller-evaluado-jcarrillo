from sqlalchemy import select
from conexiones import Session
from modelos import Sala


def consular_salas():
    with Session() as session:
        consulta = select(Sala)
        salas = session.scalars(consulta).all()

        print("\n======== lista de salas =====")
        if not salas:
            print("no hay salas registradas")
            return

        for sala in salas:
            
            estado = "Disponible" if sala.disponible else "Ocupada"

            print(f"ID           : {sala.id}")
            print(f"Nombre       : {sala.nombre}")
            print(f"Capacidad    : {sala.capacidad} personas")
            print(f"Disponibilidad: {estado} ({sala.disponible})")

