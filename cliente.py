from entidad import Entidad
from excepciones import ErrorValidacion

# Aporte de Jully: importa la validación general de texto.
from excepciones import validar_campo


#Creamos la clase Cliente con sus atributos y metodos como una clase hija de la clase Entidad, la cual se encargara de hacer validaciones robustas y encapsulación de datos personales
class Cliente (Entidad):
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        # Aporte de Jully: valida los datos antes de almacenarlos.
        self.__nombre = self.validar_nombre(nombre)
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)

    @staticmethod
    def validar_nombre(nombre):
        """Comprueba que el nombre sea un texto no vacío."""

        # Valida y devuelve el nombre sin espacios exteriores.
        return validar_campo(nombre, "nombre")

    # Aporte de Jully: validación básica del correo.
    @staticmethod
    def validar_correo(correo):
        """Realiza una comprobación básica del formato del correo."""

        # Comprueba que el correo sea texto y no esté vacío.
        correo = validar_campo(correo, "correo")

        # Revisa que tenga una sola arroba y que no contenga espacios.
        if correo.count("@") != 1 or any(
            caracter.isspace() for caracter in correo
        ):
            raise ErrorValidacion(
                "El correo debe tener una sola arroba y no contener espacios."
            )

        # Separa el usuario del dominio.
        usuario, dominio = correo.split("@")

        # Comprueba que ambas partes existan y que el dominio tenga un punto.
        if (
            not usuario
            or "." not in dominio
            or any(not parte for parte in dominio.split("."))
        ):
            raise ErrorValidacion(
                "Ingrese un correo con formato usuario@dominio.com."
            )

        # Devuelve el correo validado.
        return correo

    # Aporte de Jully: validación del teléfono.
    @staticmethod
    def validar_telefono(telefono):
        """Comprueba que el teléfono contenga únicamente dígitos del 0 al 9."""

        # Comprueba que el teléfono sea texto y no esté vacío.
        telefono = validar_campo(telefono, "teléfono")

        # Revisa que todos los caracteres sean dígitos del 0 al 9.
        if not telefono.isascii() or not telefono.isdigit():
            raise ErrorValidacion(
                "El teléfono debe contener solo números, sin espacios ni signos."
            )

        # Devuelve el teléfono validado.
        return telefono

    # Aporte de Jully: implementa el método definido en Entidad.
    def mostrar_informacion(self):
        """Devuelve un resumen de los datos del cliente."""

        # Construye el texto con los datos almacenados.
        return (
            f"Identificador: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )


