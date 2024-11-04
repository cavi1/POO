import multiprocessing
from random import randint
import time

def sumatoria(argumentos):
    list1, list2 = argumentos
    return list1 + list2

if __name__ == '__main__':
    mat1 = []
    mat2 = []
    lista = []
    for j in range(5):
        lista = []
        for i in range(5):
            numran = randint(10, 70)
            lista.append(numran)
        mat1.append(lista)
    
    for j in range(5):
        lista = []
        for i in range(5):
            numran = randint(10, 70)
            lista.append(numran)
        mat2.append(lista)
    
    print("matriz1:", mat1)
    print("matriz2:", mat2)
    start_time = time.time()
    with multiprocessing.Pool(processes = 5) as pool:
        mat_resu = []
        for i in range(5):
            fila_mat1 = mat1[i]
            fila_mat2 = mat2[i]
            argumentos = list(zip(fila_mat1, fila_mat2))
            fila_resu = pool.map(sumatoria, argumentos)
            mat_resu.append(fila_resu)
    end_time = time.time()
    print ("RESULtado FinaAL de SuMAToria:", mat_resu)
    print(f"Tiempo de ejecución con multiprocessing: {end_time - start_time:.4f} segundos")