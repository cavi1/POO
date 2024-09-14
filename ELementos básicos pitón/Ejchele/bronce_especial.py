from carta import Carta
class Bronce_especial (Carta):
    
    def __init__(self, nombre, club, pais, habilidad):
        super().__init__(nombre, club, pais)
        self._tipo_carta = "Bronce Especial"
        self.__habilidad_especial = habilidad
    
    def get_tipo_carta (self):
        return self.__tipo_carta
    
    def imprimir_info(self):
        super().imprimir_info()
        print (f"Habilidad Especial : {self.__habilidad_especial}")
        
    