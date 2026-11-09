from abc import ABC, abstractmethod

# Aporte de Jully: importa la función de validación.
from excepciones import validar_campo


# Aporte de Jully: valida el identificador de las entidades.
def validar_identificador(identificador):
    """Comprueba que el identificador sea un texto no vacío."""

    # Utiliza la validación general y devuelve el resultado.
    return validar_campo(identificador, "identificador")


#Creamos la clase abstracta Entidad con sus atributos y métodos, la cual representa entidades generales del sistema
class Entidad (ABC):
    def __init__(self, identificador):
        # Aporte de Jully: valida el identificador antes de guardarlo.
        self.identificador = validar_identificador(identificador)

    @abstractmethod
    def mostrar_informacion(self):
        pass
        
