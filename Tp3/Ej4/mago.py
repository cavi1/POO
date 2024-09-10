from personaje import Personaje

class Mago(Personaje):

    def __init__(self, vida=200, nivelAtaque=30, nivelDefensa=10):
        super().__init__(self,vida,nivelAtaque,nivelDefensa)
    
    def defender(self,ataque):
        daño_recibido=ataque-self.nivelDefensa
        if daño_recibido > 0:
            self.vida-=daño_recibido        
        if self.vida < 0
            self.vida=0

    def atacar(self):
        return super().atacar * 2

        

    