from abc import ABC, abstractmethod
import random
class Personal(ABC):
    def __init__(self,nombre,sector):
        self._antiguedad=random.randint(0,30)
        self._sector=sector
        self._horas_trabajadas_mes=random.randint(0,160)
    
    def get_horas_mensuales_trabajadas(self):
        return self._horas_trabajadas_mes
    
    @abstractmethod
    def get_categoria(self):
        pass
    