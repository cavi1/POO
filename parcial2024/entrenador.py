import random

class Entrenador:
    def __init__(self,nombre,nivel_entrenador,pokemon_principal):
        self.__nombre=nombre
        self.__nivel_entrenador=nivel_entrenador
        self.__pokemon_principal=pokemon_principal
        self.__pokedex=[]

    def atrapar(self,pokemon_de_entrenador, pokemon_salvaje):
        pokemon_muerto=False
        limite_combates=0
        capturado=False
        while not pokemon_muerto and limite_combates<=2 and capturado==False:
            if self.__nivel_entrenador>pokemon_salvaje.get_salvajismo():
                print("El pokemón ha sido capturado con éxito!!")
                self.__pokedex.append(pokemon_salvaje)
                capturado=True
            else:
                print("El nivel de salvajismo del pokemon supera el nivel del entrenador!!")
                print("Procediendo al combate...")
                self.combate(pokemon_de_entrenador,pokemon_salvaje)
                if pokemon_salvaje.get_vida()<=0:
                    pokemon_muerto=True
            limite_combates+=1   
        if pokemon_muerto:
            print("RIP")
        
    def combate(self, pokemon_de_entrenador, pokemon_salvaje):    
        pokemon_de_entrenador.atacar(pokemon_salvaje)
        pokemon_salvaje.disminuir_salvajismo()
        

    def get_nombre_entrenador(self):
        return self.__nombre
    
    def get_nivel_entrenador(self):
        return self.__nivel_entrenador    
    
    def get_pokedex(self):
        for pokemon in self.__pokedex:
            print(pokemon.poke_to_string())