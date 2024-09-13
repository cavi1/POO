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

    def calcular_quimica_plantilla(self):
        quimica_total=0
        for i in self.__plantel:
            quimica_total+=i.get_quimica() 
        
        return quimica_total    
    
    def get_equipo(self):
        for i in self.__plantel:
            print("------------------")
            print(i.carta_to_string())
    
    def equipo_lleno(self):
        esta_lleno=False
        if len(self.__plantel)==11:
            esta_lleno=True
        return esta_lleno
    
    