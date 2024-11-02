"""8. Como parte de un sistema de administración de archivos debe implementar, usando el
patrón Composite, las clases necesarias para organizar carpetas y archivos.

Todo elemento posee un nombre y un método que indica si es carpeta o no. En el caso
de las carpetas cuentan con un listado de elementos que contienen.
El objetivo final será crear una serie de elementos y su contenido para luego imprimir el
nombre de cada uno.

Ejemplo de salida:
● Carpeta 1
    ○ Carpeta 2
        ■ Archivo 1
        ■ Archivo 2
    ○ Archivo 3
● Carpeta 3
    ○ Archivo 4"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Component(ABC):#tan abstracto no es a fin de cuentas
    
    def __init__(self, name):
        self._name = name
    
    def get_padre(self):
        return self.__padre
    
    def set_padre(self, padre: Component):
        self.__padre=padre 
        
    def agregar(self, component: Component):
        pass

    def quitar(self, component: Component):
        pass

    def es_compuesto(self):

        return False

    @abstractmethod
    def mostrar(self, nivel):
        pass

    @abstractmethod
    def crear(self):
        pass
    
class Archivo(Component):
    
    def mostrar(self, nivel=0):
        return "\t" * nivel + self._name
    
    def crear(self):
        open(self._name, "x")#el parámetro "x" para la fuinción open significa que el archivo se CREA para escritura
        
    
class Carpeta(Component):
    
    def __init__(self, name):
        super().__init__(name)
        self.__hijos= []  #es una lista vacia de elementos de la clase componente

    def agregar(self, component):
        self.__hijos.append(component)
        component.set_padre(self)#setea como padre a la carpeta en la que se encuentra el componente
        
    def quitar(self, component):
        self.__hijos.remove(component)
        component.set_padre(None)
    
    def es_compuesto(self):
        return True
    
    def mostrar(self, nivel=0):
        result = "\t"*nivel + self._name
        for hijo in self.__hijos:
            result+="\n" + hijo.mostrar(nivel+1)
        return result    
    def crear(self):
        return super().crear()
    
    

def mostrar_carpeta_cliente(component: Component):
    print(component.mostrar())
    

def agregar_archivo_a_carpeta_cliente(component1: Component, component2: Component):
    if component1.es_compuesto():
        component1.agregar(component2)
        

archi1=Archivo('Archivo 1')
archi2=Archivo('Archivo 2')
archi3=Archivo('Archivo 3')
archi4=Archivo('Archivo 4')
carpeta1=Carpeta('Carpeta 1')
carpeta2=Carpeta('Carpeta 2')
carpeta3=Carpeta('Carpeta 3')
raiz=Carpeta('Raíz')


#agregar_archivo_a_carpeta_cliente(raiz, carpeta1)
agregar_archivo_a_carpeta_cliente(raiz, carpeta3)
agregar_archivo_a_carpeta_cliente(carpeta1,carpeta2)
agregar_archivo_a_carpeta_cliente(carpeta2, archi1)
agregar_archivo_a_carpeta_cliente(carpeta2, archi2)
agregar_archivo_a_carpeta_cliente(carpeta1, archi3)
agregar_archivo_a_carpeta_cliente(carpeta3, archi4)

mostrar_carpeta_cliente(carpeta1)
mostrar_carpeta_cliente(carpeta3)
#mostrar_carpeta_cliente(raiz)