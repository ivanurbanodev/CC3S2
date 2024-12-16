# Representa el mapa del juego
class Map:
    def __init__(self):
        # Inicializa un mapa 5x5 vacío
        self.grid = [[' ' for _ in range(5)] for _ in range(5)]

    def place_tower(self, tower, x, y):
        # Coloca la torre en las coordenadas dadas
        self.grid[x][y] = tower.get_symbol()

    def __str__(self):
        # Representa el mapa como una cadena
        result = ""
        for row in self.grid:
            for cell in row:
                result += f"[{cell}]"
            result += "\n"
        return result
