from abc import ABC, abstractmethod

class TarifaProveedor(ABC):
    
    def __init__(self, cantidadSMS, cantidadMinutos, cantidadGigas):
        self._totalSMS=cantidadSMS
        self._totalMinutos=cantidadMinutos
        self._totalGigas=cantidadGigas
    
    def calcularSMS(self, totalSMS):
        return totalSMS
    
    def calcularMinutosDeLlamada(self, totalMinutos):
        return totalMinutos*15
    
    def calcularConsumoGB(self, totalGIgas):
        return totalGIgas*20
    
    def calcular(self,totalSMS,totalMinutos,totalGigas):
        return  (self.calcularSMS() + self.calcularMinutosDeLlamada() + 
                self.calcularConsumoGB())
    
    @abstractmethod
    def getNombre(self):
        pass
    
    