from threading import Thread

contador = 0
class Numeros(Thread):
    
    def run(self):
        global contador
        for i in range(10000000):
            contador += 1
        print(self.name+" termina ejecución ")

hilos = []
for i in range(5):
    un_hilo = Numeros()
    hilos.append(un_hilo)
    un_hilo.start()

for hilo in hilos:
    hilo.join()
print("termina ejecución de programa")
print("Resultado contador:", contador) 