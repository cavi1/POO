from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    def __init__(self, name) -> None:
        self._name = name

    @property
    def parent(self, name) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:

        return False

    @abstractmethod
    def mostrar(self) -> str:
        pass

    @abstractmethod
    def crear(self) ->bool:
        pass


class File(Component):

    def mostrar(self) -> str:
        return "\t" + self._name
    
    def crear(self)-> bool:
        open(self._name, "x")
    


class Folder(Component):

    def __init__(self, name) -> None:
        super().__init__(name)
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def mostrar(self) -> str:
        result = self._name 
        for child in self._children:
            result+="\n\t"+child.mostrar()
        result+="\n"
        return result
    
    def crear(self):
        return super().crear()

def client_code(component: Component) -> None:
    print(component.mostrar())


def client_code2(component1: Component, component2: Component) -> None:

    if component1.is_composite():
        component1.add(component2)
    print(component1.mostrar())


archivo = File("archivo_x.txt")
client_code(archivo)
print("\n")

root_folder = Folder("root")

folder1 = Folder("carpeta_1")
folder1.add(File("archivo1-1.txt"))
folder1.add(File("archivo1-2.txt"))

folder2 = Folder("carpeta_2")
folder2.add(File("archivo2-1.txt"))

root_folder.add(folder1)
root_folder.add(folder2)

print("Imprimimos el sistema de archivos:")
client_code(root_folder)
print("\n")

print("No es necesario saber :")
client_code2(root_folder, archivo)