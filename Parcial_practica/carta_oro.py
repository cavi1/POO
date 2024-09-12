from carta import Carta

class Carta_oro(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        
        
    def set_atributos(self):
        porcentaje=5
        super().set_atributos(74,90)
        self._velocidad+=int((self._velocidad*porcentaje)/100)
        self._tiro+=int((self._tiro*porcentaje)/100)
        self._regate+=int((self._regate*porcentaje)/100)
        self._fisico+=int((self._fisico*porcentaje)/100)
        self._defensa+=int((self._defensa*porcentaje)/100)
        self._pase+=int((self._pase*porcentaje)/100)
        
    