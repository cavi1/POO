class Alumno:
    __nombre=" "
    __apellido=" "
    __dni=0
    
    def __init__(self):
        pass
    
    def setnombre(self, dar_nombre):
        self.__nombre = dar_nombre
    
    def setapellido(self, dar_apellido):
        self.__apellido = dar_apellido
    
    def setdni(self, dar_dni):
        self.__dni = dar_dni
    
    @classmethod #un metodo que no tiene q ver ni con la clase ni con el objeto
    def iniciar(cls):
        instancia = cls.__new__(cls)
        instancia.__nombre=" "
        instancia.__apellido=" "
        instancia.__dni=" "
        return instancia
        
        
    
    @classmethod
    def iniciar_con_nom_ape(cls, dar_nombre, dar_apellido):
        # Crear una instancia y establecer atributos
        instancia = cls.__new__(cls)
        instancia.__nombre = dar_nombre
        instancia.__apellido = dar_apellido
        return instancia
    
    def getNombreYapellido(self):
        return f"{self.__nombre} {self.__apellido}"
        
        
    def getDni(self):
        return self.__dni