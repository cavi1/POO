"""5) Desarrolla una clase Cuenta con un atributo saldo de tipo Float. Está representará a una
cuenta bancaria y contendrá el monto monetario que se indique por defecto en el
constructor.
La clase debe poseer un método que permita descontar a ese saldo la cantidad
indicada.
Luego, cree una clase Tarjeta que extienda de Process y reciba en su constructor un
número de identificación y una instancia de la clase Cuenta. Es decir, toda tarjeta estará
asociada a una cuenta bancaria.
Implemente el método run de tal manera que ejecute dos veces un descuento de saldo
a la cuenta, a fines de prueba este descuento será siempre por $100.
Cree una instancia de la clase Cuenta con un saldo de $2000. Cree diez instancias de
la clase Tarjeta y asocie todas a la cuenta creada previamente. Ejecute el método start
de cada instancia de tarjeta(las ejecuciones deben ser en paralelo)
Al finalizar la ejecución de todos los procesos debe imprimirse el resultado. Este debería
de ser cero. Valide ejecutando varias veces el programa asegura que no se obtiene un
falso positivo."""

from multiprocessing import Process, Value
import random

class Cuenta():
    
    def __init__(self, saldo):
        self.__saldo= Value('f',saldo)
        
    def descontar_saldo(self, cantidad):
        with self.__saldo.get_lock():
            self.__saldo.value-=cantidad
    def get_saldo(self):
        return self.__saldo.value
        
    
    
class Tarjeta(Process):
    
    def __init__(self, cuenta, id_tarjeta):
        super().__init__()
        self.__id=id_tarjeta
        self.__cuenta=cuenta
        
    def run(self):
        for i in range(2):
            monto=100.0
            self.__cuenta.descontar_saldo(monto)
            print(f"Nuevo gasto -  {self.name} - Monto: {monto}")
        
cuenta_Banco_Pata=Cuenta(2000.0)
lista_tarjetas=[]

for i in range(10):
    tarjeta = Tarjeta(cuenta_Banco_Pata, i+1)  # Asignar un ID único
    lista_tarjetas.append(tarjeta)

if __name__ == '__main__':
    
    for tarjeta in lista_tarjetas:
        tarjeta.start()
    
    for tarjeta in lista_tarjetas:
        tarjeta.join()# el join debe estar porque sino no les estoy diciendo que se efectúen seria como una especie de commit
    
        
        
    print(f"El saldo de la cuenta es {cuenta_Banco_Pata.get_saldo()}") #como cada proceso utiliza un sector diferente de la memoria
                                                                        #el descuento se efectua en "universos" diferentes
                                                                        #el saldo de mi cuenta se encuentra en otro universo, por eso no se ve afectado por los start
                                                                        
#para arreglar esto, tengo que decirle al saldo que va a ser una variable compartida entre los universos de cada tarjeta(que es un proceso)
