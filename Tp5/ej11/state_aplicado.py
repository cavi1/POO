from __future__ import annotations
from abc import ABC, abstractmethod

class Personaje:
    def __init__(self):
        self.__state = CaminarState()

    def setState(self, state: State):
        self.__state = state

    def getState(self) -> State:
        return self.__state

    def mover(self):
        self.__state.mover()

    def atacar(self):
        self.__state.atacar()


class State:
    def __init__(self):
        pass

    def mover(self):
        pass

    def atacar(self):
        pass


class CaminarState(State):
    def __init__(self):
        super().__init__()

    def mover(self):
        print("El personaje está caminando")

    def atacar(self):
        print("El personaje no puede atacar mientras camina")


class CorrerState(State):
    def __init__(self):
        super().__init__()

    def mover(self):
        print("El personaje está corriendo")

    def atacar(self):
        print("El personaje puede atacar mientras corre")


class AtacarState(State):
    def __init__(self):
        super().__init__()

    def mover(self):
        print("El personaje no puede moverse mientras ataca")

    def atacar(self):
        print("El personaje está atacando")


pj = Personaje()

pj.mover()
pj.setState(CorrerState())
pj.mover()
pj.setState(AtacarState())
pj.mover()
pj.atacar()