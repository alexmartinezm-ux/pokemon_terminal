from Entrenador import Entrenador
from Pokemon import Pokemon

class Combate():
    def __init__(self, entrenador: Entrenador, pokemon: Pokemon, pokemon_rival, turno = True):
        self.turno = turno
        self.entrenador = entrenador
        self.pokemon = pokemon
        self.pokemon_rival = pokemon_rival

    def combate(self):
        while self.pokemon.ps > 0 and self.pokemon_rival.ps > 0:
            self.lucha()
            if self.pokemon.ps <= 0:
                self.cambiar_pokemon()

    def lucha(self):
        self.entrenador.stats()
        if self.turno:
            dano = self.pokemon.elegir_ataque()
            self.pokemon_rival.ps -= dano
            print("Estos son los ps restantes:", self.pokemon_rival.ps, "\n")
        else:
            dano_rival = self.pokemon_rival.elegir_ataque(False)
            self.pokemon.ps -= dano_rival
            print("Estos son los ps restantes:", self.pokemon.ps,"\n")
        self.turno = not self.turno

        if self.pokemon.ps <= 0:
            print("Has perdido...")
        if self.pokemon_rival.ps <= 0:
            print("Has ganado!")

    def cambiar_pokemon(self):
        self.entrenador.stats()
        if self.pokemon.ps <= 0:
            pokemon = int(input("Te has quedado sin ps, selecciona otro pokemon: "))
            
            print(self.entrenador.pokemons[pokemon - 1])