import threading

# Variable compartida
contador = 0

# Lock para evitar condiciones de carrera
#lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(5000):
        # Usar lock para asegurar la exclusión mutua
        #with lock:
        contador += 1

# Crear una lista para los threads
threads = []

# Crear y lanzar 4 threads
for i in range(4):
    thread = threading.Thread(target=incrementar)
    threads.append(thread)
    thread.start()

# Esperar a que todos los threads terminen
#for thread in threads:
    #thread.join()

# Imprimir el valor final del contador
print("Valor final del contador:", contador)