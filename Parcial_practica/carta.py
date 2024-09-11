#atributos comunes: nombre, club, pais, atributos, quimica
#metodo comun: imprmir toda la info de la carta exceptuando la habilidad especial


from abc import ABC, abstractmethod
import random

class Carta(ABC):

    def __init__(self, nombre, club, pais, velocidad, tiro, regate, defensa, pase, fisico, quimica, valoracion):
        self._nombre=nombre
        self._club=club
        self._pais=pais
        self._quimica=self.calcular_quimica()
        self._valoracion=self.calcular_valoracion()
        self.set_atributos()
        
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
    
    @abstractmethod 
    def calcular_quimica(self):
        pass

    
    