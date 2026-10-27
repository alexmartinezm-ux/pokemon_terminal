import random

class Pokemon():
    def __init__(self, nombre, tipo, ps, defensa, lista_ataques_nombres = [], lista_ataques_valores = []):
        self.nombre = nombre
        self.tipo = tipo
        self.ps = ps
        self.defensa = defensa
        self.lista_ataques_nombres = lista_ataques_nombres
        self.lista_ataques_valores = lista_ataques_valores

    def printear_nombre_vida(self):
        print(f"Pokemon: %s (%d ps)" %(self.nombre, self.ps))

    def elegir_ataque(self, turno = True):
        print("Estos son los ataques del pokemon:")
        numero_ataques = len(self.lista_ataques_nombres)
        for i in range(numero_ataques):
            print(i+1, ".", self.lista_ataques_nombres[i], self.lista_ataques_valores[i])

        if not turno:
            ataque = random.randint(1, numero_ataques)
            print("El enemigo ha elegido el ataque:", ataque)
        else:
            ataque = int(input("Escoge un ataque (1, 2, 3): "))
        print(self.lista_ataques_nombres[ataque-1], self.lista_ataques_valores[ataque-1])
      
        return self.lista_ataques_valores[ataque-1]