#Implemente un programa que lance cuatro threads, cada
# uno incrementará una variable contador de tipo entero,
# compartida por todos, 5000 veces y luego imprima.
# Python:¿Cómo debe ser compartida si trabajamos con
# Thread? ¿Y con Process?

from threading import Thread

contagod = 0
class Hilo(Thread):
    
    def run(self):
        global contagod
        for i in range (5000):
            contagod += 1
        print (f"{self.name} hizo su aporte incrementando la variable en 5000 jefe")
    
hilo1 = Hilo()
hilo1.start()

hilo2 = Hilo()
hilo2.start()

hilo3 = Hilo()
hilo3.start()

hilo4 = Hilo()
hilo4.start()

hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

print ("TERmino el trabajo jefe; El contador del programa es igual a =", contagod)