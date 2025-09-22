"""
    Entrada del usuario 
    En este capitulo se ahonda sobre el bucle while
    la funcion input y la interactividad de los programas en python
"""
# primer ejemplo

mensaje  = input("Dime algo y lo repetire: ")
print(mensaje)

# interesante no sabia que python permitia una concatenacion de texto de tipo lineas subsecuentes

edad = int(input('ingrese su edad: '))
print(type(edad))
print(edad)
print(edad >= 18)


print(" Mesa para varios")
cantidad_personas = int(input("\tPor favor indique cuantos comeran: "))
if cantidad_personas >= 8:
    print(" Perdonen deberan esperar a la liberacion de la mesa")
else:
    print("Su mesa esta lista")
    
val = 1
val2 = 2

print(f"valor de: {val / val2} y el modulo de {val % val2}")

print(val & val2) # this is a bitwice operator: toma cada pareja de bits de los operandos y solo retorna 1 si ambos bits son también 1
 # 0001 # 0010
 
numero_actual = 1
while numero_actual <= 5:
    print(numero_actual)
    numero_actual += 1
