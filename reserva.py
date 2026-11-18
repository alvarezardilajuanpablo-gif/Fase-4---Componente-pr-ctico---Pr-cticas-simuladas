from datetime import datetime
from entidad import Entidad
from excepciones import ReservaInvalida, validar_campo

# Aporte de Jhon: clase Reserva
class Reserva(Entidad):
    def __init__(self, identificador, cliente, servicio, fecha, hora):
        super().__init__(identificador)
        self.__cliente = cliente
        self.__servicio = servicio
        self.__fecha = self.validar_fecha(fecha)
        self.__hora = self.validar_hora(hora)

    @staticmethod
    def validar_fecha(fecha):
        fecha = validar_campo(fecha, "fecha")
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise ReservaInvalida("La fecha debe tener formato AAAA-MM-DD, ejemplo: 2026-11-20.")
        return fecha

    @staticmethod
    def validar_hora(hora):
        hora = validar_campo(hora, "hora")
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            raise ReservaInvalida("La hora debe tener formato HH:MM, ejemplo: 14:30.")
        return hora

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.__cliente.mostrar_informacion()}\n"
            f"Servicio: {self.__servicio.nombre} - ${self.__servicio.precio}\n"
            f"Fecha: {self.__fecha} Hora: {self.__hora}"
        )