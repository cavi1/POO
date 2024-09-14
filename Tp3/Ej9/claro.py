from tarifa_proveedor import TarifaProveedor

class Claro(TarifaProveedor):
    
    def __init__(self):
        pass
    
    def calcular(self,totalSMS,totalMinutos,totalGigas):
        basicoTotal=super().calcular(totalSMS,totalMinutos,totalGigas)
        return basicoTotal + basicoTotal*0.2
    
    