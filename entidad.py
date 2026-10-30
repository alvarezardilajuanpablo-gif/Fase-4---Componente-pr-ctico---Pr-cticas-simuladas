from abc import ABC, abstractmethod

#Creamos la clase abstracta Entidad con sus atributos y métodos, la cual representa entidades generales del sistema
class Entidad (ABC):
    def __init__(self, identificador):
        self.identificador = identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass
         


