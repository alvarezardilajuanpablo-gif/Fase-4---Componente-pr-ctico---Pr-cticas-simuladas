print("Software FJ")
print("Sistema de Gestión de Clientes, Servicios y Reservas")

# Aporte de Jully: importa la clase Cliente y el error de validación.
from cliente import Cliente
from excepciones import ErrorValidacion


# Aporte de Jully: menú inicial para probar el registro de clientes.
def iniciar_menu():
    """Muestra el menú y controla errores de entrada."""

    # Mantiene el menú activo hasta seleccionar la opción de salida.
    while True:
        # Presenta las opciones disponibles.
        print("\nMenú de opciones:")
        print("1. Registrar cliente")
        print("2. Consultar cliente — pendiente")
        print("3. Realizar reserva — pendiente")
        print("4. Salir")

        try:
            # Convierte la opción ingresada a un número entero.
            opcion = int(input("Seleccione una opción: "))

        except ValueError:
            # Informa el error cuando la entrada no es un número entero.
            print("Error: debe ingresar un número entero.")

            # Vuelve a mostrar el menú.
            continue

        # Ejecuta la opción de registro.
        if opcion == 1:
            try:
                # Solicita los datos necesarios para crear el cliente.
                identificador = input("Ingrese el identificador: ")
                nombre = input("Ingrese el nombre: ")
                correo = input("Ingrese el correo: ")
                telefono = input("Ingrese el teléfono, solo números: ")

                # Crea el cliente y ejecuta las validaciones.
                cliente = Cliente(
                    identificador, nombre, correo, telefono
                )

                # Muestra el resultado del registro de prueba.
                print("\nCliente creado correctamente:")
                print(cliente.mostrar_informacion())

                # Aclara el alcance de esta primera versión.
                print("Nota: todavía no se guarda en un listado o archivo.")

            except ErrorValidacion as error:
                # Muestra el error sin finalizar el programa.
                print(f"Error de validación: {error}")

        # Deja indicada la función que continuará el equipo.
        elif opcion == 2:
            print("La consulta de clientes está pendiente de implementación.")

        # Deja indicada la función que continuará el equipo.
        elif opcion == 3:
            print("La gestión de reservas está pendiente de implementación.")

        # Finaliza el menú cuando el usuario lo solicita.
        elif opcion == 4:
            print("Gracias por usar el sistema.")
            break

        # Informa cuando el número no corresponde a una opción.
        else:
            print("Error: seleccione una opción del 1 al 4.")


# Inicia el menú cuando se ejecuta este archivo directamente.
if __name__ == "__main__":
    iniciar_menu()
