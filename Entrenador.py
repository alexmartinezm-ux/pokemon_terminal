class Entrenador():
    def __init__(self, nombre, pokemons = []):
        self.nombre = nombre
        self.pokemons = pokemons

    def stats(self):
        print(self.nombre)
        print("----------------")
        for pokemon in self.pokemons:
            if pokemon.ps > 0:
                pokemon.printear_nombre_vida()