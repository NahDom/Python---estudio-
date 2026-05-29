class Perro:
    # Constructor de la clase
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

# Instanciando el objeto
mi_perro = Perro("Rex", "Golden Retriever")

# Accediendo a los atributos del objeto
print(mi_perro.nombre)  # Imprime: Rex
