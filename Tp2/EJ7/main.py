import random
from datetime import datetime
from persona import Persona
from familia import Familia

lista = []
for i in range(0,25):
    lista.append(Persona(f"nombre{i}","apellido{i}",datetime(2001,8,12),1,0,"sexo"))

#persona1=Persona("Francisco","Cavieres",datetime(2001,8,12),1,0,"Hombre")
#persona2=Persona("Marcia","Mazzuca",datetime(1966,11,29),1,0,"Mujer")
#persona3=Persona("Ignacio","Cavieres",datetime(2001,2,27),1,0,"Hombre")

familias=[]
for j in range(0,5):
    familia = Familia()
    for i in lista:
        rnd = random.randint(0,3)
        familia.agrega_integrante_familia(i)
        if rnd == 1: 
            familias.append(familia)
            break
total_edades=0
for i in familias:
    print(i.cuenta_edades_familia())
    total_edades+=i

print(f"PROMEDIO EDADES: {}")