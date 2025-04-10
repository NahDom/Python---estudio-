# listas con bucles sencillos
cosas_disponibles =  ['champiñon', 'olives', 'green peppers',
'pepperoni', 'papa frita', 'extra cheese']

cosas_pedidas = ['champiñon','poio','extra cheese']

for pedido in cosas_pedidas:
    if pedido in cosas_disponibles:
        print(f"Adhiriendo a su pedido: {pedido}") 
    else:
        print(f"Disculpe no tenemos: {pedido}")

print("\npedido hecho, disfrute la pipsha")

users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hola, admin, ¿quieres ver un informe de estado?")
else:
    print("Necesitamos usuarios o nos quitan el trabajo")
    
current_users = ['juan', 'jhon', 'peter', 'michael', 'penelope']
new_users = ['juan']

if new_users: #compruebo que la lista de nuevos usuarios no esta vacia
    for user in new_users: #itero sobre la lista de nuevos usuarios
        if user in current_users:
            print("Llegaste tarde otro usuario lo ha puesto antes")
        else:
            print(f"El nombre de usuario esta disponible!.")
            
# lista en ingles

numeros = [1,2,3,4,5,6,7,8,9]
terminacion = ['st','nd','rd','th','th','th','th','th','th']
# Acotacion de python, tal parece las listas son tan dinamicas que puedo el multiplicar una lista de un elemento por algo incluso en la declaracion de variables, asi como tambien cuando vemos sus valores internos
# por ejemplo
terminacion = ['st','nd','rd']+['th']*6 # aqui multiplico por 6 la cantidad de veces que el elemento se suma iteradamente a la lista ya creada
# olvidaba...que los elementos de las listas y arreglos se llaman i por la posicion ordinal interna de la maquina
resultado = []
# si quieres saber el tamaño de la lista para usarlo como un entero para iterar sobre la misma usa len
# El método .join() en Python toma una lista de cadenas (strings) y las une en una sola cadena, utilizando un separador que tú especifiques

# no todo se debe crear en secuencial con un if o un else...para algo el lenguaje tiene tantas herramientas

for numero in range(len(numeros)):
    if numero < 3:
        #recuerda que append va insertando elemento a elemento hasta terminar de hacerlo en orden
        resultado.append(f"{numeros[numero]}{terminacion[numero]}")
    else:
        resultado.append(f"{numeros[numero]}{terminacion[numero]}")
        
print(" ".join(resultado)) #join metodo de cadenas

