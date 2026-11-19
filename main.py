
print("Software FJ")
print("Sistema de Gestión de Clientes, Servicios y Reservas")

from cliente import Cliente
# Aporte de Jhon: Importa las clases Servicio y Reserva
from servicio import Servicio
from reserva import Reserva
# Aporte de Jully: Importación de excepciones
from excepciones import ErrorValidacion, ClienteNoEncontrado

# Listas para guardar servicios y reservas
servicios = []
reservas = []


# Aporte de Jhon: Busca un servicio por su identificador
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

        # OPCIÓN 1: Registrar cliente
        if opcion == 1:
            try:
                identificador = input("Ingrese el identificador: ")
                nombre = input("Ingrese el nombre: ")
                correo = input("Ingrese el correo: ")
                telefono = input("Ingrese el teléfono, solo números: ")

                cliente = Cliente(
                    identificador, nombre, correo, telefono
                )

                # Aporte de Juan: Registra el cliente
                cliente.registrar_cliente()

                print("\nCliente creado correctamente:")
                print(cliente.mostrar_informacion())

            except ErrorValidacion as error:
                print(f"Error de validación: {error}")

        # OPCIÓN 2: Consultar clientes
        elif opcion == 2:
            try:
                identificador = input(
                    "Ingrese el documento del cliente: "
                )

                cliente = Cliente.buscar_cliente(identificador)

                print("\nCliente encontrado:")
                print(cliente.mostrar_informacion())

            except ErrorValidacion as error:
                print(f"Error de consulta: {error}")

        # OPCIÓN 3: Registrar servicio
        elif opcion == 3:
            try:
                identificador = input("Ingrese ID del servicio: ")
                nombre = input("Ingrese nombre del servicio: ")
                precio = input("Ingrese precio: ")
                duracion = input("Ingrese duración en minutos: ")

                servicio = Servicio(
                    identificador, nombre, precio, duracion
                )

                servicios.append(servicio)

                print("\nServicio creado correctamente:")
                print(servicio.mostrar_informacion())

            except ErrorValidacion as error:
                print(f"Error de validación: {error}")

        # OPCIÓN 4: Consultar servicios
        elif opcion == 4:
            if not servicios:
                print("No hay servicios registrados.")
            else:
                for s in servicios:
                    print("\n---")
                    print(s.mostrar_informacion())

        # OPCIÓN 5: Realizar reserva
        elif opcion == 5:
            try:
                # Verifica que existan clientes y servicios
                if not Cliente._clientes or not servicios:
                    print(
                        "Debe registrar al menos un cliente "
                        "y un servicio primero."
                    )
                    continue

                identificador = input("Ingrese ID de la reserva: ")
                id_cliente = input("Ingrese ID del cliente: ")
                id_servicio = input("Ingrese ID del servicio: ")
                fecha = input("Ingrese fecha AAAA-MM-DD: ")
                hora = input("Ingrese hora HH:MM: ")

                # Busca el cliente
                try:
                    cliente = Cliente.buscar_cliente(id_cliente)
                except ClienteNoEncontrado:
                    print("Error: cliente no encontrado.")
                    continue

                # Busca el servicio
                servicio = buscar_servicio(id_servicio)

                if servicio is None:
                    print("Error: servicio no encontrado.")
                    continue

                # Crea la reserva
                reserva = Reserva(
                    identificador,
                    cliente,
                    servicio,
                    fecha,
                    hora
                )


                print("\nReserva creada correctamente:")
                print(reserva.mostrar_informacion())

            except ErrorValidacion as error:
                print(f"Error de validación: {error}")

         # OPCIÓN 6: Consultar reservas
        elif opcion == 6:
            if not Reserva._reservas:
                print("\nNo hay reservas registradas.")
            else:
                print("\n===== RESERVAS REGISTRADAS =====")

                for r in Reserva._reservas:
                    print("\n----------------------------")
                    print(r.mostrar_informacion())

                print("\n===== FIN DE LAS RESERVAS =====")


        # OPCIÓN 7: Salir
        elif opcion == 7:
            print("Gracias por usar el sistema.")
            break

        else:
            print("Error: seleccione una opción del 1 al 7.")


# Ejecuta el programa principal
if __name__ == "__main__":
    iniciar_menu()

