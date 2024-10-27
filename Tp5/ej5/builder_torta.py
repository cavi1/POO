"""5. Aplique el patrón Builder para la construcción de tres tipos de tortas, una torta deberá
tener como atributo la masa y el relleno. Las tortas deben ser de Vainilla, coco y una a
su elección para demostrar el objetivo del patrón solicitado."""


from __future__ import annotations
from abc import ABC, abstractmethod

class BuilderTorta(ABC):#interfaz builderTorta  (es una manera formal de decir como va a implementar tu clase)
    
    @abstractmethod
    def get_torta(self):
        pass
    
    def set_masa(self):
        pass
    
    def set_relleno(self):
        pass
    
class Torta_coco(BuilderTorta):#Una torta en particular
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._torta = Torta()
    
    def set_masa(self):
        self._torta.agregar("Masa de coco")
    
    def set_relleno(self):
        self._torta.agregar("Relleno de crema de coco")
    
    def get_torta(self):
        torta = self._torta
        self.reset()
        return torta


class TortaChocolate(BuilderTorta):#Una torta en particular
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._torta = Torta()
    
    def set_masa(self):
        self._torta.agregar("Masa de chocolate")
    
    def set_relleno(self):
        self._torta.agregar("Relleno de crema de chocolate")
    
    def get_torta(self):
        torta = self._torta
        self.reset()
        return torta

class Torta_vainilla(BuilderTorta):#Una torta en particular
    
    def __init__(self):
        self.reset()

    def reset(self):
        self._torta = Torta()    
    
    def get_torta(self):
        torta = self._torta
        self.reset()
        return torta
    
    def set_masa(self):
        self._torta.agregar("masa de vainilla")
        
    def set_relleno(self):
        self._torta.agregar("vainilla de vainilla")
        

class Torta():#Un armador de tortas genérico que consta en agregar sus ingredientes y mostrarlos (funciona para cualquier torta)
    
    def __init__(self):
        self.ingredientes=[]
        
    def agregar(self, cosa_que_agrego):
        self.ingredientes.append(cosa_que_agrego)
        
    def mostrar_ingredientes(self):
        print(f"Partes de la torta: {', '.join(self.ingredientes)}", end="")#es una manera de imprimir una lista sacandole las comillas y separando los elementos con una coma
    

class Director:#es una clase extra que se encarga de añadir una mayor personalización a la construcción del objeto, en este caso se puede crear una torta básica o una torta completa
    
    def __init__(self):
        self._builder= None
    
    def get_builder(self):
        return self._builder
    
    def set_builder(self, builder: BuilderTorta):
        self._builder=builder
        
    def torta_basica(self):
        self._builder.set_masa()
        
    def torta_completa(self):
        self._builder.set_masa()
        self._builder.set_relleno()

director=Director()#el director se instancia una sola vez ya que su atributo va cambiando mediante la funcion set_builder

################################################################################# impresión torta de vainilla
constructor_torta_de_vainilla=Torta_vainilla()
director.set_builder(constructor_torta_de_vainilla)


print("Torta de vainilla básica ingredientes: ")
director.torta_basica()
constructor_torta_de_vainilla.get_torta().mostrar_ingredientes()

print("\n")

print("Torta de vainilla completa ingredientes: ")
director.torta_completa()
constructor_torta_de_vainilla.get_torta().mostrar_ingredientes()

print("\n")

################################################################################# impresión torta de coco
constructor_torta_de_coco=Torta_coco()
director.set_builder(constructor_torta_de_coco)

print("Torta de coco básica ingredientes: ")
director.torta_basica()
constructor_torta_de_coco.get_torta().mostrar_ingredientes()

print("\n")

print("Torta de coco completa ingredientes: ")
director.torta_completa()
constructor_torta_de_coco.get_torta().mostrar_ingredientes()