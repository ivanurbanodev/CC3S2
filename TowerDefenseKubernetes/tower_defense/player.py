# Representa al jugador y sus estadísticas
class Player:
    def __init__(self):
        # Inicializa la puntuación y la salud de la base
        self.score = 0
        self.base_health = 100

    def get_score(self):
        # Devuelve la puntuación del jugador
        return self.score

    def get_base_health(self):
        # Devuelve la salud actual de la base
        return self.base_health
