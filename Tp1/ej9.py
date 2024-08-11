#para poder usar un método para generar numeros aleatorios, se precisa importar la librería random, para hacerlo:
import random

#la librería random posee funciones que permiten generar todo tipo de numeros aleatorios, para enteros: nro=random.randint(intPiso,intTope)
#para flotantes: nro=random.uniform(floatPiso,floatTope)
#para flotantes entre 0 y 1:  nro=random.random()
#para numeros aleatorios de una lista selecta de valores: nro=random.choice([10,20,30,40,50,60,...,n]) no importa ni el orden ni el tipo de los datos en este caso

ingreso_usuario=input("ingrese un numero entero: \n")

ingreso_usuario_int=int(ingreso_usuario)

nro_aleat=random.randint(1,10)

if ingreso_usuario_int != nro_aleat:
    print(f"{ingreso_usuario_int} es distinto a {nro_aleat}")
    
if ingreso_usuario_int < nro_aleat:
    print(f"{ingreso_usuario_int} es menor a {nro_aleat}")

if ingreso_usuario_int <= nro_aleat:
    print(f"{ingreso_usuario_int} es menor o igual a {nro_aleat}")
    
if ingreso_usuario_int > nro_aleat:
    print(f"{ingreso_usuario_int} es mayor o igual a {nro_aleat}")
    
if ingreso_usuario_int >= nro_aleat:
    print(f"{ingreso_usuario_int} es mayor o igual a {nro_aleat}")
    
if ingreso_usuario_int == nro_aleat:
    print(f"{ingreso_usuario_int} es igual a {nro_aleat}")