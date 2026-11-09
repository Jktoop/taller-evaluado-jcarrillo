#nombre: Joaquin carrillo
from conexiones import engine
import crear_tabla
from inserta import insertar_sala
from consultar_sala import consular_salas
from registrar_reserva import registrar_reserva
from consultar_reservas import consultar_reservas
from cancelar_reserva import cancelar_reserva

def probar_conexion():
    with engine.connect() as con:
        print("Conexión a SQLite (reservas.db) exitosa.")

def mostrar_menu():
    print("========== sistema de reservas de salas ==========")
    print("1. Registrar sala")
    print("2. Consultar salas")
    print("3. Registrar reserva")
    print("4. Consultar reservas")
    print("5. Cancelar reserva")
    print("0. Salir")
    print("=================================================")

def opcion_registrar_sala():
    print("\n--------- REGISTRAR SALA ---------")
    nombre = input("ingrese el nombre de la sala: ").strip()
    try:
        capacidad = int(input("ingrese la capacidad de la sala: "))
        if not nombre:
            print("error: debe ingresar un nombre vslido.")
            return
        if capacidad <= 0:
            print("error: La capacidad debe ser un número entero mayor a cero.")
            return

        insertar_sala(nombre, capacidad)
    except ValueError:
        print("errorr: Ingrese un valor numérico entero para la capacidad.")

def opcion_registrar_reserva():
    print("\n--------- REGISTRAR RESERVA ---------")
    try:
        sala_id = int(input("ingrese el ID de la sala: "))
        if sala_id <= 0:
            print("error: el ID de la sala debe ser un numero positivo.")
            return

        estudiante = input("ingrese el nombre del estudiante: ").strip()
        fecha = input("ingrese la fecha (AAAA-MM-DD): ").strip()

        if not estudiante or not fecha:
            print("error: el nombre del estudiante y la fecha son obligatorios.")
            return

        registrar_reserva(estudiante, sala_id, fecha)
    except ValueError:
        print("error: ingrese un ID numérico válido.")

def opcion_cancelar_reserva():
    print("\n--------- CANCELAR RESERVA ---------")
    try:
        id_reserva = int(input("ingrese el ID de la reserva a cancelar: "))
        if id_reserva <= 0:
            print("error: El ID de la reserva debe ser un número positivo.")
            return

        confirmar = input(f"¿seguro que desea cancelar la reserva #{id_reserva}? (S/N): ")
        if confirmar.strip().upper() == "S":
            cancelar_reserva(id_reserva)
        else:
            print("cancelación abortada por el usuario.")
    except ValueError:
        print("errro: Ingrese un ID numérico válido.")

def main():
    probar_conexion()
    while True:
        mostrar_menu()
        opcion = input("seleccione una opción: ").strip()

        if opcion == "1":
            opcion_registrar_sala()
        elif opcion == "2":
            consular_salas()
        elif opcion == "3":
            opcion_registrar_reserva()
        elif opcion == "4":
            consultar_reservas()
        elif opcion == "5":
            opcion_cancelar_reserva()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()