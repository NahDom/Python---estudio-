"""solo una pequeña prueba"""
"""definicion de atributos y metodos privados"""

# comenzando con la definicion de una clase comun con atributos publicos
class Auto:
    # definicion de los atributos
    # pues...si, en python se puede definir una clase como el pseudocodigo de toda la vida
    # no lo recomiendo pues las cosas que pueden pasar son extrañas pero solamente cuando pruebe algun juego hecho
    # vere si me es util aunque self.atributo sigue siendo mas seguro al menos para la referencia por punteros a la clase instanciada
    color = 'rojo'
    modelo = 'v1'
    marca = 'camaro'
    encendido = False
    velocidad = 0
    llave = '12345'
    # metodos de la clase que son publicos
    def encender(self):
        self.encendido = True
        print("el auto esta encendido")
    
    def acelerar(self):
        if self.encendido:
            self.velocidad = self.velocidad + 1
    
    def frenar(self):
        if self.velocidad > 0:
            self.velocidad = self.velocidad - 1
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            