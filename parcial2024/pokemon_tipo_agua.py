from pokemon import Pokemon
import random
class Pokemon_tipo_agua(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo="Agua"
        self._debilidad="Hierba"
        
        
    def atacar(self, victima):  
        daño_neto=victima.defensa(self._ataque)
        
        if victima._debilidad == self._tipo:
            daño_neto=victima.defender(self._ataque+self._ataque*0.7)
            if daño_neto-victima._defensa > 0:
                victima._vida-=(daño_neto-victima._defensa)
        else:
            if daño_neto-victima._defensa > 0:
                victima._vida-=(daño_neto-victima._defensa)
                
    def defender(self, daño):
        prob=random.random()
        if prob<=0.3:
            daño=daño*0.5
        return daño
