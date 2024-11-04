"""2) Implemente un programa que lance cuatro threads, cada uno incrementará una variable
contador de tipo entero, compartida por todos, 5000 veces y luego imprima.
Python:¿Cómo debe ser compartida si trabajamos con Thread? ¿Y con Process?"""

from threading import Thread
from multiprocessing import Process

contglob=0

class Hilo(Thread):
    
    def run(self):
        global contglob
        for i in range(5000):
            contglob+=1 
        print(f"termina {self.name}")
        
hilo1=Hilo()

hilo2=Hilo()

hilo3=Hilo()

hilo4=Hilo()

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

#joins

print(f"Contador= {contglob}")

"""Si trababajamos con thread tenemos que usar una variable global
y hacer referencia a ella en un proceso almacenado en una
clase de tipo thread, creamos 4 objetos de esa clase y
comenzamos cada uno de estos hilos y luego los joineamos"""