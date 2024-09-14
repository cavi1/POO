
import random
from datetime import date

class Impuesto:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__monto=random.uniform(1000.0,5000.0)
        self.__periodo=date(2024,9,random.randint(1,10)) # es para facilitar la comprobacion
        self.__estado=False
    
    def get_monto(self):
        return self.__monto
    
    def validar_pago(self, monto, periodo):
        if monto - self.__monto >= 0 and self.__periodo.month == periodo:
            self.__estado=True
        else:
            print("No hay plata")
    
    def get_estado(self):
        return self.__estado