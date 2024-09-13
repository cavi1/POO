
import random
from carta import Carta

class Carta_bronce_especial(Carta):

    def __init__(self, nombre, club, pais, habilidad_especial):
        super().__init__(nombre, club, pais)        
        self.__habilidad_especial=habilidad_especial
        
    def set_atributos(self):
        super().set_atributos(49,65)
        self._velocidad+=2
        self._tiro+=2
        self._regate+=2
        self._fisico+=2
        self._defensa+=2
        self._pase+=2
    
    def carta_to_string(self):
        return f"Habilidad Especial: \n{self.__habilidad_especial}\n{super().carta_to_string()}"
        