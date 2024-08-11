peso=input("ingrese su peso: \n")
altura=input("ingrese su altura: \n")

peso_float=float(peso)
altura_float=float(altura)

IMC=peso_float/altura_float**2

print(f"el índice de masa corporal es {IMC:.3f}") #notacion para restringir deicmales en la impresión de un flotante