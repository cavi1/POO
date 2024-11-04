from threading import Thread

class Letras(Thread):

    def run(self):
        letras = 'ABCDEEFGHIJKLMNÑOPQRSTUVWXYZ'
        for letra in letras:
            print(self.name+" Letra: "+letra)
        print(self.name+" termina ejecución de imprimir_letras")

class Numeros(Thread):
    
    def run(self):
        for i in range(1, 10):
            print(self.name+" Número: "+str(i))
        print(self.name+" termina ejecución de imprimir_numeros")

for i in range(0,5):  #por cada ejecucion asigno un hilo a letras y un hilo a numeros, si saco este for, thread 1 va a tener a letras y thread 2 va a tener a numeros
    Letras().start() #pero ahora lo que estoy haciendo es dividir en 10 hilos (1 para cada 1)
    Numeros().start()



#si en vez de start se pone run(), se convierte en un print secuencial como los vistos hasta ahora
#escribir start() en lugar de run() convierte el print en uno con propiedades de concurrencia y paralelismo
#colocar run() en lugar de start es un error muy comun, esto no debe hacerse si que quiere aplicar concurrencia y paralelismo a un programa
# que sucede si saco los join?
#si sacas los join el ultimo print se imprime donde se le cante el ogt
print("termina ejecución de programa") 
