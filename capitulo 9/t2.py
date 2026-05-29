# test = numero = [x for x in range(10)]
# print(dir(test))
# print(dir(list))
""" 
    Python me deja hacer literalmente un bucle for en una sola linea por medio del for 
    si la hago en modo x for x in range de esa forma la creo de una sola vez para pruebas
"""
class Person:
    def __init__(self):
        pass

""" 
    Por ejemplo puedo crear un pseudo clase que sea un metodo, pero esto no es mas que el como se 
    crean los decoradores
"""


# funcion totalmente virgen sin nada cualquiera que la llame la puede usar
# class prueba:
#     def __init__(self, operacion):
#         self.operacion = operacion        

# def cuadrado(a):
#     return a*a

# calculo = prueba(operacion=cuadrado)
# print(calculo.operacion(10))

# crear una clase monstruo con un parametro llamado func y almacenarlo como parametro

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
ataque = Ataque()
monster = Monster(func=ataque.cortar) # advertencia esto no se hace pero lo razone asi xDDDD, hay que hacer que devuelva una clase por medio de la instancia del objeto siendo el parentesis al final de ataque()
print(monster.func())