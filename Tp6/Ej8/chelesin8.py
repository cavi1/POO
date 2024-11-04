from random import randint
import time

def sumatoria(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

if __name__ == '__main__':
    mat1 = []
    mat2 = []
    lista = []
    
    # Crear las matrices con números aleatorios
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
    mat_resu = []
    
    # Sumar las matrices sin multiprocessing
    for i in range(5):
        fila_resu = sumatoria(mat1[i], mat2[i])
        mat_resu.append(fila_resu)
        
    end_time = time.time()
    
    print("RESULTADO FINAL de SUMATORIA:", mat_resu)
    print(f"Tiempo de ejecución sin multiprocessing: {end_time - start_time:.100f} segundos")  # Ajustado para más decimales

