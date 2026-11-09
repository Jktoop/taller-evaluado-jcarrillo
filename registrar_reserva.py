from conexiones import Session
from modelos import Sala, Reserva


def registrar_reserva(estudiante:str, sala_id:int, fecha:str):
    nombre_estudiante = estudiante.strip
    fecha_reserva = fecha.strip

    if not nombre_estudiante:
        print("error: el nombre del estudiante no puede estar vacio")
        return

    if not fecha_reserva:
        print("error: la fecha de reserva no puede estar vacia")
        return


    with Session.begin() as session:
            
        sala = session.get(Sala, sala_id)
    
        if sala is None:
            print(f"error: no se encontro una sala con el id: {sala_id}.")
            return
    
        if not sala.disponible:
            print(f"error: la sala '{sala.nombre}' ya se encuentra ocupada.")
            return
    
            
        nueva_reserva = Reserva(
            estudiante=nombre_estudiante,
            sala_id=sala_id,
            fecha=fecha_reserva
        )
        session.add(nueva_reserva)

        sala.disponible = False
    
    print(f"Reserva registrada exitosamente para {nombre_estudiante} en la sala '{sala.nombre}'.")
    

    