
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