from entidad import Entidad
from excepciones import ErrorValidacion

#Creamos la clase Cliente con sus atributos y metodos como una clase hija de la clase Entidad, la cual se encargara de hacer validaciones robustas y encapsulación de datos personales
class Cliente (Entidad):
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    @staticmethod
    def validar_nombre(nombre):
        pass




