# Tuplas, elementos inmutables 
# podemos modificar el valor de los elementos almacenados en las posiciones de memoria asignadas a las variables de la tupla, lo que no podemos hacer es modificar el tamñapo de la tupla bajo ningun concepto
# las mismas son definidas por el uso de la coma, el parentesis es para diferenciarlas de las listas, esto debido a que estas si funcionarian mas a los arreglos en otros lenguajes en tanto las listas son la version simplificada en codigo de las listas enlazadas que realizamos

dimensiones = (20, 50)
print("dimension de la tupla")

for dimension in dimensiones:
    print(dimension)
    
dimensiones = (30,60)

print("dimension modificada de la tupla")

for dimension in dimensiones:
    print(dimension)
    
menu = 'pizza', 'fideos', 'cafe', 'chorizo', 'ensalada'

for comidas in menu:
    print(comidas)

menu = 'sopa', 'carne asada', 'cafe', 'chorizo', 'ensalada' 

print("\n")
print("nuevo menu")
for comidas in menu:
    print(comidas)
    
