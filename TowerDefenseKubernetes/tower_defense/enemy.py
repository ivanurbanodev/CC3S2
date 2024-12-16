# Clase base para todos los enemigos
class Enemy:
    def __init__(self, name, health, damage):
        # Inicializa el enemigo con un nombre, salud y daño
        self.name = name
        self.health = health
        self.damage = damage

    def receive_damage(self, damage):
        # Reduce la salud del enemigo y devuelve si sigue vivo
        self.health -= damage
        return self.health > 0

    def __str__(self):
        # Representación del enemigo como cadena
        return f"{self.name} (Salud: {self.health}, Daño: {self.damage})"
