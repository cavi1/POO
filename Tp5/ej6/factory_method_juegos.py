"""6. Aplique el patrón Factory Method para la creación de juegos físicos y digitales. Los
juegos comparten un id y un importe. También el método abstracto getPrecio, que se
encarga de calcular el precio de uno u otro. Para ello los juegos físicos tienen un
atributo que es el precio de traslado (a caso de ejemplo elija usted). Y los juegos
digitales el precio depende de la plataforma en la cual se compra teniendo como
atributo el precio de la plataforma. Estos valores deben ser float y multiplicarlos al
importe."""
import random
from abc import ABC, abstractmethod

class Creator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
    def calc_precio(self):
        precio_de_juego=self.factory_method()
        result = f'Creador: El precio de tu juego es:{precio_de_juego.get_precio()}'
        return result
    
class Concrete_creator_juego_digital(Creator):
    
    def factory_method(self):
        return Concrete_product_juego_digital()
    
class Concrete_creator_juego_fisico(Creator):
    
    def factory_method(self):
        return Concrete_product_juego_fisico()
    
class Juego(ABC):
    
    @abstractmethod
    def get_precio(self):
        pass

class Concrete_product_juego_digital(Juego):
    
    def __init__(self):
        self.__id_juego=random.randint(1000,9999)
        self.__importe=random.uniform(9,99)
        self.__precio_de_plataforma=self.get_precio()
    

    def get_precio(self):
        precio_plataforma=random.uniform(99,999)
        return self.__importe*precio_plataforma
    
    
class Concrete_product_juego_fisico(Juego):
    
    def __init__(self):
        self.__id_juego=random.randint(1000,9999)
        self.__importe=random.uniform(9,99)
        self.__precio_de_traslado=self.get_precio()
    

    def get_precio(self):
        precio_de_traslado=69.0
        return self.__importe*precio_de_traslado
    
def client_code(creator: Creator):
    print(f"Cliente: Desconozco la clase específica del creador, pero funciona.\n"
    f"{creator.calc_precio()}", end="")
        
    
print("App: Lanzado con Juego digital.")
client_code(Concrete_creator_juego_digital())
print("\n")

print("App: Lanzado con Juego fisico.")
client_code(Concrete_creator_juego_fisico())