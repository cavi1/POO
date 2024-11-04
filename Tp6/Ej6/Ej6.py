from multiprocessing import Process
from multiprocessing import Lock

"""  En este código, se produce un deadlock porque el proceso intenta adquirir el 
mismo Lock dos veces seguidas en un bloque anidado. Aquí tienes una explicación detallada:

Análisis del Problema
Primera adquisición del Lock:

El proceso ejecuta with Lock: y adquiere el Lock correctamente.
Durante este tiempo, el Lock está bloqueado, y ninguna otra sección de código puede adquirirlo hasta que se libere.
Segunda adquisición del Lock dentro del mismo bloque:

Dentro de ese bloque, el proceso intenta volver a adquirir el mismo Lock con with Lock:. Sin embargo, 
el Lock ya está en posesión del proceso actual y no puede ser adquirido de nuevo hasta que se libere.
Como el Lock nunca se libera mientras el proceso esté dentro del primer with, 
el proceso queda atascado esperando la liberación, lo que genera un deadlock."""


def task(Lock):
    print("Adquiriendo el lock... ", flush=True)
    with Lock:
        print("Adquiriendo el lock otra vez...", flush=True)
        with Lock:
            pass

if __name__ == '__main__':
    lock=Lock()
    process=Process(target=task, args=(lock,))
    process.start()
    process.join()

    
    
"""Solución
Si necesitas que un Lock pueda ser adquirido múltiples veces por el mismo proceso sin causar un deadlock, 
debes usar un RLock (bloqueo reentrante) en lugar de un Lock simple. 
Un RLock permite que el mismo proceso o hilo adquiera el bloqueo varias veces, siempre que se libere el mismo número de veces.

Código corregido:"""

from multiprocessing import Process, RLock

def task(lock):
    print("Adquiriendo el lock... ", flush=True)
    with lock:
        print("Adquiriendo el lock otra vez...", flush=True)
        with lock:
            pass  # Esto ahora es seguro con RLock

if __name__ == '__main__':
    lock = RLock()
    process = Process(target=task, args=(lock,))
    process.start()
    process.join()