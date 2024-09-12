#atributos comunes: nombre, club, pais, atributos, quimica
#metodo comun: imprmir toda la info de la carta exceptuando la habilidad especial


from abc import ABC, abstractmethod

import random

class Carta(ABC):

    def __init__(self, nombre, club, pais):
        self._nombre=nombre
        self._club=club
        self._pais=pais
        self.set_atributos()
        self.calcular_valoracion()
    
    def carta_to_string(self):
        return f"{self._nombre}\n{self._club}\n{self._pais}\n{self._valoracion}\nvelocidad {self._velocidad} tiro {self._tiro}\nregate {self._regate} defensa {self._defensa}\npase {self._pase} fisico {self._fisico}"

    def set_atributos(self, min, max):
        self._velocidad=random.randint(min,max)
        self._tiro=random.randint(min,max)
        self._regate=random.randint(min,max)
        self._defensa=random.randint(min,max)
        self._pase=random.randint(min,max)
        self._fisico=random.randint(min,max)
        
    def calcular_valoracion(self):
        self._valoracion=(self._velocidad+self._tiro+self._regate+self._defensa+self._pase+self._fisico) // 6
    
    def calcular_quimica(self, pais_fav_plantilla, club_fav_plantilla):
        if pais_fav_plantilla==self._pais and club_fav_plantilla==self._club:
            self._quimica=100
        elif pais_fav_plantilla==self._pais or club_fav_plantilla==self._club:
            self._quimica=80
        else:
            self._quimica=0
    
    