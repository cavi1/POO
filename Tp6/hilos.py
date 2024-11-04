import threading

def imprimir_numeros():
    for i in range(1, 100):
        print(f'Número {i}')
    print("termina ejecución de imprimir_numeros")

def imprimir_letras():
    letras = 'ABCDEEFGHIJKLMNÑOPQRSTUVWXYZ'
    for letra in letras*5:
        print(f'Letra {letra}')
    print("termina ejecución de imprimir_letras")

thread1 = threading.Thread(target=imprimir_numeros)
thread2 = threading.Thread(target=imprimir_letras)

thread1.start()#inicia la ejecución de un hilo
thread2.start()

thread1.join()#espera a que la ejecución termine antes de continuar el programa
thread2.join()
print("termina ejecución de programa")
#si yo en vez de iterar una serie de numeros hiciera una cuenta en la iteracion y quisiera imprimir el resultado y no colocara los join 
#me imprime pura mierda osea seria completamente random lo q imprime