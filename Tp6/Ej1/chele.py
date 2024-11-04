from threading import Thread
import time

class Hola_Mundo(Thread):

    def imprimir_hola_mundo (self, tiempo):
        time.sleep(tiempo)
        print (f"HOLA MUNDITO desde el hilo: {self.name }")
    
for i in range (1,7):
    Hola_Mundo().imprimir_hola_mundo(i)