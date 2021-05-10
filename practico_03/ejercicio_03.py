"""Dataclasses"""


class Persona:
    """Clase con los siguientes miembros:

    Atributos de instancia:
    - nombre: str
    - edad: int
    - sexo (H hombre, M mujer): str
    - peso: float
    - altura: float

    Métodos:
    - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
    """
    def __init__(self,nombre: str,edad: int,sexo: str,peso: float,altura: float):
        self.nombre: str = nombre
        self.edad: int = edad
        self.sexo: str = sexo
        self.peso: float = peso
        self.altura: float = altura
    def es_mayor_edad(self) ->bool:
        return self.edad >= 18
    # Completar


# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Persona:
    """Re-Escribir utilizando DataClasses"""
    nombre:str
    edad:int
    sexo:str
    peso:float
    altura: float
    # Completar
    def es_mayor_edad(self):
        return self.edad >=18

# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN
