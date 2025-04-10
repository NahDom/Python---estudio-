invitados = ['tralalero tralala', 'juliana', 'denise', 'vaca saturna saturnita', 'Carlos', 'ferra', 'lautaro', 'tung tung tung shakur']

print("Lista ordenada: ")
print(sorted(invitados)) # inversion temporal de la lista

print("Lista original: ")
print(invitados)

# Es mas facil ordenar por orden alfabetico si son minusculas que mayusculas, las mayusculas son mas complejas debido al alfabeto del cual deben de basarse

# el metodo sort(reverse=True) si cambia el orden de la lista en forma ordenada por una condicion, PERO el metodo reverse() nada mas la invierte a la lista

# El tamaño de la lista se puede saber con el metodo len(lista)

len(invitados) # solo esta en memoria
print(len(invitados)) # aqui si muestra cuantos elementos hay en la lista

paises = ['suiza', 'finlandia', 'japon', 'china', 'eeuu']
print(paises)
print("Lista invertida temporalmente")
print(sorted(paises))
print(paises)
print(" ")
print("Lista revertida en forma temporal")
print(sorted(paises,reverse=True))
print(" ")
print("Lista con metodo de cadenas aplicados a listas")
print(paises[::-1]) # esto es temporal tambien
print(" ")
print("Lista revertida")
paises.reverse()
print(paises)
print("Devuelta a su orden original ")
paises.reverse()
print(paises)
print("Lista ordenada ")
paises.sort()
print(paises)
print("Lista devuelta al orden original con sort")
paises.sort(reverse=True)
print(paises)

