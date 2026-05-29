
class Monster:
    def __init__(self, func):
        self.func = func

# clase llamada ataque y tiene 4 metodos morder, contra atacar, cortar, patear

class Ataque:
    def morder(self):
        return 'El monstruo muerde'
    def cortar(self):
        return 'El monstruo corta'
    def strike(self):
        return 'El monstruo contra ataca'
    def patear(self):
        return 'El monstruo patea'
    
# crear un objeto que tome cualquiera de los metodos de la clase ataque

monster = Monster(func=Ataque.cortar)

print(monster)