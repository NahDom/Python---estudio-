"""
    En este apartado me dedico al estudio de las funciones en python
"""
# definicion de una funcion cualquiera

# Saludo

def saludo(username):
    print(f"hello, {username}")
    
saludo("Nahuel")

def libro(libro):
    print(f"Uno de mis libros favoritos es {libro}")
    
libro("Gente Ansiosa")

def describe_mascot(animal, name):
    print(f"\nI have an {animal}")
    print(f"My {animal}'s name is {name.title()}")
    
describe_mascot("Dog", "Toto")