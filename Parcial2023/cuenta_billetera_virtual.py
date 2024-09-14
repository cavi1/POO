from cuenta import Cuenta
from datetime import datetime
import random

class Cuenta_billetera_virtual(Cuenta):
    
    def __init__(self, dueño):
        super().__init__(dueño)
        self.__cvu=random.randint(10**21,10**22-1)
        
    def pagar_con_credito(self, impuesto, cuotas):
        impuesto.validar_pago(self._saldo,datetime.now().month)
        if impuesto.get_estado():
            interes=impuesto.get_monto()*(8*cuotas/100)
            super().pagar_con_credito(impuesto.get_monto(), interes)
        