from entidad import Entidad
from excepciones import ErrorValidacion, validar_campo

# Aporte de Jhon: clase Servicio
class Servicio(Entidad):
    def __init__(self, identificador, nombre, precio, duracion_minutos):
        super().__init__(identificador)
        self.__nombre = validar_campo(nombre, "nombre del servicio")
        self.__precio = self.validar_precio(precio)
        self.__duracion_minutos = self.validar_duracion(duracion_minutos)

    @staticmethod
    def validar_precio(precio):
        try:
            precio = float(precio)
        except (ValueError, TypeError):
            raise ErrorValidacion("El precio debe ser un número.")
        if precio <= 0:
            raise ErrorValidacion("El precio debe ser mayor a 0.")
        return precio

    @staticmethod
    def validar_duracion(duracion):
        try:
            duracion = int(duracion)
        except (ValueError, TypeError):
            raise ErrorValidacion("La duración debe ser un número entero.")
        if duracion <= 0:
            raise ErrorValidacion("La duración debe ser mayor a 0 minutos.")
        return duracion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def duracion_minutos(self):
        return self.__duracion_minutos

    def mostrar_informacion(self):
        return (
            f"Identificador: {self.identificador}\n"
            f"Servicio: {self.__nombre}\n"
            f"Precio: ${self.__precio}\n"
            f"Duración: {self.__duracion_minutos} min"
        )