from __future__ import annotations
from abc import ABC, abstractmethod


class Compra():
    def __init__(self, metodo_pago: MetodoPago) -> None:
        self.__metodo_pago = metodo_pago

    @property
    def metodo_pago(self) -> MetodoPago:
        return self.__metodo_pago

    @metodo_pago.setter
    def metodo_pago(self, metodo_pago: MetodoPago) -> None:
        self.__metodo_pago = metodo_pago

    def procesar_pago(self, monto: float) -> None:

        print("La persona selecciono un metodo de pago, esperamos resultado de transacción....")
        result = self.__metodo_pago.pagar(monto)
        print("resultado de la transacción: "+ str(result))


class MetodoPago(ABC):

    @abstractmethod
    def pagar(self, monto: float):
        pass

class MercadoPago(MetodoPago):
    def pagar(self, monto: float) -> bool:
        print("Se realiza el pago de: "+ str(monto)+" con Mercado Pago")
        return True


class Visa(MetodoPago):
    def pagar(self, monto: float) -> bool:
        print("Se realiza el debito de: "+ str(monto)+" de su cuenta asociada a la tarjeta Visa")
        return True

monto = 15000.0
print("Bienvenido! Sus productos dan un total de: "+str(monto)+ "\n seleccione un metodo de pago: \n1- Mercado Pago \n2- Debito")
seleccion = MercadoPago() if int(input()) == 1 else Visa()
compra = Compra(seleccion)

compra.procesar_pago(monto)