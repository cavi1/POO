import random
from datetime import datetime
from persona import Persona
from familia import Familia

lista = []
for i in range(0,25):
    lista.append(Persona(f"nombre{i}","apellido{i}",datetime(2008,8,12),1,0,"sexo"))

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
cant_familias=0
cant_personas=0
edad_total=0
laburantes=0
puede_trabajar=0
puede_manejar=0
for i in familias:
    cant_familias+=1
    cant_personas+=i.cuenta_integrantes()
    edad_total+=i.cuenta_edades_familia()
    laburantes+=i.cuenta_laburantes_familia()
    for j in  i.retorna_integrantes_familia():
        if j.calc_edad()>=16:
            puede_trabajar+=1
        if j.calc_edad()>=17:
            puede_manejar+=1    
                
print(f"cantidad de familias censadas {cant_familias}")
print(f"cantidad de personas censadas {cant_personas}")
print(f"el promedio de las edades es {edad_total/cant_personas}")
print(f"hay {laburantes} laburantes")    
print(f"{puede_trabajar} personas pueden trabajar")
print(f"{puede_manejar} pueden manejar")

