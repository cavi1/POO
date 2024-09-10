#atributos comunes: nombre, club, pais, atributos, quimica
#metodo comun: imprmir toda la info de la carta exceptuando la habilidad especial


from abc import ABC, abstractmethod

class Carta(ABC)

    def __init__(self, nombre, club, pais, habilidad_especial, velocidad, tiro, regate, defensa, pase,fisico, quimica, valoracion):
        self._nombre=nombre
        self._club=club
        self._habilidad_especial=[]
        self._atributos=[]
        self._quimica=quimica

    def get_info_carta(self):
        return f"nombre: {self._nombre} club: {self._club} atributos: {self._atributos} quimica: {self._quimica}"

    @abstractmethod
    def set_attributos(self, min, max):
        self._velocidad=,
        



    