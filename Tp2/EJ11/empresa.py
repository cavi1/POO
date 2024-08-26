from typing import Any


class empresa:
    __nombre=" "
    __direccion=" "
    __empleados=[]
    
    def __init__(self,nombre,direccion):
        self.__nombre=nombre
        self.__direccion=direccion
        
    def set_nombre_empresa(self,nombre):
        self.__nombre=nombre 
        
    def get_nombre_empresa(self):
        return self.__nombre
    
    def set_direccion(self, direccion):
        self.__direccion=direccion
        
    def get_direccion(self, direccion):
        return self.__direccion
    
    def set_empleado(self,empleado):
        self.__empleados.append(empleado)
        
    def get_nro_empleados(self):
        cant=0
        for i in self.__empleados:
            cant+=1
        return cant
    
    

    