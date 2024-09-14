from personal import Personal

class Nodocente(Personal):
    
    def __init__(self, nombre, sector, jornada):
        super().__init__(nombre, sector)
        self.__jornada=jornada
        
    def get_categoria(self):
        return self.__jornada   