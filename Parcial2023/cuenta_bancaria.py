
from cuenta import Cuenta
from datetime import datetime
import random
class Cuenta_bancaria(Cuenta):
        
    def __init__(self, dueño):
        super().__init__(dueño)
        self.__cbu=random.randint(10**22,10**23-1)#la probalidad de que dos cbu coincidan es casi como ganar la lotería tres veces seguidas
        
    def pagar_con_debito(self, impuesto):
        impuesto.validar_pago(self._saldo,datetime.now().month)
        if impuesto.get_estado():
            super().pagar_con_debito(impuesto.get_monto())
            reintegro=impuesto.get_monto()*0.1
            self._saldo+=reintegro
        
    def pagar_con_credito(self, impuesto, cuotas):
        impuesto.validar_pago(self._saldo,datetime.now().month)
        if impuesto.get_estado():
            if cuotas > 3:
                interes=impuesto.get_monto()*(2*cuotas/100)
                super().pagar_con_credito(impuesto.get_monto(),interes)
            else:
                super().pagar_con_credito(impuesto.get_monto(),0)        
    