from carta import Carta

class Carta_especial(Carta):
    def __init__(self,nombre,equipo,pais):
        super().__init__(nombre,equipo,pais)
        self.__habilidad_especial=habilidad_especial
        
    def set_atributos_especial(self):
        super().set_atributos(89,99)
        self._velocidad=min(99,self._velocidad+ self._velocidad*0.02)#me esta diciendo que va a ser ó 99 o el valor + el 2% en caso de no ser 99
        self._regate=min(99,self._regate+ self._regate*0.02)
        self._pase=min(99,self._pase+ self._pase*0.02)
        self._defensa=min(99,self._defensa+ self._defensa*0.02)
        self._fisico=min(99,self._fisico+ self._fisico*0.02)
        self._tiro=min(99,self._tiro+ self._tiro*0.02)
        
    def calcular_quimica(self):
        return 100