print("Software FJ")
print("Sistema de Gestión de Clientes, Servicios y Reservas")

from cliente import Cliente
# Aporte de Jhon: Importa las clases Servicio y Reserva para servicios y Reservas
from servicio import Servicio
from reserva import Reserva
# Aporte de Jully: corrección de importación para capturar cliente no encontrado.
from excepciones import ErrorValidacion, ClienteNoEncontrado

# Aporte de Jully: corrección para usar la lista compartida de clientes
# registrada dentro de la clase Cliente.
# Aporte de Jhon: Listas para guardar servicios y reservas
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
       # Aporte de Jhon: Opciones para servicios y reservas
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
                                                                           
    # Aporte de Jhon: Registra un servicio nuevo en la lista
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
# Aporte de Jhon: Crea una reserva asociada a un cliente y un servicio
elif opcion == 5:
            try:
                if not Cliente.clientes or not servicios:
                    print("Debe registrar al menos un cliente y un servicio primero.")
                    continue

                identificador = input("Ingrese ID de la reserva: ")
                id_cliente = input("Ingrese ID del cliente: ")
                id_servicio = input("Ingrese ID del servicio: ")
                fecha = input("Ingrese fecha AAAA-MM-DD: ")
                hora = input("Ingrese hora HH:MM: ")

                try:
                    cliente = Cliente.buscar_cliente(id_cliente)
                except ClienteNoEncontrado:
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
