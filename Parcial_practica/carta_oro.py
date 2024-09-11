from carta import Carta
from carta_bronce_especial import Carta_bronce_especial

class Carta_oro(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        self.set_atributos_oro()
        self.calcular_quimica()
        self.calcular_valoracion()
        
    def set_atributos_oro(self):
        porcentaje=5
        super().set_atributos(74,90)
        self._velocidad+=(self._velocidad*porcentaje)/100
        self._tiro+=(self._tiro*porcentaje)/100
        self._regate+=(self._regate*porcentaje)/100
        self._fisico+=(self._fisico*porcentaje)/100
        self._defensa+=(self._defensa*porcentaje)/100
        self._pase+=(self._pase*porcentaje)/100
        
    def calcular_quimica(self):
        return Carta_bronce_especial().calcular_quimica()
    