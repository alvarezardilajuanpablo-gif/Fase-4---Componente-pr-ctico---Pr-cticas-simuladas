print("Software FJ")
print("Sistema de Gestión de Clientes, Servicios y Reservas")

from cliente import Cliente
from servicio import Servicio
from reserva import Reserva
from excepciones import ErrorValidacion

clientes = []
servicios = []
reservas = []

def buscar_cliente(identificador):
    for c in clientes:
        if c.identificador == identificador:
            return c
    return None

def buscar_servicio(identificador):
    for s in servicios:
        if s.identificador == identificador:
            return s
    return None

def iniciar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar cliente")
        print("2. Consultar clientes")
        print("3. Registrar servicio")
        print("4. Consultar servicios")
        print("5. Realizar reserva")
        print("6. Consultar reservas")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

        if opcion == 1:
            try:
                identificador = input("Ingrese el identificador: ")
                nombre = input("Ingrese el nombre: ")
                correo = input("Ingrese el correo: ")
                telefono = input("Ingrese el teléfono, solo números: ")
                cliente = Cliente(identificador, nombre, correo, telefono)
                clientes.append(cliente)
                print("\nCliente creado correctamente:")
                print(cliente.mostrar_informacion())
            except ErrorValidacion as error:
                print(f"Error de validación: {error}")

        elif opcion == 2:
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for c in clientes:
                    print("\n---")
                    print(c.mostrar_informacion())

        elif opcion == 3:
            try:
                identificador = input("Ingrese ID del servicio: ")
                nombre = input("Ingrese nombre del servicio: ")
                precio = input("Ingrese precio: ")
                duracion = input("Ingrese duración en minutos: ")
                servicio = Servicio(identificador, nombre, precio, duracion)
                servicios.append(servicio)
                print("\nServicio creado correctamente:")
                print(servicio.mostrar_informacion())
            except ErrorValidacion as error:
                print(f"Error de validación: {error}")

        elif opcion == 4:
            if not servicios:
                print("No hay servicios registrados.")
            else:
                for s in servicios:
                    print("\n---")
                    print(s.mostrar_informacion())

        elif opcion == 5:
            try:
                if not clientes or not servicios:
                    print("Debe registrar al menos un cliente y un servicio primero.")
                    continue
                identificador = input("Ingrese ID de la reserva: ")
                id_cliente = input("Ingrese ID del cliente: ")
                id_servicio = input("Ingrese ID del servicio: ")
                fecha = input("Ingrese fecha AAAA-MM-DD: ")
                hora = input("Ingrese hora HH:MM: ")

                cliente = buscar_cliente(id_cliente)
                if cliente is None:
                    print("Error: cliente no encontrado.")
                    continue
                servicio = buscar_servicio(id_servicio)
                if servicio is None:
                    print("Error: servicio no encontrado.")
                    continue

                reserva = Reserva(identificador, cliente, servicio, fecha, hora)
                reservas.append(reserva)
                print("\nReserva creada correctamente:")
                print(reserva.mostrar_informacion())
            except ErrorValidacion as error:
                print(f"Error de validación: {error}")

        elif opcion == 6:
            if not reservas:
                print("No hay reservas registradas.")
            else:
                for r in reservas:
                    print("\n---")
                    print(r.mostrar_informacion())

        elif opcion == 7:
            print("Gracias por usar el sistema.")
            break
        else:
            print("Error: seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    iniciar_menu()