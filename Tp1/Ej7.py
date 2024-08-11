accum=0

for i in range(2): #una de las miles de formas de hacer un bucle
                    #en este caso el bucle itera el numero de veces determinado en el método range
    rta = input("ingrese el entero " + str(i+1) + "\n")
    nro=int(rta)
    accum+=nro

#formas de concatenar tipos en prints 
#1 castear al tipo: 
    
print("la respuesta es: " + str(accum) )

#2 interpolacion de cadenas

print(f"la respuesta es: {accum} "  )

#3 método format

print("la respuesta es: {} ".format(accum))

#4 dividir en argumentos

print("la respuesta es:",accum) #ya me toma el espacio

#5 con el operador %

print("la respuesta es: %d" %accum)

