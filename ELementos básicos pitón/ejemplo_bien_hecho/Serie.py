

class Serie:
    
    def __init__(self, img, titulo, estreno):
        self.__urlImg = img
        self.__titulo = titulo
        self.__estreno = estreno
    
    def imprimir(self):
        print("{}  {}  {}".format(self.__urlImg, self.__titulo,self.__estreno))