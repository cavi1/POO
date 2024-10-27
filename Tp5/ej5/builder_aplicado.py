from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class BuilderSmartphone(ABC):

    @property
    @abstractmethod
    def smartphone(self) -> None:
        pass

    @abstractmethod
    def smartphone(self) -> None:
        pass

    @abstractmethod
    def produce_screen(self) -> None:
        pass

    @abstractmethod
    def produce_network(self) -> None:
        pass
    @abstractmethod
    def produce_bluetooth(self) -> None:
        pass


class ConcreteBuilderSmartphone(BuilderSmartphone):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._smartphone = Smartphone()

    @property
    def smartphone(self) -> Smartphone:
        smartphone = self._smartphone
        self.reset()
        return smartphone

    def produce_screen(self) -> None:
        self._smartphone.add("PANTALLA GORILLA GLASS etc..")

    def produce_network(self) -> None:
        self._smartphone.add("BANDA 5G")

    def produce_bluetooth(self) -> None:
        self._smartphone.add("BLUETOOTH")


class Smartphone():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes del smartphone: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderSmartphone:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderSmartphone) -> None:
        self._builder = builder

    def build_basic(self) -> None:
        self.builder.produce_screen()
        self.builder.produce_network()

    def build_full(self) -> None:
        self.builder.produce_screen()
        self.builder.produce_network()
        self.builder.produce_bluetooth()



director = Director()
builder = ConcreteBuilderSmartphone()
director.builder = builder

print("Smartphone basico: ")
director.build_basic()
builder.smartphone.list_parts()

print("\n")

print("Smartphone alta gama: ")
director.build_full()
builder.smartphone.list_parts()
