"""Demo: personaje andando por un mapa en terminal con rich + readchar.

Uso:
    pip install rich readchar
    python demo_mapa.py

Controles: WASD o flechas para moverse, Q para salir.
"""
import random
from dataclasses import dataclass

import readchar
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

console = Console()

# ---------- Datos del mapa ----------
# '#' muro, '.' camino, '"' hierba alta, '~' agua, 'T' árbol
MAPA = [
    "########################",
    "#......T.....~~~.......#",
    "#..\"\"\"..T....~~~~.\"\"\"..#",
    "#..\"\"\".......~~~..\"\"\"..#",
    "#.......TTT.........T..#",
    "#.\"\"\"\".......\"\"\"\"....T.#",
    "#.\"\"\"\"..T....\"\"\"\"......#",
    "#.......T..............#",
    "########################",
]

# carácter -> (cómo se dibuja, estilo, ¿se puede pisar?)
TILES = {
    "#": ("█", "grey37", False),
    ".": ("·", "grey30", True),
    '"': ('"', "green", True),
    "~": ("≈", "blue", False),
    "T": ("♣", "dark_green", False),
}

MOVIMIENTOS = {
    "w": (0, -1), readchar.key.UP: (0, -1),
    "s": (0, 1), readchar.key.DOWN: (0, 1),
    "a": (-1, 0), readchar.key.LEFT: (-1, 0),
    "d": (1, 0), readchar.key.RIGHT: (1, 0),
}


@dataclass
class Jugador:
    x: int
    y: int


# ---------- Lógica (sin print) ----------

def es_transitable(x, y):
    if not (0 <= y < len(MAPA) and 0 <= x < len(MAPA[y])):
        return False
    return TILES[MAPA[y][x]][2]


def mover(jugador, dx, dy):
    """Devuelve True si se ha movido."""
    nx, ny = jugador.x + dx, jugador.y + dy
    if es_transitable(nx, ny):
        jugador.x, jugador.y = nx, ny
        return True
    return False


def encuentro_salvaje(jugador):
    """10% de probabilidad de encuentro al pisar hierba alta."""
    return MAPA[jugador.y][jugador.x] == '"' and random.random() < 0.10


# ---------- Vista ----------

def dibujar(jugador, mensaje=""):
    texto = Text()
    for y, fila in enumerate(MAPA):
        for x, c in enumerate(fila):
            if (x, y) == (jugador.x, jugador.y):
                texto.append("@", style="bold yellow")
            else:
                caracter, estilo, _ = TILES[c]
                texto.append(caracter, style=estilo)
        texto.append("\n")
    texto.append(f"\n{mensaje}", style="bold")
    return Panel(texto, title="Mapa", subtitle="WASD/flechas · Q salir", width=40)


def main():
    jugador = Jugador(1, 1)
    mensaje = "Explora el mapa. La hierba alta esconde sorpresas."

    with Live(dibujar(jugador, mensaje), console=console,
              screen=True, auto_refresh=False) as live:
        while True:
            tecla = readchar.readkey()
            if tecla.lower() == "q":
                break

            if tecla in MOVIMIENTOS:
                dx, dy = MOVIMIENTOS[tecla]
                if not mover(jugador, dx, dy):
                    mensaje = "No puedes pasar por ahí."
                elif encuentro_salvaje(jugador):
                    mensaje = "¡Un Pokémon salvaje apareció!"
                    # Aquí llamarías a vuestro mostrar_combate / Batalla
                else:
                    mensaje = ""

            live.update(dibujar(jugador, mensaje), refresh=True)


if __name__ == "__main__":
    main()
