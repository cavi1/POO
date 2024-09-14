from tarifa_proveedor import TarifaProveedor

class Personal(TarifaProveedor):
    
    def __init__(self):
        pass
    
    def calcularMinutosDeLlamada(self, totalMinutos):
        minutosClaro=super().calcularMinutosDeLlamada(totalMinutos)
        return minutosClaro + minutosClaro*0.2
    
    def calcularConsumoGB(self, totalGIgas):
        GbClaro=super().calcularConsumoGB(totalGIgas)
        return GbClaro + GbClaro*0.5
    
    