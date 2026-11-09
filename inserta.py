from conexiones import Session
from modelos import Sala

def insertar_sala(nombre: str, capacidad: int):
    nombre_limpio = nombre.strip()

    if not nombre_limpio:
        print("error: El nombre de la sala no puede estar vacío.")
        return

    if capacidad <= 0:
        print("errro: La capacidad debe ser mayor que cero.")
        return

    with Session.begin() as session:
        sala = Sala(
            nombre=nombre_limpio,
            capacidad=capacidad,
            disponible=True
        )
        session.add(sala)

    print(f"Sala '{nombre_limpio}' registrada con éxito.")