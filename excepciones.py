#Creamos una clase de excepción para definir errores personalizados
class ErrorValidacion(Exception):
    """Error generado cuando un dato no cumple con las condiciones requeridas"""
    pass
# Aporte de Jully: excepciones adicionales para validar datos y reservas

class DatoInvalido(Exception):
    """Error cuando el usuario ingresa un dato vacío o incorrecto."""
    pass

class ClienteNoEncontrado(Exception):
    """Error cuando el cliente buscado no existe en el sistema."""
    pass

class ReservaInvalida(Exception):
    """Error cuando la reserva no cumple las condiciones requeridas."""
    pass

# Función para validar que un campo no esté vacío
def validar_campo(valor, nombre_campo):
    # Verifica si el valor está vacío o contiene solamente espacios
    if not valor or valor.strip() == "":
        # Genera un error si el campo está vacío
        raise DatoInvalido(f"El campo '{nombre_campo}' no puede estar vacío.")
    
    # Devuelve el valor sin espacios adicionales
    return valor.strip()
