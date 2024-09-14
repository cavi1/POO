from abc import ABC, abstractmethod
import random
from datetime import datetime
class Cuenta:  

    def __init__(self, dueño):
        self._dueño=dueño
        self._nro_cuenta=random.randint(10**15,10**16-1)
        self._saldo=random.uniform(5000.0,10000.0)
    def pagar_con_debito(self,monto):
        self._saldo -= monto    

    def pagar_con_credito(self, monto, interes):
        self._saldo -= (monto + interes)
    
    def get_saldo(self):
        return self._saldo