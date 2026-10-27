import random
from Pokemon import Pokemon
from Entrenador import Entrenador
from Combate import Combate

nombre_entrenador = input("Como te llamas? ")

entrenador = Entrenador(nombre_entrenador)

pokemon1 = Pokemon("Charmander", "Fuego", 14, 7, ["Placaje", "Lanzallamas", "Ascuas"], [4, 6, 10])
pokemon2 = Pokemon("Bulbasaur", "Planta", 15, 8, ["Placaje", "Lazo hierba"], [4, 7])
pokemon3 = Pokemon("Squirtle", "Agua", 16, 9, ["Placaje", "Rayo burbuja"], [4, 5])
pokemon4 = Pokemon("Evee", "Normal", 14, 5, ["Placaje", "Ataque rapido"], [4, 6])
pokemon_rival = Pokemon("Rattata", "Normal", 10, 5, ["Placaje", "Ataque rapido"], [100, 100])

pokemon_inicial = int(input("Selecciona un pokemon (1-3): "))
if pokemon_inicial == 1:
    pokemon_inicial = pokemon1
elif pokemon_inicial == 2:
    pokemon_inicial = pokemon2
elif pokemon_inicial == 3:
    pokemon_inicial = pokemon3
else:
    print("Ese pokemon no existe")

entrenador.pokemons.append(pokemon_inicial)
entrenador.pokemons.append(pokemon4)

combate = Combate(entrenador, pokemon_inicial, pokemon_rival)
combate.combate()