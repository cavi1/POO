# Defina la clase abstracta Personaje con los atributos vida, nivelAtaque, nivelDefensa y los
##métodos atacar() que retorne un integer, y defender(ataque). Implemente el método
#atacar pero no el método defender(). Luego, cree dos clases hijas donde ambas
#implementan el método defenderse y al menos una de ellas extiende el método atacar.
#Cada clase debe establecer una cantidad de puntos de vida por defecto.
#En un ataque se deben realizar cierta cantidad de puntos de daño y en la defensa se
#debe reducir esa cantidad de puntos de daños. El resultado final de los puntos de ataque
#debe descontar la misma cantidad de puntos de vida del personaje que defiende.

from abc import ABC, abstractmethod

class personaje(ABC)

    def __init__(self, vida, nivelAtaque, nivelDefensa):
        self._vida = vida
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa
        
    def atacar(self):
        return 10

    @abstractmethod
    def defender(self, ataque):   
        pass

    

    