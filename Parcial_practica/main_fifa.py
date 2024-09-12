from carta import Carta
from carta_bronce_especial import Carta_bronce_especial
from carta_oro import Carta_oro
from carta_especial import Carta_especial

carta1_bronce=Carta_bronce_especial("leo","PSG","argentina","pase")
carta1_oro=Carta_oro("cr7","Barca","brasil")
carta1_especial=Carta_especial("neymar","Boca","China")
print(carta1_bronce.carta_to_string())
print(carta1_oro.carta_to_string())
print(carta1_especial.carta_to_string())