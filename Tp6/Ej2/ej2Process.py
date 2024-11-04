# Si trabajamos con multiprocessing tenemos que hacer una
#variable compartida en el main, la sitaxis de if name = main
# es obligatoria, cuando la creamos tenemos que indicar
#que tipo de variable es y su valor inicial y cuando
#referenciamos a ella en el proceso de incrementacion en
#la clase de process tenemos que indicar con el with getlock
#un bloqueo para evitar condiciones de carrera XD. Despues
#en el main cuando creamos el process tenemos que crear un
#objeto de tipo process que referencie al metodo incrementar
#de la clase process que creamos y le indicamos los
#argumentos del mismo proceso, esta todo en la sintaxis

from multiprocessing import Process, Value

class Contador_Numero(Process):
    
    
    def incrementar (variable_compartida):
        for i in range(5000):
            with variable_compartida.get_lock():
                variable_compartida.value += 1

if __name__ == '__main__':
    var_comp = Value('i', 0)

    proceso1 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso1.name} incrementó la variable nashe")
    proceso2 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso2.name} incrementó la variable nashe")
    proceso3 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso3.name} incrementó la variable nashe")
    proceso4 = Process(target=Contador_Numero.incrementar, args=(var_comp,))
    print(f"El proceso {proceso4.name} incrementó la variable nashe")

    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso4.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()
    proceso4.join()

    print ("el valor final de la variable es: ", var_comp.value)
    