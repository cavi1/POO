from abc import ABC, abstractmethod
import random
class Pokemon(ABC):
    
    def __init__(self,nombre):
        self._nombre=nombre
        self._vida=100
        self._ataque=random.randint(0,100)
        self._defensa=random.randint(0,100)
        self._velocidad=random.randint(0,100)
        self._salvajismo=random.randint(0,100)
        self._debilidad=" "
        self._tipo=" "
    
    def poke_to_string(self):
        print(f"Nombre: {self._nombre} Vida:{self._vida} Ataque: {self._ataque} Defensa: {self._defensa} Velocidad: {self._velocidad} Salvajismo:{self._salvajismo}")
        
    def atacar(self, victima):#esta generalizado para los de hierba y los de fuego
        daño_neto=victima.defender(self._ataque)  
        
        if victima._debilidad == self._tipo:
            
            prob=random.random()
            critico=False
            
            if prob<=0.7:
                
                critico=True
            
            if critico:
                
                daño_neto=victima.defender(self._ataque+self._ataque*0.5)
                
                if daño_neto-victima._defensa > 0:
                    victima._vida-=daño_neto-victima._defensa# la vida de la victima esta condicionada por el daño del atacante y la defensa de la victima
            else:
                if daño_neto-victima._defensa > 0:
                    victima._vida-=(victima.defender(self._ataque)-victima._defensa)
        else:
            if daño_neto-victima._defensa > 0:
                victima._vida-=(victima.defender(self._ataque)-victima._defensa)
    
    @abstractmethod
    def defender(self,daño):
        pass
    
    
    def get_salvajismo(self):
        return self._salvajismo
    
    def get_vida(self):
        return self._vida
    
    def disminuir_salvajismo(self):
        self._salvajismo-=self._salvajismo*0.1