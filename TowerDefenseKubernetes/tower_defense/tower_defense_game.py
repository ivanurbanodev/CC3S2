from tower_defense.wave import Wave
from tower_defense.map import Map
from tower_defense.player import Player

class TowerDefenseGame:
    def __init__(self):
        self.map = Map()  # Instancia del mapa
        self.player = Player()  # Instancia del jugador
        self.waves = []  # Lista de oleadas

    def place_tower(self, tower, x, y):
        # Coloca una torre en el mapa en las coordenadas especificadas
        self.map.place_tower(tower, x, y)

    def start_wave(self):
        # Inicia una nueva oleada
        wave = Wave()
        self.waves.append(wave)
        wave.start()

    def game_state(self):
        # Muestra el estado actual del juego
        print(self.map)
        print(f"Puntuación: {self.player.get_score()}")
        print(f"Vida de la base: {self.player.get_base_health()}")
