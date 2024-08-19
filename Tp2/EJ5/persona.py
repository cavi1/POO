#Defina la clase Persona con los atributos
#● Nombre de tipo string
#● Apellido de tipo string
#● Fecha de nacimiento de tipo Date
#Genere además un constructor que reciba tres parámetros(uno por atributo), los
#métodos de acceso(getters y setters) de cada atributo y un método toString que retorne
#una cadena con el valor de todos los atributos.
#● Instancie tres veces la clase persona y por cada instancia imprima en consola el
#valor devuelto por el método toString

#A la clase Persona del ejercicio 6 añada un nuevo método que retorne la edad haciendo
#uso de la fecha de nacimiento. Imprima en consola la edad de tres instancias de la clase

from datetime import datetime
class Persona:
    __nombre=" "
    __apellido=" "
    __nacimiento= datetime
    
    def __init__(self,nombre,apellido,nacimiento):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__nacimiento=nacimiento
        
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
    
    def to_string(self):
        return f"Nombre: {self.__nombre} Apellido: {self.__apellido} Nacimiento: {self.__nacimiento}"
    
    def calc_edad(self):
        
        ya_cumplio=False
        
        if datetime.now().month - self.__nacimiento.month >= 0 and datetime.now().day - self.__nacimiento.day >= 0 :
            ya_cumplio=True
        
        if ya_cumplio:
            return datetime.now().year-self.__nacimiento.year
        else:
            return datetime.now().year-self.__nacimiento.year-1
    
    