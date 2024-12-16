from tower_defense.tower_defense_game import TowerDefenseGame
from tower_defense.map import Map
from tower_defense.player import Player
from tower_defense.wave import Wave
from tower_defense.enemy import Enemy  

class Tower:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

# Punto de entrada del juego
if __name__ == "__main__":
    game = TowerDefenseGame()

    # Crear torres
    tower1 = Tower("T")
    tower2 = Tower("A")

    # Colocar torres en el mapa
    game.place_tower(tower1, 1, 1)
    game.place_tower(tower2, 2, 3)

    # Mostrar el estado inicial del juego
    game.game_state()
