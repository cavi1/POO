class Personaje():
    def __init__(self, vida: int = 100, defensa: int = 5) -> None:
        self._vida = vida
        self._defensa = defensa

    def recibir_danio(self) -> str:
        pass

class Mago(Personaje):
    def __init__(self, vida: int = 100, defensa: int = 5) -> None:
        super().__init__(vida, defensa)

    def recibir_danio(self, ataque= 0) -> int:
        ataque_efectivo = ataque - self._defensa
        self._vida = self._vida + ataque_efectivo
        return ataque_efectivo 
    #me imagino este valor como el que se muestra sobre el personaje al ser atacado

class PersonajeDecorator(Personaje):
    def __init__(self, personaje: Personaje) -> None:
        self._personaje = personaje

    @property
    def personaje(self) -> Personaje:
        return self._personaje

    def recibir_danio(self, ataque= 0) -> int:
        return self._personaje.recibir_danio(ataque)


class EscudoDecorator(PersonajeDecorator):

    def recibir_danio(self, ataque= 0) -> int:
        ataque = ataque - 15 #suponiendo que el escudo es de 15 puntos.
        return self.personaje.recibir_danio(ataque)




def atacar(personaje: Personaje, ataque) -> None:
    print("recibe daño de: "+str(personaje.recibir_danio(ataque)))


mago = Mago()
print("El mago es atacado")
atacar(mago,30)
print("\n")

mago_con_escudo = EscudoDecorator(mago)
print("El mago con escudo es atacado ")
atacar(mago_con_escudo, 30)