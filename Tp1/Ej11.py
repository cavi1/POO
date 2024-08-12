import random

while True:
    
    nro1=random.getrandbits(10)
    nro2=random.getrandbits(10)

    while nro1==nro2:
        nro1=random.getrandbits(10)
        nro2=random.getrandbits(10)

    if nro1>nro2:
        nroganador=nro1
    else:
        nroganador=nro2 

    ingreso=int(input("escriba '1' para apostar por el valor 1, ó '2' para apostar por el valor 2:\n"))

    while ingreso!=1 and ingreso!=2:
        print("ingreso incorrecto...")
        ingreso=int(input("escriba '1' para apostar por el valor 1, ó '2' para apostar por el valor 2:\n"))
        

    if ingreso==1:
        nroescogido=nro1
        str="primer"
    else:
        nroescogido=nro2
        str="segundo"
        
    if nroescogido==nroganador:
        print(f"apostó por el {str} numero")
        print("usted ganó")
        print(f"nro1:{nro1},nro2:{nro2}")
    else:
        print(f"apostó por el {str} numero")
        print("usted perdió")
        print(f"nro1:{nro1},nro2:{nro2}")   
        
    continuar=input("¿quiere volver a jugar?(s/n)").lower()
    
    while continuar !='s' and continuar!='n':
        continuar=input("dato erróneo, ingrese 's' si quiere continuar o 'n' si quiere finalizar el juego: \n").lower()
    
    if continuar=='s':
        continue
    elif continuar=='n':
        break
        
    
print("fin...")