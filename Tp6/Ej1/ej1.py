"""Implemente un programa que escriba un “hola mundo” por cada hilo de ejecución que
se cree (seis es un número razonable) y que además indique desde qué hilo se
imprime. Luego haga que cada uno espere un tiempo proporcional a su identificador
antes de imprimir el mensaje (el thread 1, un segundo, el 2, dos segundos, el 3, tres
segundos)."""
from multiprocessing import Process
import time

class Impresion(Process):
    
    def run(self):
        print(f"Thread {self.name} Hola mundo")

imp1=Impresion()
imp2=Impresion()

if __name__ == '__main__':
    for i in range(6):                                            
        time.sleep(i) 
        Impresion().start()
