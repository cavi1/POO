from persona import Persona
from datetime import datetime

humano1=Persona("queso","ortiz",datetime(2003,9,7))
humano2=Persona("chele","gonzales",datetime(2003,10,14))
humano3=Persona("mazzu","caca",datetime(2004,2,27))

print(humano1.to_string())
print(humano2.to_string())
print(humano3.to_string())