"""10. Aplique el patrón de diseño Observer para un sistema de reporte del clima, defina la
clase Sistema Meteorológico que extienda de la clase Observable y tenga como atributo
el estado del clima en forma de String. Cada vez que se modifica el clima esté notifica a
todos los observadores. El observador va a ser la clase Reportero que implementa la
interfaz Observer, él será el encargado de imprimir por consola el clima cuando cambia
en el sistema meteorológico.
Pruebe el sistema creando instancias de cada clase y cambiando el clima.
"""

from __future__ import annotations
import random
from abc import ABC, abstractmethod

class I_sistema_meteorologico(ABC):
    
    @abstractmethod
    def suscribir_a(self):
        pass
    
    @abstractmethod
    def desuscribir_a(self):
        pass
    
    @abstractmethod
    def notificar(self):
        pass
    
class C_sistema_meteorologico(I_sistema_meteorologico):
    
        
    __lista_de_suscriptores=[]# por qué no está en un constructor: Este es un caso excepcional ya que en este caso debemos hacer
                                #que todas las instancias de la clase compartan esta lista (que son los suscriptores)
    
    def __init__(self):
        self.__estado_clima=random.choice(['soleado','nublado','lluvioso','ventoso'])    
                                
    def suscribir_a(self, suscriptor: Observer):
        self.__lista_de_suscriptores.append(suscriptor)
        
    def desuscribir_a(self, suscriptor: Observer):
        self.__lista_de_suscriptores.remove(suscriptor)
    
    def notificar(self):
        for suscriptor in self.__lista_de_suscriptores:
            suscriptor.actualizar(self)
            
    def get_clima(self):
        return self.__estado_clima
            
class Observer(ABC):
    
    @abstractmethod
    def actualizar(self, observado:I_sistema_meteorologico):
        pass
    

class Reportero(Observer):
    
    def actualizar(self, observado):
        if observado.get_clima()=='soleado':
            print("Está soleado")
        elif observado.get_clima()=='nublado':
            print("Está nublado")
        elif observado.get_clima()=='lluvioso':
            print("Está lloviendo")
        elif observado.get_clima()=='ventoso':
            print("Hay viento")
            

servicio_meteorologico=C_sistema_meteorologico()
reportero1=Reportero()

servicio_meteorologico.suscribir_a(reportero1)

servicio_meteorologico.notificar()
