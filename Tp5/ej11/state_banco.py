"""11. Aplique el patrón State para simular el funcionamiento de atención de una caja en un
banco. La clase Banco tiene una caja y este puede atender una persona, suspender,
cerrar y abrir la caja. La caja tiene el nombre del cajero y el estado actual, los estados
posibles son:
a. Abierta: imprime por pantalla al cliente próximo en la fila.
b. Suspendida: en este estado solo atiende a personas mayores a 60 años de
edad, en otro caso imprime un mensaje de espera.
c. Cerrada: no atiende personas y muestra mensajes indicando su estado.
Pruebe el correcto funcionamiento del sistema creando personas con diferentes edades
y cambiando los estados de la caja."""
from faker import Faker
import random
from abc import ABC, abstractmethod

class Persona:
    
    def __init__(self):
        faker=Faker()
        self.__nombre=faker.name()
        self.__edad=random.randint(50,70)
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
class Caja:
    
    def __init__(self):
        faker=Faker()
        self.__nombre=faker.name()
        self.__state=Abierta()#arranca con un estado inicial
        
    def set_estado(self, estado):
        self.__state=estado
        
    def get_estado(self):
        return self.__state
    
    def atender(self):
        self.__state.atender()
        
    def suspender(self):
        self.__state.suspender()
        if type(self.__state) != Suspendida:
            self.__state = Suspendida()
        
    def cerrar(self):
        self.__state.cerrar()
        if type(self.__state) != Cerrada:
            self.__state = Cerrada()
        
    def abir(self):
        self.__state.abrir()
        if type(self.__state) != Abierta:
            self.__state = Abierta()
    
        
    
class State(ABC):#interfaz de los estados
    
    @abstractmethod
    def atender(self):
        pass
    
    @abstractmethod
    def suspender(self):
        pass
    
    @abstractmethod
    def cerrar(self):
        pass
    
    @abstractmethod
    def abrir(self):
        pass
    
class Abierta(State):
    
    def atender(self):
        persona=Persona()
        print(f"El próximo cliente a ser atendido es {persona.get_nombre()}")#es random
        
    def suspender(self):
        print("La caja pasará de abierta a suspendida")
        
    def abrir(self):
        print("La caja ya está abierta...")    
        
    def cerrar(self):
        print("La caja pasará de abierta a cerrada")
        
class Suspendida(State):
    
    def atender(self):
        persona=Persona()
        if persona.get_edad()>60:
            print(f"{persona.get_nombre()}, te atiendo porque tenes {persona.get_edad()} años")
        else:
            print(f"{persona.get_nombre()}, no te atiendo porque tenes {persona.get_edad()} años")
        
    def suspender(self):
        print("La caja ya está suspendida...")
        
    def abrir(self):
        print("La caja pasará de suspendida a abierta")    
        
    def cerrar(self):
        print("La caja pasará de suspendida a cerrada")
        
class Cerrada(State):
    
    def atender(self):
        print("La caja está cerrada")
        
    def suspender(self):
        print("La caja pasará de cerrada a suspendida")
        
    def abrir(self):
        print("La caja pasará de cerrada a abierta")    
        
    def cerrar(self):
        print("La caja ya estaba cerrada...")       

cajaX=Caja()  
cajaX.abir()
cajaX.atender()
cajaX.suspender()
cajaX.atender()
cajaX.atender()
cajaX.suspender()
cajaX.abir()   

    
#Cada instancia de banco tiene una instancia de caja