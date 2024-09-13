import random
from carta import Carta
from carta_bronce_especial import Carta_bronce_especial
from carta_oro import Carta_oro
from carta_especial import Carta_especial
from plantilla import Plantilla	

lista_clubes=["Arsenal","Montevideo City Torque", "Inter Miami", "Manchester City"]
lista_paises=["Argentina","Inglaterra","Holanda","Japón"]
lista_habilidades=["Ataque","Pase","Defensa"]
lista_cartas=[]

for i in range(22):
    num_aleat=random.randint(1,3)
    if num_aleat==1:
        carta_bronce=Carta_bronce_especial(f"jugador{i}",random.choice(lista_clubes),random.choice(lista_paises),random.choice(lista_habilidades))
        lista_cartas.append(carta_bronce)
    elif num_aleat==2:
        carta_oro=Carta_oro(f"jugador{i}",random.choice(lista_clubes),random.choice(lista_paises))
        lista_cartas.append(carta_oro)
    else:
        carta_especial=Carta_especial(f"jugador{i}",random.choice(lista_clubes),random.choice(lista_paises))
        lista_cartas.append(carta_especial)
        
equipo1=Plantilla("Cavi", "Japón", "Inter Miami")
equipo2=Plantilla("Chela", "Argentina", "Arsenal")

random.shuffle(lista_cartas)

for i in lista_cartas: #voy recorriendo la lista que desordené con el shuffle y segun el numero que toque lo agrego a alguno de los 2 equipos
    num_aleat=random.randint(1,2)
    if num_aleat==1 and not equipo1.equipo_lleno():
        equipo1.agrega_carta(i)
    else:
        equipo2.agrega_carta(i)
        
equipo1.get_equipo()
print(equipo1.calcular_quimica_plantilla())

        


#carta1_bronce=Carta_bronce_especial("leo","PSG","argentina","pase")
#carta1_oro=Carta_oro("cr7","Barca","brasil")
#carta1_especial=Carta_especial("neymar","Boca","China")
#print(carta1_bronce.carta_to_string())
#print(carta1_oro.carta_to_string())
#print(carta1_especial.carta_to_string())