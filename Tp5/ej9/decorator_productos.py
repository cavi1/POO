"""9. Patrón decorator.
Dada una clase Producto con un método public String getPrecio() que el precio del
mismo como String y con dos decimales.
Eje: 90000,50
Es necesario crear dos decorators, uno para cuando el sistema usa moneda
estadounidense($USD) y otro para cuando el sistema usa moneda argentina ($ARS).
Cada decorator debe implementar getLineDescription de forma de que se devuelva el
símbolo de la moneda antes del valor.
Eje: $ARS 90000,50 o $USD 90000,50
Pruebe la implementación con un producto, imprimiendo:
● Lo que retorna el método getPrecio()
● Lo que retorna el método getPrecio() para el primer decorator.
● Lo que retorna el método getPrecio() para el segundo decorator."""

from abc import ABC, abstractmethod

class Producto(ABC):#interfaz para dar mas formalidad
    
    @abstractmethod
    def get_precio(self):
        pass

class Producto_concreto(Producto):
    
    def __init__(self, precio):
        self.__precio=precio
        
    def get_precio(self):
        return self.__precio
    
class Decorador_precio(Producto_concreto):
    
    def __init__(self, producto:Producto):
        self._producto=producto
    
    @abstractmethod
    def get_precio(self):
        pass
    
    
class ARS_decorator(Decorador_precio):
    
    def get_precio(self):
        return '$ARS ' + self._producto.get_precio()
    

class USD_decorator(Decorador_precio):
    
    def get_precio(self):
        return '$USD ' + self._producto.get_precio()
    

prod1=Producto_concreto('90000,50')
prod1USD=USD_decorator(prod1)
print(prod1USD.get_precio())

prod1ARS=ARS_decorator(prod1)
print(prod1ARS.get_precio())

prod1ARSUSD=USD_decorator(prod1ARS)#para ver que funciona como capas
print(prod1ARSUSD.get_precio())

