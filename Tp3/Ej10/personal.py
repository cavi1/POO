from abc import ABC
import random
class Personal(ABC):
    def __init__(self,nombre,sector):
        self._antiguedad=random.randint(0,30)
        self._sector=sector
        self.__horas_trabajadas_mes=random.randint(0,100)
    
    def get_horas_mensuales_trabajadas(self):
        return self.__horas_trabajadas_mes
    