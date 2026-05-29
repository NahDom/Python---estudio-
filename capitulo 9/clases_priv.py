"""definicion de atributos y metodos privados"""

# comenzando con la definicion de una clase comun con atributos publicos
class Auto:
    #atributos
    def __init__(self):
        self.color = 'rojo'
        self.modelo = 'v1'
        self.marca = 'camaro'
        self.encendido = False
        self.velocidad = 0
        self.__llave = '12345' # atributo privado
    # metodos de la clase que son publicos
    def encender(self, llave):
        if self.__llave == llave:
            self.encendido = True
            print("el auto esta encendido")
        else:
            self.encendido = False
            print("Esa no es la llave, se ha llamado a la policia")
    
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
            
camaro1 = Auto()
camaro1.encender("12345")
print("Auto encendido", camaro1.encendido)
