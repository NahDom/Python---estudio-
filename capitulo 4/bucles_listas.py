# El bucle for
# for iterable (variable temporal) in iterables (lista de elementos):
#       execution bucle

magos = ['merlin', 'alice', 'in chain']

for mago in magos:
        print(f"{mago.title()}, ese fue un gran truco de magia") 
        print(f"no puedo esperar a ver tu siguiente truco mago {mago.title()}!!!\n")

pizzas = ['pepperoni', 'mozzarella', 'quetzo']

for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza.title()}")
    
print("\nDe hecho este libro de python es el mejor!")

lista = []
lista2 = [1,2,3,4,5,6,7,8,9,10]

for numero in lista2:
    if numero / 2:
            lista.append(numero)
    else:
          pass
    
print(lista)

# para pasar un elemento en un for era el elemento que se itera en el iterable