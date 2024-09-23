from pokemon import Pokemon

class Pokemon_tipo_fuego(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo="Fuego"
        self._debilidad="Agua"
        
    def defender(self, daño):#según entendí este pokemon recibe todo el daño
        return daño