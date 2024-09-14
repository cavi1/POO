

class Categoria:
    #titulo tipo string
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__series = []
        
    
    def agregar_serie(self, serie):
        self.__series.append(serie)
        
    
    def imprimir(self):
        print(self.__titulo)
        for pepe in self.__series:
            pepe.imprimir()
        
    