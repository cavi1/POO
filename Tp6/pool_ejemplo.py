import multiprocessing

def calcular_cuadrado(numero):
    return numero ** 2

if __name__ == '__main__':
    num_procesadores = multiprocessing.cpu_count()
    print("numero de procesadores disponibles:", num_procesadores)
    datos = []
    for i in range(num_procesadores):
        datos.append(i)

    with multiprocessing.Pool(processes=num_procesadores) as pool:
        resultados = pool.map(calcular_cuadrado, datos)

    print("Resultados finales:", resultados)