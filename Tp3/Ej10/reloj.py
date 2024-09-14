class Reloj:
    
    def __init__(self):
        self.__horas_mensuales_categoria_docente={"Simple":40,"Semiexclusiva":80,"Exclusiva":160}
        self.__horas_mensuales_jornada_nodocente={"Completa":120,"Reducida":80}
        self.__estado_cumplido=False
    
    def generar_informe(self,personal):
        self.evalua_estado_cumplido()
        print(f"Cantidad de horas trabajadas: {personal.get_horas_mensuales_trabajadas()}")
        if self.__estado_cumplido == True:
            print("El personal seleccionado cumple con sus horas mensuales")
    
    
    def evalua_estado_cumplido(self,personal):
        
        if personal.get_categoria() == "Simple":
            if personal.get_horas_mensuales_trabajadas() >= self.__horas_mensuales_categoria_docente.get("Simple"):
                self.__estado_cumplido=True
        elif personal.get_categoria() == "Semiexclusiva": 
            if personal.get_horas_mensuales_trabajadas() >= self.__horas_mensuales_categoria_docente.get("Semiexclusiva"):
                self.__estado_cumplido=True
        elif personal.get_categoria() == "Exclusiva": 
            if personal.get_horas_mensuales_trabajadas() >= self.__horas_mensuales_categoria_docente.get("Exclusiva"):
                self.__estado_cumplido=True        
        elif personal.get_categoria() == "Completa": 
            if personal.get_horas_mensuales_trabajadas() >= self.__horas_mensuales_jornada_nodocente.get("Completa"):
                self.__estado_cumplido=True
        elif personal.get_categoria() == "Reducida": 
            if personal.get_horas_mensuales_trabajadas() >= self.__horas_mensuales_jornada_nodocente.get("Reducida"):
                self.__estado_cumplido=True
                            
