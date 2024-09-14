from carta import Carta
class Oro(Carta):
    
    def __init__(self, nombre, club, pais):
        super().__init__(nombre, club, pais)
        self._tipo_carta = "Oro"
    
    def get_tipo_carta (self):
        return self.__tipo_carta
