class Materia:
    __nombre=" "
    __codigo=" "
    
    def __init__(self, nombre, codigo):
        self.__nombre=nombre
        self.__codigo=codigo
        
    def getNombre(self):
        return self.__nombre
        
    def set_nombre(self,nombre):
        self.nombre=nombre
        
    def set_codigo(self,codigo):
        self.__codigo=codigo
        
    