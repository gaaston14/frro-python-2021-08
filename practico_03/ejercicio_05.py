"""Propiedades"""


class Auto:
    def __init__(self,nombre,precio):
        self.__nombre = nombre
        self.__precio= precio

    @property
    def nombre(self ):
        return self.__nombre.capitalize()


    @property
    def precio(self) :
        return round(self.__precio,2)
    @precio.setter
    def precio(self, value) :
        self.__precio=value
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    # Completar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.nombre == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Auto:
    """Re-Escribir utilizando DataClasses"""
    __nombre:str
    __precio:float

    @property
    def nombre(self):
        return self.__nombre.capitalize()
    @property
    def precio(self):
        return round(self.__precio,2)
    @precio.setter
    def precio(self,value):
        self.__precio=value
    # Completar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.nombre == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
