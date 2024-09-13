from carta import Carta

class Carta_oro(Carta):
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        
        
    def set_atributos(self):
        super().set_atributos(74,90)
        self._velocidad=int(min(90,self._velocidad+ self._velocidad*0.05))
        self._tiro=int(min(90,self._tiro+ self._tiro*0.05))
        self._regate=int(min(90,self._regate+ self._regate*0.05))
        self._fisico=int(min(90,self._fisico+ self._fisico*0.05))
        self._defensa=int(min(90,self._defensa+ self._defensa*0.05))
        self._pase=int(min(90,self._pase+ self._pase*0.05))
        
    