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

# a veces complejizar una funcion es mas contraproducente que otra cosa

def mensaje(llamar):
    print(f"{llamar}, esta aprendiendo funciones en python!!")
    
mensaje('Nahuel')

# paso por clave y paso por posicion

def reservar(destino, precio= 1000):
    print(f"Usted a reservado un viaje a {destino}, por {precio} dolares")

reservar('mar de ajo', 500)

# mayor o menor
def extrae(valores, comparacion):
    a = valores[0]
    for x in valores[1:]:
        if comparacion(x,a):
            a=x
    return a

def mayor(a,b):
    return a > b
def menor(a,b):
    return a < b
print(extrae([2,3,6,8,10],mayor))
print(extrae([0,1,2,3,4,5,6,7,8,9,10],menor))