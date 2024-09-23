from pokemon import Pokemon
import random
class Pokemon_tipo_hierba(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo="Hierba"
        self._debilidad="Fuego"
    
            
    def defender(self,daño):
        if self._velocidad>50:
            evadir=False
            prob=random.random()
            if prob<=0.5:
                evadir=True
            if evadir:
                daño=0
        return daño    