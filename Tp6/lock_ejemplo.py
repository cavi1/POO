from  multiprocessing import Process, Pipe, Lock
import random
import time

class EstacionMeteorologica(Process):
    def __init__(self, canal, lock):
        super(EstacionMeteorologica, self).__init__()
        self.canal = canal
        self.lock = lock

    def run(self):
        for i in range(3):
            with self.lock:
                mensaje = "estación: "+self.name +" paquete "+str(i) 
                self.canal.send(mensaje+ " temperatura: "+ str(random.randint(-20,50)))
                time.sleep(random.random())
                self.canal.send(mensaje+ " humedad: "+ str(random.randint(0,100)))
                time.sleep(random.random())
                self.canal.send(mensaje+ " velocidad de viento: "+ str(random.randint(0,180)))
                time.sleep(random.random())

        self.canal.send(None)

class Servidor(Process):
    def __init__(self, canal):
        super(Servidor, self).__init__()
        self.canal = canal

    def run(self):
        contador = 0
        while contador <2:
            mensaje = self.canal.recv()
            if mensaje is not None: 
                print(f"Recibido: {mensaje}")
            else:
                contador += 1

if __name__ == '__main__':
    pipe_conn1, pipe_conn2 = Pipe() #devuelve dos pipes siempre
    lock = Lock()
    estacion1 = EstacionMeteorologica(pipe_conn1,lock)
    estacion2 = EstacionMeteorologica(pipe_conn1,lock)
    servidor = Servidor(pipe_conn2)

    estacion1.start()
    estacion2.start()
    servidor.start()

    estacion1.join()
    estacion2.join()
    servidor.join()
    print("fin de la ejecución")
