lista = list(range(5))
print(lista[2:len(lista)]) # recordando que python empieza en el indice posterior al indicado
print(len(lista))

iterables = list(range(11))
iterables[len(iterables):] = "hola como estas"
iterables.extend("HOLA")
print(iterables)

for iterable in iterables:
    print(f"\n{iterable}")