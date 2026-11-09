from conexiones import Session
from modelos import Reserva

def cancelar_reserva(id_reserva:int):

    with Session.begin() as session:

        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            print(f"error: no se encontro una reserva con el id: {id_reserva}")
            return

        reserva.sala.disponible = True

        session.delete(reserva)

    print(f"reserva {id_reserva} cancelada")

    

