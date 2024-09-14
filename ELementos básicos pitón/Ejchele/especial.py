from carta import Carta
from random import randint
class Especial (Carta):
    
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        self._tipo_carta = "Especial"
        self.__lista_habilidades = []
    
    def get_tipo_carta (self):
        return self.__tipo_carta
    
    def set_lista_habilidades (self, lista):
        for i in lista:
            self.__lista_habilidades.append (i)
        
    
    def get_lista_habilidades (self):
        return self.__lista_habilidades
    
    def calcular_quimica(self, pais_fav, club_fav):
        return 100
    
    def imprimir_info(self):
        super().imprimir_info()
        print(" Lista de Habilidades:")
        for i in self.__lista_habilidades:
            print (i)
    
    