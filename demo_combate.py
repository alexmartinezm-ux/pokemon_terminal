"""Demo visual de combate Pokemon en terminal con rich.

Uso:
    pip install rich
    python demo_combate.py
"""
import random
import time
from dataclasses import dataclass

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


@dataclass
class Pokemon:
    nombre: str
    nivel: int
    hp: int
    hp_max: int
    ataques: list


# ---------- Vista ----------

def barra_vida(actual, maximo, ancho=20):
    actual = max(actual, 0)
    ratio = actual / maximo
    llenos = round(ratio * ancho)
    color = "green" if ratio > 0.5 else "yellow" if ratio > 0.2 else "red"

    barra = Text("█" * llenos, style=color)
    barra.append("░" * (ancho - llenos), style="dim")
    barra.append(f" {actual}/{maximo}")
    return barra


def panel_pokemon(p, borde):
    contenido = Text(f"{p.nombre}  Nv.{p.nivel}\n", style="bold")
    contenido.append("HP ")
    contenido.append_text(barra_vida(p.hp, p.hp_max))
    return Panel(contenido, width=38, border_style=borde)


def mostrar_combate(jugador, rival, mensajes=None):
    console.clear()
    escena = Table.grid(expand=True)
    escena.add_column(justify="left")
    escena.add_column(justify="right")
    escena.add_row("", panel_pokemon(rival, "red"))
    escena.add_row(panel_pokemon(jugador, "cyan"), "")
    console.print(escena)

    if mensajes:
        console.print(Panel("\n".join(mensajes), title="Combate", border_style="white"))


def animar_dano(jugador, rival, objetivo, dano, mensajes=None, pausa=0.03):
    """Baja la vida punto a punto para dar sensación de animación."""
    for _ in range(dano):
        if objetivo.hp <= 0:
            break
        objetivo.hp -= 1
        mostrar_combate(jugador, rival, mensajes)
        time.sleep(pausa)


# ---------- Lógica mínima de la demo ----------

def turno(atacante, defensor, jugador, rival):
    ataque = random.choice(atacante.ataques)
    dano = random.randint(8, 22)
    mensajes = [f"¡{atacante.nombre} usa {ataque}!"]

    mostrar_combate(jugador, rival, mensajes)
    time.sleep(1)

    mensajes.append(f"{defensor.nombre} pierde {min(dano, defensor.hp)} HP")
    animar_dano(jugador, rival, defensor, dano, mensajes)
    time.sleep(0.8)


def main():
    pikachu = Pokemon("Pikachu", random.randint(10, 20), 100, 100,
                      ["Impactrueno", "Ataque Rápido", "Cola Férrea"])
    charmander = Pokemon("Charmander", random.randint(10, 20), 100, 100,
                         ["Ascuas", "Arañazo", "Lanzallamas"])

    mostrar_combate(pikachu, charmander, [f"¡Un {charmander.nombre} salvaje apareció!"])
    time.sleep(1.5)

    atacante, defensor = pikachu, charmander
    while pikachu.hp > 0 and charmander.hp > 0:
        turno(atacante, defensor, pikachu, charmander)
        atacante, defensor = defensor, atacante

    ganador = pikachu if pikachu.hp > 0 else charmander
    mostrar_combate(pikachu, charmander, [f"¡{ganador.nombre} ha ganado el combate!"])


if __name__ == "__main__":
    main()
