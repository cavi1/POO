class Plantilla:
    def __init__(self, usuario, pais_fav, equipo_fav):
        self.__usuario=usuario
        self.__pais_fav=pais_fav
        self.__equipo_fav=equipo_fav
        self.__plantel=[]
        
    def get_pais_fav(self):
        return self.__pais_fav
    
    def get_equipo_fav(self):
        return self.__equipo_fav
    
    