from carta import Carta
from carta_bronce_especial import Carta_bronce_especial
from carta_especial import Carta_especial
from carta_oro import Carta_oro

class Plantilla:

    def __init__(self, usuario, pais_fav, equipo_fav):
        self.__usuario=usuario
        self.__pais_fav=pais_fav
        self.__equipo_fav=equipo_fav
        self.__plantel=[]
        
    def agrega_carta(self,carta):
        carta.calcular_quimica(self.__pais_fav,self.__equipo_fav)
        self.__plantel.append(carta)

    
    