from multiprocessing import Process
import time
import os

class MiProceso(Process):

    def run(self):
        inicio = time.perf_counter()
        info('Hilo MiProceso')
        print("Duermo el hilo")
        time.sleep(0.5)
        fin= time.perf_counter()
        print("termina hilo: "+ str(fin-inicio))


def info(title):
    print(title)
    print('Nombre de modulo:', __name__)
    print('Proceso padre:', os.getppid())
    print('ID de proceso:', os.getpid())

if __name__ == '__main__':
    info('Hilo main')
    p = MiProceso()
    p.start()
    p.join()