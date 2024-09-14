from random import randint
from abc import ABC
class Carta(ABC):
    
    def __init__(self, nombre, club, pais ):
        self._tipo_carta = ""
        self._nombre_carta = nombre
        self._club_carta = club
        self._pais_carta = pais
        self._velocidad = 0
        self._tiro = 0
        self._regate = 0
        self._defensa = 0
        self._pase = 0
        self._fisico = 0
        self._valoracion = 0
    
    def set_nombre_carta(self, nombre):
        self._nombre_carta = nombre
    
    def get_nombre_carta(self):
        return self.__nombre_carta
    
    def set_club_carta(self, club):
        self._club_carta = club
    
    def get_club_carta(self):
        return self._club_carta
    
    def set_pais_carta(self, pais):
        self._pais_carta = pais
    
    def get_pais_carta(self):
        return self._pais_carta
    
    def calcular_valoracion (self):
        valoracion =(self._velocidad + self._tiro + self._regate + self._defensa + self._pase + self._fisico) / 6
        valoracion = int(valoracion)
        return valoracion
    
    def set_atributos(self, max, min, caso):
        vec = []
        for i in range(6):
            nro = randint (min, max)
            if caso == 0:
                nro = int(nro + 2)
            elif caso == 1:
                nro = int(nro * 1.05)
            else:
                nro = int(nro * 1.02)
            if nro > max:
                    nro = max
            vec.append(nro)
        self._velocidad = vec[0]
        self._tiro = vec[1]
        self._regate = vec[2]
        self._defensa = vec[3]
        self._pase = vec[4]
        self._fisico = vec[5]
    
    def calcular_quimica(self, pais_fav, club_fav):
        quimica = 0
        if self._club_carta == club_fav or self._pais_carta == pais_fav:
            quimica = 80
        if self._club_carta == club_fav and self._pais_carta == pais_fav:
            quimica = 100
        return quimica
    
    def imprimir_info (self):
        valoracion =self.calcular_valoracion()
        print(f"""Tipo de carta : {self._tipo_carta}
            Nombre del jugador : {self._nombre_carta}
            Nombre del club : {self._club_carta}
            Pais del jugador: {self._pais_carta}
            Valoracion :{valoracion}
            Velocidad : {self._velocidad}
            Tiro : {self._tiro}
            Regate : {self._regate}
            Defensa : {self._defensa}
            Pase : {self._pase}
            Fisico : {self._fisico}
            """)