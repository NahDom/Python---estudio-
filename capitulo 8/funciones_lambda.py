"""
    En este apartado me dedico al estudio de las funciones en python
"""
# definicion de una funcion cualquiera

# Saludo

def saludo(username):
    print(f"hello, {username}")
    
saludo("Nahuel")

"""libros"""
def libro(libro):
    print(f"Uno de mis libros favoritos es {libro}")
    
libro("Gente Ansiosa")

# Funciones con argumentos posicionales
"""Nombre de mascotas"""
def describe_mascot(animal, name):
    print(f"\nI have an {animal}")
    print(f"My {animal}'s name is {name.title()}")
    
describe_mascot("Dog", "Toto")

chicos = ['juan', 'paco', 'paco']
chicas = ['romina', 'denise', 'pilar']

# no hace correctamente la mezcla
for x in chicas:
    for j in chicos:
        parejas = (x,j)
print(parejas)

# la realiza por medio de funciones lambda
parejas = {(x,j) for x in chicas for j in chicos}
print(parejas)


