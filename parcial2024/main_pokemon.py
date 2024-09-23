from pokemon_tipo_hierba import Pokemon_tipo_hierba
from pokemon_tipo_agua import Pokemon_tipo_agua
from pokemon_tipo_fuego import Pokemon_tipo_fuego
from entrenador import Entrenador
import random
lista_pokemon=[]

for i in range(10):#lista con pokemon al azar
    aleat=random.randint(1,3)
    if aleat == 1:
        pokemonX=Pokemon_tipo_agua(f"pokemon{i}")
        lista_pokemon.append(pokemonX)
    elif aleat == 2:
        pokemonX=Pokemon_tipo_hierba(f"pokemon{i}")
        lista_pokemon.append(pokemonX)
    else:
        pokemonX=Pokemon_tipo_fuego(f"pokemon{i}")
        lista_pokemon.append(pokemonX)
        
pokemon_de_cavi=Pokemon_tipo_fuego("Charmander")        
EntrenadorX=Entrenador("Cavi",random.randint(1,100),pokemon_de_cavi)

for poke_salvaje in lista_pokemon: #puede pasar : 1)que el pokemon muera 2)que el pokemon sea atrapado 3) que el pokemon no muera pero se agoten los intentos
    print("------------------------------------------")
    EntrenadorX.atrapar(pokemon_de_cavi, poke_salvaje)
    print("------------------------------------------")
    
print(f"Nombre Entrenador: {EntrenadorX.get_nombre_entrenador()} Nivel entrenador: {EntrenadorX.get_nivel_entrenador()}")
print("Pokedex: ")
EntrenadorX.get_pokedex()


#me tira un none porque  me falto la impresión de algun atributo pero no me estoy dando cuenta cual (no me queda tiempo)