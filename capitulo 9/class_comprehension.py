"""creando una clase de monstruo"""

class Monster:
    # atributos
    def __init__(self, health, energy, speed):
        self.healt = health
        self.energy = energy
        self.speed = speed
    
    # metodos
    def attack(self, cantidad):
        print("monster made an attack")
        print(f'La cantidad de daño inflingido fue de {cantidad}')
        print(self.energy)
    
    def move(self, aceleracion):
        print(f"The monster has made a move with {self.speed + aceleracion}")
        print(self.speed)

    def __str__(self):
        return f"el monstruo tiene {self.healt} de vida y {self.energy} de energia total"
    
monster = Monster(100, 90,20)
print(monster)

