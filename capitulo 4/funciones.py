# Funcion range()

#for value in range(6):
#    print(value)
    
cuadrados = [valor**2 for valor in range(1,11)]
print(cuadrados)

for valor in range(1,11):
    cuadrados.append(valor ** 3)

print(cuadrados)

valor = list(range(1,101))

print(max(valor))
print(min(valor))
print(sum(valor))

lista_20 = [value for value in range(1,1_000_001)]
print(max(lista_20))
print(min(lista_20))
print(sum(lista_20))

treses = []
for trece in range(1,31):
    treses.append(trece)
    
print(treses) #adhiero todo a la lista de treces

cubito = [cubo**3 for cubo in range(1,11)] # lista de cubos
print(cubito)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
#print(players[-1:]) # el : donde termina y el :: donde empieza
#print(players[::3])
#print(players)
print("Aqui estan los primeros 3 jugadores")
de_reserva = []
for player in players[:3]:
    print(player.title())
    
juegos_fav = ['gow', 'rdr','gta']
friend_list = juegos_fav[:] #con [:] copio todos los elementos de la lista original a la lista que necesito para copiarla
juegos_fav.append('tetris')
friend_list.append('aristo put as')
print(f"Mis juegos favoritos son {juegos_fav}")
print(f"Sus juegos favoritos son {friend_list}")

print("\n")

lista = [0, 1, 2, 3, 4, 5, 6]

print(f"Estos son los primeros 3 elementos de mi lista: {lista[:3]}")
print(f"Estos son los 3 elementos del medio de mi lista: {lista[2:5]}")
# Ahora quiero mostrar los 3 ultimos para ello tengo dos varaintes pero usando el [elemento ::] que me dice desde tal elemento hasta el final
print(f"Estos son los 3 elementos ultimos de mi lista: {lista[-3::]}")
print(f"Estos son los 3 elementos ultimos de mi lista: {lista[4::]}")

print("\n")

pizzas_mias = ['calabreso', 'anvorgueso', 'chipiorca']
pizza_amigo = pizzas_mias[:]

print("Mis pizzas favoritas son: ")

for pija in pizzas_mias:
    print(pija)

pizzas_mias.append('italiana')
print(pizzas_mias)

print("Sus pizzas favoritas son: ")

for pi_or in pizza_amigo:
    print(pi_or)

pizza_amigo.append('chicago')
print(pizza_amigo)