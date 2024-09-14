from bronce_especial import Bronce_especial
from oro import Oro
from especial import Especial
from plantilla import  Plantilla
import random
from random import randint

lista_habilidades_especiales = ["Ataque", "Pase", "Defensa"]
lista_clubes = ["Arsenal", "Montevideo City Torque", "Inter Miami", "Manchester City"]
lista_paises = ["Argentina", "Inglaterra", "Holanda", "Japon"]

min_bronce_especial = 49
max_bronce_especial = 65

min_oro = 74
max_oro = 90

min_especial = 89
max_especial = 99

lista_jugadores = []

for i in range(22):
    habilidades = []
    if i <= 7:
        nombre = f"Jugador {i}"
        pais = random.choice(lista_paises)
        club = random.choice(lista_clubes)
        habilidad = random.choice(lista_habilidades_especiales)
        jugador = Bronce_especial (nombre, club, pais, habilidad)
        jugador.set_atributos(max_bronce_especial, min_bronce_especial, 0)
        lista_jugadores.append(jugador)
    if i <= 14:
        nombre = f"jugador {i}"
        pais = random.choice(lista_paises)
        club = random.choice(lista_clubes)
        nro = randint (2,3)
        habilidades = random.sample(lista_habilidades_especiales, nro)
        jugador = Especial (nombre, club, pais)
        jugador.set_lista_habilidades(habilidades)
        jugador.set_atributos(max_especial, min_especial, 2)
        lista_jugadores.append(jugador)
    if i <= 22:
        nombre = f"jugador {i}"
        pais = random.choice(lista_paises)
        club = random.choice(lista_clubes)
        jugador = Oro(nombre, club, pais)
        jugador.set_atributos(max_oro, min_oro, 1)
        lista_jugadores.append(jugador)


pais= random.choice(lista_paises)
club = random.choice(lista_clubes)
equipo1 = Plantilla("dueño1", pais, club)

pais= random.choice(lista_paises)
club = random.choice(lista_clubes)
equipo2 = Plantilla("dueño2", pais, club)

lista_jugadores = random.sample(lista_jugadores, len(lista_jugadores))
for i in range(22):
    if i <= 11:
        equipo1.set_plantilla_jugadores(lista_jugadores[i])
    else:
        equipo2.set_plantilla_jugadores(lista_jugadores[i])

equipo1.imprimir_plantilla()
equipo2.imprimir_plantilla()