

from datetime import datetime

class Persona:
    __nombre=" "
    __apellido=" "
    __sexo=" "
    __nacimiento= datetime
    __edad=0
    __estudia=bool 
    __trabaja=bool
    
    def __init__(self,nombre,apellido,nacimiento,estudia, trabaja, sex):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__nacimiento=nacimiento
        self.__sexo=sex
        self.__estudia=estudia
        self.__trabaja=trabaja
        
    def set_nombre(self,nombre):
        self.__nombre=nombre
        
    def set_apellido(self,apellido):
        self.__apellido=apellido
        
    def set_nacimiento(self,nacimiento):
        self.__nacimiento=nacimiento
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_nacimiento(self):
        return self.__nacimiento
    
    def get_trabaja(self):
        return self.__trabaja
    
    def to_string(self):
        return f"Nombre: {self.__nombre} Apellido: {self.__apellido} Nacimiento: {self.__nacimiento}"
    
    def calc_edad(self):
        
        edad=datetime.now().year-self.__nacimiento.year
        
        if (datetime.now().month,datetime.now().day) < (self.__nacimiento.month,self.__nacimiento.day):
            return edad-1
        else:
            return edad
    
    
    
    