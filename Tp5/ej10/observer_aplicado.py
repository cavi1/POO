from __future__ import annotations
from abc import ABC, abstractmethod
import random
from typing import List


class Sujeto(ABC):

    @abstractmethod
    def agregar(self, observador: Observador) -> None:

        pass

    @abstractmethod
    def quitar(self, observador: Observador) -> None:
        pass

    @abstractmethod
    def notificar(self) -> None:
        pass


class SensorMovimiento(Sujeto):

    _observadores: List[Observador] = []

    def agregar(self, observer: Observador) -> None:
        self._observadores.append(observer)

    def quitar(self, observer: Observador) -> None:
        self._observadores.remove(observer)

    def notificar(self) -> None:
        print("MOVIMIENTO!!\nSensor de movimiento: Solicitar sacar foto o grabar video...")
        for observador in self._observadores:
            observador.actualizar(self)

    def detectar(self) -> None:
        
        movimiento = False
        while not movimiento:
            print("\nSensando movimiento...")
            movimiento = bool(random.getrandbits(1))
        self.notificar()    




class Observador(ABC):

    @abstractmethod
    def actualizar(self, sujeto: Sujeto) -> None:
        pass


class CamaraFotos(Observador):
    def actualizar(self, sujeto: Sujeto) -> None:
        print("saco foto!")

class CamaraVideo(Observador):
    def actualizar(self, sujeto: Sujeto) -> None:
        print("comienzo a grabar!")


sensor_movimiento = SensorMovimiento()

camara1 = CamaraFotos()
sensor_movimiento.agregar(camara1)

camara2 = CamaraVideo()
sensor_movimiento.agregar(camara2)

sensor_movimiento.detectar()