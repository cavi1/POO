from personaje import Personaje

class Guerrero(Personaje):

    def __init__(self, vida=400, nivelAtaque=5, nivelDefensa=20):
        super().__init__(self,vida,nivelAtaque,nivelDefensa)

    def defender(self, ataque):
        daño_recibido = ataque - self.nivelDefensa
        if daño_recibido > 0:
            self.vida -= daño_recibido
        if self.vida < 0:
            self.vida = 0
