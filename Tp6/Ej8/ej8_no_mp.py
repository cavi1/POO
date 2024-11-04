"""8) Haciendo uso de Pool de multiprocessing, realice una sumatoria de dos matrices de
gran tamaño con números random. Realice la comparativa de realizar el mismo cálculo
de forma secuencial."""


import numpy as np
import time

# Generar dos matrices de 1000x1000 con números aleatorios
matriz1 = np.random.rand(10000, 10000)
matriz2 = np.random.rand(10000, 10000)

# Medir el tiempo de ejecución de la suma
start_time = time.time()
suma_matriz = matriz1 + matriz2
end_time = time.time()

# Mostrar el tiempo de ejecución
print(f"Tiempo de ejecución sin multiprocessing: {end_time - start_time:.4f} segundos")


