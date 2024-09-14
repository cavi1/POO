from personal import Personal
import random
class Docente(Personal):

    def __init__(self, nombre, sector, categoria):
        super().__init__(nombre, sector)
        self.__categoria=categoria
        
        
    def get_categoria(self):
        return self.__categoria  
        
        