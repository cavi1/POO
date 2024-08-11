import random

while True:

nro1=random.getrandbits(10) #lo hago del 1 al 1024 por ej
nro2=random.getrandbits(10)

while nro1==nro2:
    nro1=random.getrandbits(10)
    nro2=random.getrandbits(10)
    
if nro1>nro2:
    ganador1=True
    ganador2=False
else:
    ganador1=False
    ganador2=True
    
print("los valores han sido generados...")
print("el valor mas grande gana...")

rta=input("Ingrese '1' si quiere apostar por el valor 1 o '2' si quiere apostar por el valor 2")

while rta !=1 and rta !=2:

    print("valor incorrecto")
    print("debe ingresar '1' si quiere apostar por el valor 1 o '2' si quiere apostar por el valor 2")
    print("ingrese nuevamente")
    
    
if ganador1 and rta==1:
    print("usted ganó")
    print(f"numero elegido: {nro1}, resultó ser mayor que el otro número, que era {nro2}")
else:
    print("usted perdió...")  
    print(f"numero elegido: {nro1}, resultó ser menor que el otro número, que era {nro2}")
    
if ganador2 and rta==2:
    print("usted ganó")
    print(f"numero elegido: {nro1}, resultó ser mayor que el otro número, que era {nro2}")
else:
    print("usted perdió...")  
    print(f"numero elegido: {nro1}, resultó ser menor que el otro número, que era {nro2}")    
    
seguir=input("ingrese 's' is desea seguir jugando, 'n' si desea kitear")

if seguir==n:

break

