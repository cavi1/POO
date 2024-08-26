

class Familia:
    
    def __init__(self) :
        self.__nombre_familia=" "
        self.__integrantes=[]
        
    def agrega_integrante_familia(self, persona):
        self.__integrantes.append(persona)
    
    
    def cuenta_integrantes(self):
        cont=0
        for persona in self.__integrantes:
            cont+=1
        return cont
    
    def cuenta_edades_familia(self):
        cont=0
        for persona in self.__integrantes:
            
            cont+=persona.calc_edad()
        return cont
            
    
    def cuenta_laburantes_familia(self):
        cont=0
        for persona in self.__integrantes:
            if persona.get_trabaja():
                cont+=1
                
        return cont
                
    
    def retorna_integrantes_familia(self):
        return  self.__integrantes
    
        
    