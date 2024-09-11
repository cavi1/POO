from plantilla import Plantilla
from carta import Carta

class Carta_bronce_especial(Carta):

    def __init__(self, nombre, club, pais, habilidad_especial):
        super().__init__(nombre, club, pais, habilidad_especial)        
        self.set_atributos_bronce()
        self.calcular_quimica()
        self.calcular_valoracion()
        
        
    def set_atributos_bronce(self):
        super().set_atributos(49,65)
        self._velocidad+=2
        self._tiro+=2
        self._regate+=2
        self._fisico+=2
        self._defensa+=2
        self._pase+=2
        
    def calcular_quimica(self):
        if Plantilla().get_pais_fav==self._pais and Plantilla().get_equipo_fav==self._club:
            self._quimica=100
        elif Plantilla().get_pais_fav==self._pais or Plantilla().get_equipo_fav==self._club:
            self._quimica=80
        else:
            self._quimica=0
    
    def carta_to_string(self):
        return f"{self._habilidad_especial}\n{super().carta_to_string()}"
        