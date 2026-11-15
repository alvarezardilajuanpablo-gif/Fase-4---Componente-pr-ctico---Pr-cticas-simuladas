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
        print("2. Consultar cliente")
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

                #Aporte de Juan: Registra el cliente en la lista compartida
                cliente.registrar_cliente()

                # Muestra el resultado del registro de prueba.
                print("\nCliente creado correctamente:")
                print(cliente.mostrar_informacion())

                #Aporte de Juan: se elimina el mensaje anterior por que ahora los clientes si se almacenan en la lista compartida

            except ErrorValidacion as error:
                # Muestra el error sin finalizar el programa.
                print(f"Error de validación: {error}")

        # Aporte de Juan: Implementamos la consulta de clientes por documento 
        elif opcion == 2:
            try:
                #Solicita el documento del cliente que se desea buscar
                identificador = input("Ingrese el documento del cliente: ")

                #Busca el cliente utilizando su identificador
                cliente = Cliente.buscar_cliente(identificador) 

                #Muestra la informacion del cliente encontrado
                print("\nCliente encontrado:")
                print(cliente.mostrar_informacion())

            except ErrorValidacion as error:
                #Muestra el error si el cliente no existe o hay datos invalidos
                print(f"Error de consulta: {error}")                                 
                                                                           

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
