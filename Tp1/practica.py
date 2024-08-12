#for i, str in enumerate("hola"):
#if i % 2 == 0:
#print(str)


#def elimina_n_primeros_elementos_str_mutable(str,n): 
    #str[0]=str[0][n:]

#def elimina_n_primeros_elementos_str_inmutable(str,n): 
    #str=str[n:]
    #print(str) 
    
#string_mutable=["hola, mundo"] #en realidad es una lista o array que contiene un string, como es mutable, puede modificarse si se pasa como parámetro     
#string_inmutable="hola, mundo" #el tipo string es inmutable, por lo que si lo paso como parámetro, se crea una copia que es la que va ser modificada

#elimina_n_primeros_elementos_str_mutable(string_mutable,7)
#print(string_mutable)

#elimina_n_primeros_elementos_str_inmutable(string_inmutable,7)

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in lista:
    if lista[i]%5==0:
        print(lista[i])