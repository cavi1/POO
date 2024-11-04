"""8) Haciendo uso de Pool de multiprocessing, realice una sumatoria de dos matrices de
gran tamaño con números random. Realice la comparativa de realizar el mismo cálculo
de forma secuencial."""


import numpy as np
from multiprocessing import Pool
import multiprocessing
import time

# Función para sumar filas de las matrices
def sumar_filas(args):
    fila1, fila2 = args
    return fila1 + fila2

if __name__ == '__main__':
    
    num_procesadores = multiprocessing.cpu_count()
    # Generar dos matrices de 10000x10000 con números aleatorios
    matriz1 = np.random.rand(10000, 10000)
    matriz2 = np.random.rand(10000, 10000)

    # Crear un Pool de procesos y medir el tiempo de ejecución
    start_time = time.time()
    with multiprocessing.Pool(processes=num_procesadores) as pool:
        resultado = pool.map(sumar_filas, zip(matriz1, matriz2))
    end_time = time.time()

    # Convertir el resultado a una matriz de NumPy
    suma_matriz = np.array(resultado)

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución con multiprocessing: {end_time - start_time:.4f} segundos")