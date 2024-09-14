from cuenta_billetera_virtual import Cuenta_billetera_virtual
from cuenta_bancaria import Cuenta_bancaria
from impuesto import Impuesto
import random

cuenta1=Cuenta_billetera_virtual("Cavi")
cuenta2=Cuenta_bancaria("Chela")

lista_impuestos=[]

for i in range(20):
    impuestoX=Impuesto(f"impuesto{i}")
    lista_impuestos.append(impuestoX)
    
    
random.shuffle(lista_impuestos)

print(f"Saldo cuenta de cavi {cuenta1.get_saldo()}")