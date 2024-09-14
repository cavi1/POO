from oro import Oro
from bronce_especial import Bronce_especial
from especial import Especial

class Plantilla ():
    
    def __init__(self, nombre, pais, equipo):
        self.__nombre_propietario = nombre
        self.__pais_favorito_plantel = pais
        self.__equipo_favorito = equipo
        self.__plantilla_jugadores = []
    
    def set_pais_fav (self, pais):
        self.__pais_favorito_plantel = pais
    
    def get_pais_fav (self):
        return self.__pais_favorito_plantel
    
    def set_equipo_favorito (self, equipo):
        self.__equipo_favorito = equipo
    
    def get_equipo_favorito (self):
        return self.__equipo_favorito
    
    def set_nombre_propietario (self, nombre):
        self.__nombre_propietario = nombre
    
    def set_plantilla_jugadores (self, jugador):
        self.__plantilla_jugadores.append(jugador)
    
    def set_quimica (self):
        quimica_plantilla = 0
        for i in self.__plantilla_jugadores:
            quimica_plantilla = quimica_plantilla + i.calcular_quimica(self.__pais_favorito_plantel, self.__equipo_favorito)
        quimica_plantilla = quimica_plantilla / (len(self.__plantilla_jugadores) + 1) # porque devuelve el indice (10, pq el areglo va de 0 a 10), no devuelve la longitud total)
        return quimica_plantilla
    
    
    
    def imprimir_plantilla (self):
        print (f"""Propietario del equipo : {self.__nombre_propietario}
            Nombre del equipo : {self.__equipo_favorito}
            Quimica del equipo : {self.set_quimica()}
            Formacion: """)
        indice = 0
        for i in self.__plantilla_jugadores:
            self.__plantilla_jugadores[indice].imprimir_info()
            print(f" Quimica = {i.calcular_quimica(self.__pais_favorito_plantel, self.__equipo_favorito)}")
            indice = indice + 1
            print(" --------------------------------------- ")
    